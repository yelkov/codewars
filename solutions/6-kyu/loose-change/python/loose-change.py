def loose_change(cents):
    #trying not to use loops at all
    cents = int(cents) 
    change = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents > 0:
        quartersValue = cents // 25
        change['Quarters'] = quartersValue
        resto = cents - quartersValue * 25

        dimesValue = resto // 10
        change['Dimes'] = dimesValue
        resto = resto - dimesValue * 10

        nickelsValue = resto // 5
        change['Nickels'] = nickelsValue
        resto = resto - nickelsValue * 5

        penniesValue = resto // 1
        change['Pennies'] = penniesValue

        return change
    else:
        return change
    

#first solution:

def loose_change(cents):
    coinKeys = ['Nickels', 'Pennies', 'Dimes', 'Quarters']
    coinValues = [5, 1, 10, 25]

    wallet = dict(zip(coinKeys, coinValues))

    coins = list(sorted(wallet.values()))

    change = []
    i = len(coins) - 1
    while cents > 0 and i >= 0:
        if cents >= coins[i]:
            cents = cents - coins[i]
            change.append(coins[i])
        else:
            i -= 1

    change_dict = dict.fromkeys(coinKeys, 0)
    for coin in change:
        for coinKeys in wallet:
            if wallet[coinKeys] == coin:
                change_dict[coinKeys] += 1

    return change_dict
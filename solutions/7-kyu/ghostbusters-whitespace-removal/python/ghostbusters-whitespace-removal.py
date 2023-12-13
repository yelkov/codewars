def ghostbusters(building):
    if building.find(" ") == -1:
        return "You just wanted my autograph didn't you?"
    else:
        return building.replace(" ","")
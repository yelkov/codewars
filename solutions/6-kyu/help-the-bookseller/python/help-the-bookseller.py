def stock_list(list_of_books, categorie):
    if list_of_books == [] or categorie == []:
        return ""
    
    book_dictionary = {}
    final_string = ""
    for letter in categorie:

        book_dictionary[letter] = 0

        for bundle in list_of_books:
            
            number = int(bundle.split()[-1])

            if bundle[0] == letter:
                book_dictionary[letter] += number

    final_string = " - ".join([f"({k} : {v})" for k, v in book_dictionary.items()])
        
    return final_string

#firs solution:

def stock_list(list_of_books, categorie):
    
    base_string = ""
    
    if list_of_books == [] or categorie == []:
        return base_string
    
    book_dictionary = {}
    final_string = ""
    for letter in categorie:

        book_dictionary[letter] = 0

        for bundle in list_of_books:
            
            number = int(bundle.split()[-1])

            if bundle[0] == letter:
                book_dictionary[letter] += number

    final_string = " - ".join([f"({key} : {value})" for key, value in book_dictionary.items()])
        
    return final_string
def print_upper_words(list):
    """capitalize each word and print"""

    for word in list:
        if word.upper().startswith('E') == True:
            print(word.upper() + '\n')

print_upper_words(['bob','enormous','glory', 'name', 'entertain', '34df', 'Everywhere'])
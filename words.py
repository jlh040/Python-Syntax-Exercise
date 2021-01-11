def print_upper_words(list, must_start_with):
    """Capitalize and print each word that starts with 'e'."""

    for word in list:
        if word[0] in must_start_with:
            print(word.upper() + '\n')

print('Should print BOB and GLORY \n')
print_upper_words(['bob','enormous','glory', 'name', 'entertain', '34df', 'Everywhere'], must_start_with={'g', 'b'})

print('Should print ZOOKEEPER \n')
print_upper_words(['banana', 'Cat', 'dog', 'angel', 'zookeeper', 'facemask'], {'v', 'z'})

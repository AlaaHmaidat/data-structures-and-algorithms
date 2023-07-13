def repeated_word(string):
    '''
    Finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    '''
    if len(string) == 0:
        return '', 'The str is empty', []

    string = string.lower().replace('.', '').replace('...', '').replace(',', '')

    words = string.split()

    dic1 = {}
    dic2 = {}

    first_repeated_word = ''

    most_freq = 0
    most_common_word = []

    for i in words:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1

    all_words = dic1.items()

    for word, freq in dic1.items():
        if freq > most_freq:
            most_freq = freq
            most_common_word.append(word)
            

    for i in words:
        if i in dic2:
            if dic2[i] < 2:
                dic2[i] += 1
                first_repeated_word =  i
                break
        else:
            dic2[i] = 1

    return all_words, first_repeated_word, most_common_word


if __name__ == '__main__':
    
    all_words, first_repeated_word, most_common_word = repeated_word("Once upon a time, there was a brave princess who...")
    
    print("All Words:", list(all_words))
    print("First Repeated Word:", first_repeated_word)
    print("Most Common Word:", most_common_word)
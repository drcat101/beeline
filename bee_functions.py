

def compare_two_word_lists(word_list_1, word_list_2):
    """Compare the lists of words both people have found.

    Args:
        word_list_1 (list): Person 1's list of words
        word_list_2 (list): Person 2's list of words

    Returns:
        tuple: list of all words, list of words only person 1 found, 
        list of words only person 2 found
    """

    all_found_words = set(word_list_1).union(set(word_list_2))
    wl1_minus_wl2 = set(word_list_1) - set(word_list_2)
    wl2_minus_wl1 = set(word_list_2) - set(word_list_1)

    return all_found_words, wl1_minus_wl2, wl2_minus_wl1


def find_missing_lengths(found_word_list, lengths_dict):
    """Take the dictionary of lengths and decrease by 1 for every found word. 
    Remove all values that are zero.

    Args:
        found_word_list (list): Joint list of the words we have found
        lengths_dict (dict): Dictionary of the word lengths scraped from the hints page

    Returns:
        dict: Dictionary of the word lengths that have not been found
    """
    for word in found_word_list:
        word = word.upper()
        lengths_dict[word[0]][len(word)]-=1

    for first_letter in lengths_dict.keys():
        lengths_dict[first_letter] = {x:y for x,y in lengths_dict[first_letter].items() if y!=0}
    
    lengths_dict = {x:y for x,y in lengths_dict.items() if y}

    return lengths_dict


def find_missing_bigrams(found_word_list, bigrams_dict):
    """Take the dictionary of bigrams and decrease by 1 for every found word. 
    When the count in the dict reaches 0, remove that key.

    Args:
        found_word_list (list): Joint list of the words we have found
        bigrams_dict (dict): Dictionary of the bigrams scraped from the hints page

    Returns:
        dict: Dictionary of the bigrams that have not been found
    """
    for word in found_word_list:
        word = word.upper()
        bigrams_dict[word[0]][word[:2]]-=1
        if bigrams_dict[word[0]][word[:2]] == 0:
            del bigrams_dict[word[0]][word[:2]]

    bigrams_dict = {x:y for x,y in bigrams_dict.items() if y}

    return bigrams_dict


def find_and_print_missing(word_list_1, word_list_2, lengths_dict, bigrams_dict):
    """_summary_

    Args:
        word_list_1 (_type_): _description_
        word_list_2 (_type_): _description_
        lengths_dict (_type_): _description_
        bigrams_dict (_type_): _description_
    """
    found_word_list, wl1_minus_wl2, wl2_minus_wl1 = compare_two_word_lists(word_list_1, word_list_2)

    print('found list '+ str(found_word_list))
    print('words in first list not in second '+ str(wl1_minus_wl2))
    print('words in second list not in first '+ str(wl2_minus_wl1))

    lengths_dict = find_missing_lengths(found_word_list, lengths_dict)

    bigrams_dict = find_missing_bigrams(found_word_list, bigrams_dict)

    print('')
    for first_letter in bigrams_dict.keys():
        print(f'Bigrams: {bigrams_dict[first_letter]}, lengths: {list(lengths_dict[first_letter].keys())}')

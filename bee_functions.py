#!/usr/bin/env python3

def list_differences(word_list1, word_list2, solutions):
    # assumes word lists are arrays
    # assumes solutions is of the form {letter: {'lengths': {length: num_words}, 'bigrams': {bigram: num_words}}}
    # assumes everything is upper case in solutions
    found_list = set(word_list1).union(set(word_list2))
    wl1_minus_wl2 = set(word_list1) - set(word_list2)
    wl2_minus_wl1 = set(word_list2) - set(word_list1)

    print('found list '+ str(found_list))
    print('words in first list not in second '+ str(wl1_minus_wl2))
    print('words in second list not in first '+ str(wl2_minus_wl1))

    # create found_list dictionary with lengths and bigrams

    found_list_dict = dict()
    
    for word in found_list:
        first_letter = word[0].upper()
        bigram = word[0:2].upper()
        length = len(word)

        if first_letter in found_list_dict.keys():
            length_dict = found_list_dict[first_letter]['lengths']
            bigram_dict = found_list_dict[first_letter]['bigrams']
            update_num_dict(length_dict, length)
            update_num_dict(bigram_dict, bigram)

        else:
            found_list_dict[first_letter] = {'lengths': {length: 1}, 'bigrams': {bigram: 1}}

    # diff found_list_dict with solutions

    diff_dict = dict()
    
    for letter in solutions.keys():
        d = found_list_dict.get(letter, {'lengths': dict(), 'bigrams': dict()})
        found_length_dict = d['lengths']
        found_bigram_dict = d['bigrams']
        solution_length_dict = solutions[letter]['lengths']
        solution_bigram_dict = solutions[letter]['bigrams']

        diff_dict[letter] = {'lengths': dict(), 'bigrams': dict()}

        update_diff_dict(found_length_dict, solution_length_dict, diff_dict[letter]['lengths'])
        update_diff_dict(found_bigram_dict, solution_bigram_dict, diff_dict[letter]['bigrams'])

    # print out the result
    
    for letter in diff_dict.keys():
        print(letter.upper())
        for length, num in diff_dict[letter]['lengths'].items():
            print(str(length) + ' ' + str(num))

        for bigram, num in diff_dict[letter]['bigrams'].items():
            print(bigram.upper() + ' ' + str(num))

        print('\r')
            
                
            
def update_num_dict(d, key):
    if key in d.keys():
        d[key] += 1
    else:
        d[key] = 1
    
def update_diff_dict(found_dict, solution_dict, diff_dict):
    for k in solution_dict.keys():
            diff = solution_dict.get(k) - found_dict.get(k, 0)
            if diff > 0:
                diff_dict[k] = diff

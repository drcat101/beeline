from bee_functions import list_differences, compare_two_word_lists, compare_found_words_to_solutions, convert_found_words_to_dict, print_results

# need error and also what it should have been

known_bug_wl1 = ['Beck', 'Bedeck', 'Bedecked', 'Block', 'Blocked', 'Bocce', 'Bock', 'Cede', 'Ceded', 'Cell', 'Celled', 'Cello', 'Clock', 'Clocked', 'Clod', 'Cobble', 'Cobbled', 'Cock', 'Cocked', 'Code', 'Coded', 'Coed', 'Coke', 'Cooed', 'Cook', 'Cookbook', 'Cooked', 'Cool', 'Cooled', 'Deck', 'Decked', 'Deco', 'Decode', 'Decoded', 'Dock', 'Docked', 'Lock', 'Locked']
known_bug_wl2 = ['Bedeck', 'Bedecked', 'Block', 'Blocked', 'Bocce', 'Cede', 'Ceded', 'Cell', 'Cellblock', 'Celled', 'Clock', 'Clocked', 'Clod', 'Cobble', 'Cobbled', 'Cock', 'Cocked', 'Cockle', 'Coddle', 'Coddled', 'Code', 'Coded', 'Coed', 'Coke', 'Cold', 'Cooed', 'Cook', 'Cookbook', 'Cooked', 'Cool', 'Cooled', 'Deck', 'Decked', 'Deco', 'Decode', 'Decoded', 'Dock', 'Docked', 'Lock', 'Locked', 'Loco']
known_bug_solutions = {'C': {'lengths': {4: 10, 5: 6, 6: 7, 7: 3, 8: 2, 9: 1, 10: 1}, 'bigrams': {'CE': 7, 'CL': 3, 'CO': 20}}, 'B': {'lengths': {4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0, 10: 0}, 'bigrams': {'BE': 3, 'BL': 3, 'BO': 2}}, 'D': {'lengths': {4: 3, 5: 0, 6: 4, 7: 1, 8: 0, 9: 0, 10: 0}, 'bigrams': {'DE': 6, 'DO': 2}}, 'E': {'lengths': {4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 'bigrams': {}}, 'K': {'lengths': {4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 'bigrams': {}}, 'L': {'lengths': {4: 2, 5: 0, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0}, 'bigrams': {'LO': 3}}, 'O': {'lengths': {4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 'bigrams': {}}}

def test_list_differences_simple():
    result = list_differences(['boon', 'bonbon'], ['bonobo'], {'B': {'lengths': {4: 1, 6: 2}, 
                                                                     'bigrams': {'BO': 3}}})
    assert result == {'B': {'bigrams': {}, 'lengths': {}}}


def test_compare_two_word_lists():
    all_found_words, wl1_minus_wl2, wl2_minus_wl1  = compare_two_word_lists(['boon', 'bonbon'], ['bonobo'])
    assert all_found_words == {'boon', 'bonbon', 'bonobo'}
    assert wl1_minus_wl2 == {'boon', 'bonbon'}
    assert wl2_minus_wl1 == {'bonobo'}


def test_convert_found_words_to_dict():
    result = convert_found_words_to_dict({'boon', 'bonbon', 'bonobo'})
    assert result == {'B': {'bigrams': {'BO': 3}, 'lengths': {4: 1, 6: 2}}}


def test_convert_found_words_to_dict_known_bug():
    all_found_words, _, _  = compare_two_word_lists(known_bug_wl1, known_bug_wl2)
    print(all_found_words)
    result = convert_found_words_to_dict(all_found_words)
    assert result == None


def test_compare_found_words_to_solutions():
    result = compare_found_words_to_solutions({'B': {'bigrams': {'BO': 3}, 'lengths': {4: 1, 6: 2}}},
                                              {'B': {'bigrams': {'BO': 4}, 'lengths': {4: 2, 6: 2}}})
    assert result == {'B': {'bigrams': {'BO': 1}, 'lengths': {4: 1}}}
    

def test_print_results():
    result = print_results({'B': {'bigrams': {'BO': 1}, 'lengths': {4: 1}}})
    assert result == "Bigrams: ['BO'], lengths: [4]"
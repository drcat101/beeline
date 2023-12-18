from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import re


def scrape_hints_page():

    todays_date = datetime.today()
    day_of_month = todays_date.strftime('%d')
    date_link = todays_date.strftime('%Y/%m/%d')
    date_element = todays_date.strftime('%Y-%m-%d')

    opts = Options()
    opts.add_argument("--headless")
    browser = Firefox(options=opts)
    browser.get(f'https://www.nytimes.com/{date_link}/crosswords/spelling-bee-forum.html')

    grid_element = browser.find_elements(By.ID, f'{day_of_month}sb-forum-{date_element}')
    child = (grid_element[0].find_elements(By.XPATH, '*'))
    grid_text = child[0].get_attribute('innerText')

    browser.quit()

    return grid_text.split("\n")


def get_lengths_by_letter(first_letter, grid_text_list, todays_lengths):
    lengths_dict = {}
    for grid_line in grid_text_list:
        if grid_line[:2] == first_letter + ':':
            # first 3 characters are letter, :, space
            # last character is sum
            lengths = grid_line[3:-1].replace('-', '0').split()
            for i in range(len(todays_lengths)):
                lengths_dict[int(todays_lengths[i])] = int(lengths[i])
            return lengths_dict
        
    for i in range(len(todays_lengths)):
        lengths_dict[int(todays_lengths[i])] = 0
    return lengths_dict


def get_bigrams_by_letter(first_letter, grid_text_list):
    bigram_dict = {}
    for grid_line in grid_text_list:
        # bigrams have format AC-12
        if re.match(rf'{first_letter}[A-Z]-\d\d?', grid_line):
            bigrams = grid_line.split()
            for bigram in bigrams:
                bigram_dict[bigram[:2]] = int(bigram[3:])
            return bigram_dict
    return bigram_dict


def scrape_and_parse_hints():

    grid_text_list = scrape_hints_page()

    todays_letters = grid_text_list[2].split()
    words_points_pangrams = grid_text_list[4].split()
    todays_lengths = grid_text_list[6].split()[:-1]

    words_points_pangrams_dict = {'words': words_points_pangrams[1],
                    'points': words_points_pangrams[3],
                    'pangrams': words_points_pangrams[5]}

    lengths_dict = {}
    bigrams_dict = {}

    for letter in todays_letters:
        lengths_dict[letter] = get_lengths_by_letter(letter, grid_text_list, todays_lengths)
        bigrams_dict[letter] = get_bigrams_by_letter(letter, grid_text_list)
    
    # TODO assert that the number of words is correct
    # TODO assert that the points total is correct

    return lengths_dict, bigrams_dict, words_points_pangrams_dict

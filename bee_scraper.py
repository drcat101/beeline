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

    grid_text = browser.find_element(By.ID, f'{day_of_month}sb-forum-{date_element}').text

    browser.quit()

    return grid_text


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
        if re.match(f'{first_letter}[A-Z]-\d\d?', grid_line):
            bigrams = grid_line.split()
            for bigram in bigrams:
                bigram_dict[bigram[:2]] = int(bigram[3:])
            return bigram_dict
    return bigram_dict


def scrape_and_parse_hints():
    # TODO also get number of words and number of points

    grid_text = scrape_hints_page()
    grid_text_list = grid_text.split("\n")

    # TODO search for letters and lengths using regex to make it more robust
    todays_letters = grid_text_list[1].split()
    todays_lengths = grid_text_list[3].split()[:-1]

    results_dict = {}
    for letter in todays_letters:
        results_dict[letter] = {'lengths': get_lengths_by_letter(letter, grid_text_list, todays_lengths)}
        results_dict[letter]['bigrams'] = get_bigrams_by_letter(letter, grid_text_list)

    print(results_dict)
    return results_dict


if __name__ == '__main__':
    scrape_and_parse_hints()

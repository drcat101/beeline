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

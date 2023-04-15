from bee_scraper import scrape_hints_page


def test_scrape_hints_page():
    grid_text = scrape_hints_page()

    assert grid_text
    assert grid_text[:6] == 'Center'
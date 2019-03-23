
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# get web driver up and running
driver = webdriver.Chrome("/Users/jasonchan/PycharmProjects/hang-seng-scraping/chromedriver")
driver.get("https://www.hangseng.com/en-hk/e-valuation/address-search/")

# window size to make sure javascript parts does not get hidden
driver.set_window_size(1280, 1024)

def get_area_select():
    path = '//select[@id="areaValue"]'
    area_select_elem = driver.find_element_by_xpath(path)
    area_select = Select(area_select_elem)

    return area_select


def scrape_area():

    area_select = get_area_select()
    area_values = [area.get_attribute('text') for area in area_select.options[1:]]

    return area_values






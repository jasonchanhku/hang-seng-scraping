
from selenium import webdriver

import time
import pandas as pd

# get web driver up and running
driver = webdriver.Chrome("/Users/jasonchan/PycharmProjects/hang-seng-scraping/chromedriver")
driver.get("https://www.hangseng.com/en-hk/e-valuation/address-search/")

# window size to make sure javascript parts does not get hidden
driver.set_window_size(1280, 1024)



path = '//select[@id="areaValue"]'
area_dropdown = driver.find_elements_by_xpath(path)
areas = [area.get_attribute('text') for area in area_dropdown[0].find_elements_by_tag_name('option')]
areas = areas[1:]



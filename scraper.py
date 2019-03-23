
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class Scraper(object):

    def __init__(self):
        self.url = "https://www.hangseng.com/en-hk/e-valuation/address-search/"
        self.driver = webdriver.Chrome("/Users/jasonchan/PycharmProjects/hang-seng-scraping/chromedriver")
        self.driver.set_window_size(1280, 1024)

    def get_area_select(self):
        path = '//select[@id="areaValue"]'
        area_select_elem = self.driver.find_element_by_xpath(path)
        area_select = Select(area_select_elem)

        return area_select

    def load_page(self):
        self.driver.get(self.url)

        def page_loaded(driver):
            path = '//select[@id="areaValue"]'
            return driver.find_element_by_xpath(path)

        wait = WebDriverWait(self.driver, 10)
        wait.until(page_loaded)

    def scrape(self):

        def scrape_area():

            area_select = self.get_area_select()
            area_values = [area.get_attribute('text') for area in area_select.options[1:]]

            return area_values

        self.load_page()

        for area in scrape_area():
            print(area)


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape()

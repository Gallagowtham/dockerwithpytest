from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GooglePage:
    URL = "https://www.google.com"
    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def search(self, keyword):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(keyword + Keys.ENTER)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class googleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_searchInGoogle(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        searchbar = driver.find_element_by_name('q')
        searchbar.send_keys('l4sc0s4ss3h4bl4n3ncl4v3')
        searchbar.send_keys(Keys.ENTER)
        assert driver.find_element_by_xpath("//p[@role='heading']").text in driver.page_source, "Error: word not found"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
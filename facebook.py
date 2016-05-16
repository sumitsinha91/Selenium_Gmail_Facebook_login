import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestFacebook(unittest.TestCase):

	def setUp(self):
		self.deriver = webdriver.Firefox()
		usr = ""
        pwd = ""

    def test_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        self.assertIn("Facebook" in driver.title)
        elem = driver.find_element_by_id("sumitssm")
        elem.send_keys(usr)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        elem = driver.find_element_by_css_selector(".input.textInput")
        elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
        elem = driver.find_element_by_css_selector("input[value=\"Publicar\"]")
        elem.click()

    def tearDown(self):
    	time.sleep(5)
        self.driver.close()
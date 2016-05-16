import unittest
import time
from selenium import webdriver
# from selenium.webdriver.common.keys import keys

class TestGmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):

        driver = self.driver

    	driver.get('https://gmail.com/')
    	self.assertIn('Gmail', driver.title)
    	loginBox = driver.find_element_by_id('Email')
    	loginBox.send_keys('sumitsinha91@gmail.com')
        nextBtw = driver.find_element_by_id('next')
        nextBtw.click()
    	pwdBox = driver.find_element_by_id('Passwd')
    	pwdBox.send_keys('sumitsinha')
    	signinBtw = driver.find_element_by_id('signIn')
    	signinBtw.click()

    def tearDown(self):
    	time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

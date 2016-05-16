import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class TestFacebook(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.facebook.com/')

    def test_login(self):
        driver = self.driver
        facebookUsername = "sumitssm"
        facebookPassword = "sumit"
        emailFieldID = "email"
        passFieldID = "pass"
        loginButtonXpath =  "//input[@value='Log In']"
        
        emailFieldElement = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

class Post(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.get('https://www.facebook.com/post')

    def test_share(self):
        driver = self.driver
        driver = self.driver
        post  = "test"
        textid = "xhpc_message_text"
        buttonid = ".//*[@id='u_jsonp_25_s']/div/div[5]/div/ul/li[2]/button"

        textfiledelemnt = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(textid))
        postbotton     = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(buttonid)

        textfiledelemnt.clear()
        textfiledelemnt.send_keys(post)
        buttonid.click()


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    


if __name__ == '__main__':
    unittest.main()




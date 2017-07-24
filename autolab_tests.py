import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class AutolabTests(unittest.TestCase):
    def setUp(self):
        self.test_url = "http://autolab.cs.cmu.edu/auth/users/sign_in"
    
        local = True
        if local:
            self.driver = webdriver.Chrome()
        else:
            username = 'TODO'
            access_key = 'TODO'
            url = 'http://' + username + ':' + access_key + '@hub.browserstack.com:80/wd/hub'
        
            # See https://www.browserstack.com/automate/python#configure-capabilities
            #  for testing with other devices/browsers
            desired_cap = {'device': 'Motorola Moto X 2nd Gen', 'realMobile': 'true', 'os_version': '5.0'}
            
            self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    def test_forgot_password_visible(self):
        driver = self.driver
        driver.get(self.test_url)
        elem = driver.find_element_by_partial_link_text('Forgot your password')
        assert elem.is_displayed()
            
    def test_blank_login_rejected(self):
        driver = self.driver
        driver.get(self.test_url)
        elem = driver.find_element_by_xpath("//input[@name='commit'][@type='submit']")
        assert elem.is_displayed()
        elem.click()
        assert "Invalid email or password" in driver.page_source
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

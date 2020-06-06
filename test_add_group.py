# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        ws = self.wd
        ws.get("http://localhost/addressbook/")
        ws.find_element_by_name("user").click()
        ws.find_element_by_name("user").clear()
        ws.find_element_by_name("user").send_keys("admin")
        ws.find_element_by_name("pass").click()
        ws.find_element_by_name("pass").clear()
        ws.find_element_by_name("pass").send_keys("secret")
        ws.find_element_by_xpath("//input[@value='Login']").click()
        ws.find_element_by_link_text("groups").click()
        ws.find_element_by_name("new").click()
        ws.find_element_by_name("group_name").click()
        ws.find_element_by_name("group_name").clear()
        ws.find_element_by_name("group_name").send_keys("123")
        ws.find_element_by_name("group_header").click()
        ws.find_element_by_name("group_header").clear()
        ws.find_element_by_name("group_header").send_keys("123")
        ws.find_element_by_name("group_footer").click()
        ws.find_element_by_name("group_footer").clear()
        ws.find_element_by_name("group_footer").send_keys("123")
        ws.find_element_by_name("submit").click()
        ws.find_element_by_link_text("group page").click()
        ws.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

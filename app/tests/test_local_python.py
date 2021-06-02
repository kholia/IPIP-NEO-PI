#!/usr/bin/env python3

"""
The XPath stuff was buggy. We moved away from it and things are fine now!

https://www.softwaretestinghelp.com/radio-buttons-in-selenium/
"""

import time
import unittest
import collections

from common import answers

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from pyquery import PyQuery as pq

# Globals
m = {}
debug = False

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8888/"

    def test_(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_name("Nick").clear()
        driver.find_element_by_name("Nick").send_keys("hello")
        driver.find_element_by_name("Sex").click()
        driver.find_element_by_name("Age").clear()
        driver.find_element_by_name("Age").send_keys("28")

        Select(driver.find_element_by_name('Country')).select_by_index(3)

        if debug:
            end = 9
        else:
            end = 120

        for i in range(0, end):
            name = "Q%s" % (i+1)
            answer_in_range = answers[i]-1
            print(name, answers[i])
            buttons = driver.find_elements_by_name(name)
            buttons[answer_in_range].click()
            """
            xpath = "(//input[@name='Q%s'][@value=%d])" % (i+1, answers[i])
            driver.find_element_by_xpath(xpath).click()
            print(xpath, answers[i])
            """

        if debug:
            time.sleep(120)
        """
        if debug:
            from IPython import embed
            embed()
        """

        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def tearDown(self):
        time.sleep(600)

        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

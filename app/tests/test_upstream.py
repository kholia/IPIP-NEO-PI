#!/usr/bin/env python3

"""
After disabling XPath stuff, things are fine!
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
        self.base_url = "http://www.personal.psu.edu"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/~j5j/IPIP/ipipneo120.htm")
        driver.find_element_by_name("Risk").click()
        driver.find_element_by_name("Accuracy").click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_name("Nick").clear()
        driver.find_element_by_name("Nick").send_keys("hello")
        driver.find_element_by_name("Sex").click()
        driver.find_element_by_name("Age").clear()
        driver.find_element_by_name("Age").send_keys("28")

        Select(driver.find_element_by_name('Country')).select_by_index(3)

        if debug:
            end = 10
        else:
            end = 61

        for i in range(1, end):  # answers 1st page
            if answers[i - 1] == 0:
                continue
            name = "Q%s" % i
            answer_in_range = answers[i - 1] - 1
            buttons = driver.find_elements_by_name("Q%s" % i)
            buttons[answer_in_range].click()
            """
            xpath = "(//input[@name='Q%s'])[%d]" % (i, answers[i - 1])
            print(xpath)
            driver.find_element_by_xpath(xpath).click()
            """
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

        for i in range(61, 121):  # answer 2nd page
            if answers[i - 1] == 0:
                continue
            name = "Q%s" % i
            answer_in_range = answers[i - 1] - 1
            buttons = driver.find_elements_by_name("Q%s" % i)
            buttons[answer_in_range].click()
            """
            xpath = "(//input[@name='Q%s'])[%d]" % (i, answers[i - 1])
            print(xpath)
            driver.find_element_by_xpath(xpath).click()
            """
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def tearDown(self):
        # Extract results data
        driver = self.driver
        page_source = driver.page_source
        d = pq(page_source)
        for table in d("table"):
            trs = list(pq(table)("tr"))
            trs = trs[1:]  # skip over table header ("DOMAIN/Facet")
            for tr in trs:
                ds = pq(tr)
                tds = list(ds("td"))
                label, score = tds[0:2]
                score = score.text
                label = label.text.lstrip("..")
                m[label] = score
        print(m)

        debug = True
        if debug:
            from IPython import embed
            embed()
        if debug:
            time.sleep(3600)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

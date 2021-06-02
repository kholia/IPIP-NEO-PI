#!/usr/bin/env python3

import time
import unittest
import collections

from common import answers

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from pyquery import PyQuery as pq


def test_local_python_site():
    """
    Test local site
    """
    items = []
    driver = webdriver.Firefox()
    base_url = "http://localhost:8888/"
    driver.get(base_url)
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    page_source = driver.page_source
    d = pq(page_source)  # use pyquery to extract the table values
    main_table = d("table[id='main']")
    trs = list(pq(main_table)("tr"))
    for tr in trs:
        ds = pq(tr)
        tds = list(ds("td"))
        tds = tds[1:]  # skip index number
        for td in tds:
            text = (" ").join(td.text_content().replace("\n", " ").split())  # cleanup terrible html text and canonicalize it!
            radio_button = pq(td)("input")
            val = radio_button.val()
            items.append([text, val])  # store the question, answers, and their corresponding numeric values

    driver.quit()

    return items


def test_local_perl_site():
    """
    Test upstream site
    """

    items = []
    driver = webdriver.Firefox()
    # base_url = "http://www.personal.psu.edu/~j5j/IPIP/ipipneo120.htm"
    base_url = "http://localhost/ipipneo120.htm"
    driver.get(base_url)
    driver.find_element_by_name("Risk").click()
    driver.find_element_by_name("Accuracy").click()
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    driver.find_element_by_name("Nick").clear()
    driver.find_element_by_name("Nick").send_keys("hello")
    driver.find_element_by_name("Sex").click()
    driver.find_element_by_name("Age").clear()
    driver.find_element_by_name("Age").send_keys("28")
    Select(driver.find_element_by_name('Country')).select_by_index(3)
    page_source = driver.page_source
    d = pq(page_source)
    tables = d("table")
    main_table = tables[1]  # hacky
    trs = list(pq(main_table)("tr"))
    for tr in trs:
        ds = pq(tr)
        tds = list(ds("td"))
        tds = tds[1:]  # skip index number
        for td in tds:
            text = (" ").join(td.text_content().replace("\n", " ").split())
            radio_button = pq(td)("input")
            val = radio_button.val()
            items.append([text, val])
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()  # go to next 60 questions
    time.sleep(3)
    page_source = driver.page_source  # ATTENTION!
    d = pq(page_source)
    tables = d("table")
    main_table = tables[0]  # hacky
    trs = list(pq(main_table)("tr"))
    for tr in trs:
        ds = pq(tr)
        tds = list(ds("td"))
        tds = tds[1:]  # skip index number
        for td in tds:
            text = (" ").join(td.text_content().replace("\n", " ").split())
            radio_button = pq(td)("input")
            val = radio_button.val()
            items.append([text, val])

    driver.quit()

    return items


def test_upstream_site():
    """
    Test upstream site
    """

    items = []
    driver = webdriver.Firefox()
    base_url = "http://www.personal.psu.edu/~j5j/IPIP/ipipneo120.htm"
    driver.get(base_url)
    driver.find_element_by_name("Risk").click()
    driver.find_element_by_name("Accuracy").click()
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    driver.find_element_by_name("Nick").clear()
    driver.find_element_by_name("Nick").send_keys("hello")
    driver.find_element_by_name("Sex").click()
    driver.find_element_by_name("Age").clear()
    driver.find_element_by_name("Age").send_keys("28")
    Select(driver.find_element_by_name('Country')).select_by_index(3)
    page_source = driver.page_source
    d = pq(page_source)
    tables = d("table")
    main_table = tables[1]  # hacky
    trs = list(pq(main_table)("tr"))
    for tr in trs:
        ds = pq(tr)
        tds = list(ds("td"))
        tds = tds[1:]  # skip index number
        for td in tds:
            text = (" ").join(td.text_content().replace("\n", " ").split())
            radio_button = pq(td)("input")
            val = radio_button.val()
            items.append([text, val])
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()  # go to next 60 questions
    time.sleep(3)
    page_source = driver.page_source  # ATTENTION!
    d = pq(page_source)
    tables = d("table")
    main_table = tables[0]  # hacky
    trs = list(pq(main_table)("tr"))
    for tr in trs:
        ds = pq(tr)
        tds = list(ds("td"))
        tds = tds[1:]  # skip index number
        for td in tds:
            text = (" ").join(td.text_content().replace("\n", " ").split())
            radio_button = pq(td)("input")
            val = radio_button.val()
            items.append([text, val])

    driver.quit()

    return items

    """
    debug = True
    if debug:
        from IPython import embed
        embed()
    if debug:
        time.sleep(3600)
    driver.quit()
    """


if __name__ == "__main__":
    perl_items = test_local_perl_site()

    python_items = test_local_python_site()

    # print(perl_items)
    # print(python_items)

    for index, item in enumerate(perl_items):  # compare the question, answers, and their corresponding numeric values
        if item != python_items[index]:
            print(index, item, python_items[index])
        else:
            # print("[+] Item <%s> is OK!" % item)
            pass

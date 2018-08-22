# -*- coding: utf-8 -*-
import unittest

import pytest
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group

def is_alert_present(driver):
    try:
        driver.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)

    def open_homepage(self, driver):
        driver.get("http://localhost/addressbook/")

    def test_add_group(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="kot", header="kot", footer="kot"))
        self.return_to_groups(driver)
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="", header="", footer=""))
        self.return_to_groups(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text(u"Выйти").click()

    def return_to_groups(self, driver):
        driver.find_element_by_link_text("group page").click()

    def create_group(self, driver, group):
        # Init group creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()

    def open_groups_page(self, driver):
        driver.find_element_by_link_text(u"Группы").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Пароль:'])[1]/following::input[2]").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()

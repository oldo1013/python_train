from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import session_helper
from fixture.group import group_helper


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)
        self.session = session_helper(self)
        self.group = group_helper(self)

    def open_homepage(self):
            driver = self.driver
            driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()

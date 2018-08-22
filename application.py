from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)

    def open_homepage(self):
            driver = self.driver
            driver.get("http://localhost/addressbook/")

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text(u"Выйти").click()

    def return_to_groups(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
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
        self.return_to_groups()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text(u"Группы").click()

    def login(self, username, password):
        driver = self.driver
        self.open_homepage()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Пароль:'])[1]/following::input[2]").click()

    def destroy(self):
        self.driver.quit()

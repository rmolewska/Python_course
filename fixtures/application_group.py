from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.session import SessionHelper


class ApplicationGroup:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("grupy").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_group_page()

    def return_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def destroy(self):
        self.wd.quit()
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(first_name="Adam", middle_name="Jan", last_name="Kowalski", nickname="dsksljd",
                                company_title="dfdsbf", company_name="dfdsf", company_address="dfdsfds",
                                home_phone="3232132131", mobile_phone="12313213232", work_phone="2132132133",
                                fax="213123213213", email="hshs@qwe.com", email_2="ewqe@qwe.com",
                                email_3="dqweweq@qwe.com", homepage="www.ff.com",
                                birth_day="//div[@id='content']/form/select[1]//option[31]",
                                birth_month="//div[@id='content']/form/select[2]//option[12]", birth_year="1987",
                                ann_day="//div[@id='content']/form/select[3]//option[31]",
                                ann_month="//div[@id='content']/form/select[4]//option[11]", ann_year="1996",
                                address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfdgfdgd"))
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(first_name="", middle_name="", last_name="", nickname="",
                                company_title="", company_name="", company_address="",
                                home_phone="", mobile_phone="", work_phone="",
                                fax="", email="", email_2="",
                                email_3="", homepage="",
                                birth_day="//div[@id='content']/form/select[1]//option[1]",
                                birth_month="//div[@id='content']/form/select[2]//option[1]", birth_year="",
                                ann_day="//div[@id='content']/form/select[3]//option[1]",
                                ann_month="//div[@id='content']/form/select[4]//option[1]", ann_year="",
                                address_2="", phone_2="", notes=""))
        self.return_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Wyloguj się").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_new_contact(self, wd, contact):
        # init contact creation
        wd.find_element_by_link_text("nowy wpis").click()
        # fill name info
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # fill company info
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.company_title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.company_address)
        # fill  contact (phone, mail, website) info
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # fill birthday date info
        if not wd.find_element_by_xpath(contact.birth_day).is_selected():
            wd.find_element_by_xpath(contact.birth_day).click()
        if not wd.find_element_by_xpath(contact.birth_month).is_selected():
            wd.find_element_by_xpath(contact.birth_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        # fill anniversary date info
        if not wd.find_element_by_xpath(contact.ann_day).is_selected():
            wd.find_element_by_xpath(contact.ann_day).click()
        if not wd.find_element_by_xpath(contact.ann_month).is_selected():
            wd.find_element_by_xpath(contact.ann_month).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ann_year)
        # fill second address info
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_main_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

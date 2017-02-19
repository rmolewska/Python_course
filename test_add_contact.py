# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application_contact import ApplicationContact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = ApplicationContact()


    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_new_contact(Contact(first_name="Adam", middle_name="Jan", last_name="Kowalski", nickname="dsksljd",
                                company_title="dfdsbf", company_name="dfdsf", company_address="dfdsfds",
                                home_phone="3232132131", mobile_phone="12313213232", work_phone="2132132133",
                                fax="213123213213", email="hshs@qwe.com", email_2="ewqe@qwe.com",
                                email_3="dqweweq@qwe.com", homepage="www.ff.com",
                                birth_day="//div[@id='content']/form/select[1]//option[31]",
                                birth_month="//div[@id='content']/form/select[2]//option[12]", birth_year="1987",
                                ann_day="//div[@id='content']/form/select[3]//option[31]",
                                ann_month="//div[@id='content']/form/select[4]//option[11]", ann_year="1996",
                                address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfdgfdgd"))
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_new_contact(Contact(first_name="", middle_name="", last_name="", nickname="",
                                company_title="", company_name="", company_address="",
                                home_phone="", mobile_phone="", work_phone="",
                                fax="", email="", email_2="",
                                email_3="", homepage="",
                                birth_day="//div[@id='content']/form/select[1]//option[1]",
                                birth_month="//div[@id='content']/form/select[2]//option[1]", birth_year="",
                                ann_day="//div[@id='content']/form/select[3]//option[1]",
                                ann_month="//div[@id='content']/form/select[4]//option[1]", ann_year="",
                                address_2="", phone_2="", notes=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("strona główna").click()

    def create_new(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("nowy wpis").click()
        self.fill_contact_form(contact)
        # submit new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill name info
        self.change_contact_field_value("firstname", contact.first_name)
        self.change_contact_field_value("middlename", contact.middle_name)
        self.change_contact_field_value("lastname", contact.last_name)
        self.change_contact_field_value("nickname", contact.nickname)
        # fill company info
        self.change_contact_field_value("title", contact.company_title)
        self.change_contact_field_value("company", contact.company_name)
        self.change_contact_field_value("address", contact.company_address)
        # fill  contact (phone, mail, website) info
        self.change_contact_field_value("home", contact.home_phone)
        self.change_contact_field_value("mobile", contact.mobile_phone)
        self.change_contact_field_value("work", contact.work_phone)
        self.change_contact_field_value("fax", contact.fax)
        self.change_contact_field_value("email", contact.email)
        self.change_contact_field_value("email2", contact.email_2)
        self.change_contact_field_value("email3", contact.email_3)
        self.change_contact_field_value("homepage", contact.homepage)
        # fill birthday date info
        self.change_contact_field_value("byear", contact.birth_year)
        # fill anniversary date info
        self.change_contact_field_value("ayear", contact.ann_year)
        # fill second address info
        self.change_contact_field_value("address2", contact.address_2)
        self.change_contact_field_value("phone2", contact.phone_2)
        self.change_contact_field_value("notes", contact.notes)

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # delete first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm pop-up
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
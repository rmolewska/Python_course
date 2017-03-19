
from models.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
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
        self.contact_cache = None

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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # delete some contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm pop-up
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def modify_first_contact(self):
        self.open_contact_to_edit_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # open modification form
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id))
        return list(self.contact_cache)



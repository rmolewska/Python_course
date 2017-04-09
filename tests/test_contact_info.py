import re
from models.contact import Contact


def test_contact_info_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for c in range(len(contact_from_db)):
        assert contact_from_home_page[c].id == contact_from_db[c].id
        assert contact_from_home_page[c].first_name == clear_spaces(contact_from_db[c].first_name).strip()
        assert contact_from_home_page[c].last_name == clear_spaces(contact_from_db[c].last_name).strip()
        assert contact_from_home_page[c].address == clear_spaces(contact_from_db[c].address).strip()
      

def clear(s):
    return re.sub("[\s|\-[]+/]", '', s)


def clear_spaces(s2):
    return re.sub("\s+", ' ', s2)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone_2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email, contact.email_2, contact.email_3]))))




# def test_contact_info_on_home_page(app):
    # contact_from_home_page = app.contact.get_contact_list()[0]
    # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # assert clear(contact_from_home_page.first_name) == clear(contact_from_edit_page.first_name)
    # assert clear(contact_from_home_page.last_name) == clear(contact_from_edit_page.last_name)
    # assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    # assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


# def test_phones_on_contact_view_page(app):
    # contact_from_view_page = app.contact.get_contact_from_view_page(0)
    # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    # assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    # assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    # assert contact_from_view_page.phone_2 == contact_from_edit_page.phone_2
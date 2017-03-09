# -*- coding: utf-8 -*-

from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(Contact(first_name="Adam", middle_name="Jan", last_name="Kowalski", nickname="dsksljd",
                                   company_title="dfdsbf", company_name="dfdsf", company_address="dfdsfds",
                                   home_phone="3232132131", mobile_phone="12313213232", work_phone="2132132133",
                                   fax="213123213213", email="hshs@qwe.com", email_2="ewqe@qwe.com",
                                   email_3="dqweweq@qwe.com", homepage="www.ff.com", birth_year="1986",
                                   ann_year="1996", address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfdgd"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(Contact(first_name="", middle_name="", last_name="", nickname="", company_title="",
                                   company_name="", company_address="", home_phone="", mobile_phone="", work_phone="",
                                   fax="", email="", email_2="", email_3="", homepage="",  birth_year="", ann_year="",
                                   address_2="", phone_2="", notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)



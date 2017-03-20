
from models.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(first_name="Test", middle_name="Test2", last_name="Testowy", nickname="dsksljd",
                                       company_title="dfdsbf", company_name="dfdsf", company_address="dfdsfds",
                                       home_phone="3232132131", mobile_phone="12313213232", work_phone="2132132133",
                                       fax="213123213213", email="hshs@qwe.com", email_2="ewqe@qwe.com",
                                       email_3="dqweweq@qwe.com", homepage="www.ff.com", birth_year="1986",
                                       ann_year="1996", address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfdgd"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
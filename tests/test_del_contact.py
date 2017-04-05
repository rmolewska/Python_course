
from models.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(first_name="Test", middle_name="Test2", last_name="Testowy", nickname="dsksljd",
                                       company_title="dfdsbf", company_name="dfdsf", address="dfdsfds",
                                       home_phone="3232132131", mobile_phone="12313213232", work_phone="2132132133",
                                       fax="213123213213", email="hshs@qwe.com", email_2="ewqe@qwe.com",
                                       email_3="dqweweq@qwe.com", homepage="www.ff.com", birth_year="1986",
                                       ann_year="1996", address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfdgd"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    # index = randrange(len(old_contacts))
    # app.contact.delete_contact_by_index(index)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(last_name="".join(contact.last_name.strip().split()),
                           first_name="".join(contact.first_name.strip().split()),
                           address=contact.address, email=contact.email, id=contact.id)
        assert sorted(map(clean, app.contact.get_contact_list()), key=Contact.id_or_max) == \
               sorted(map(clean, new_contacts), key=Contact.id_or_max)
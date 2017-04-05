# -*- coding: utf-8 -*-

from models.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(last_name="".join(contact.last_name.strip().split()),
                           first_name="".join(contact.first_name.strip().split()),
                           address=contact.address, email=contact.email, id=contact.id)
        assert sorted(map(clean, app.contact.get_contact_list()), key=Contact.id_or_max) == \
               sorted(map(clean, new_contacts), key=Contact.id_or_max)


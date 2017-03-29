# -*- coding: utf-8 -*-

from models.contact import Contact
import pytest
from data.add_contact import test_contactdata


@pytest.mark.parametrize("contact", test_contactdata, ids=[repr(x) for x in test_contactdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



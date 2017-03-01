
from models.contact import Contact


def test_modify_contact_first_name(app):
    app.contact.modify_first_contact(Contact(first_name="New first name"))


def test_modify_contact_middle_name(app):
    app.contact.modify_first_contact(Contact(middle_name="New middle name"))

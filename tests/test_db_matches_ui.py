
from models.group import Group
from models.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name="".join(group.name.strip().split()))

    db_list = map(clean, db.get_group_list())
    ui_list = map(clean, ui_list)

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


#  s from the lecture which doesn't work.

#  def test_group_list(app, db):
#   ui_list = app.group.get_group_list()
#   def clean(group):
#       return Group(id=group.id, name=group.name.strip())
#   db_list = map(clean, db.get_group_list())
#
#   assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_contact_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(last_name="".join(contact.last_name.strip().split()), first_name="".join(contact.first_name.strip().split()),
                       address=contact.address, email=contact.email, id=contact.id)

    db_contact_list = map(clean, db.get_contact_list())
    ui_contact_list = map(clean, ui_contact_list)

    assert sorted(ui_contact_list, key=Contact.id_or_max) == sorted(db_contact_list, key=Contact.id_or_max)
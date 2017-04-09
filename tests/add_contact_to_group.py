from models.contact import Contact
from models.group import Group

import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(first_name="Test", middle_name="Test2", last_name="Testowy", nickname="dsksljd",
                                   company_title="dfdsbf", company_name="dfdsf", address="dfdsfds",
                                   home_phone="3232132131", mobile_phone="12313213232", work_phone="2132132133",
                                   fax="213123213213", email="hshs@qwe.com", email_2="ewqe@qwe.com",
                                   email_3="dqweweq@qwe.com", homepage="www.ff.com", birth_year="1986",
                                   ann_year="1996", address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfdgd"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new_name", header="new_header", footer="new_footer"))
    old_contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(groups)
    app.contact.add_contact_to_group(contact.id, group.id)

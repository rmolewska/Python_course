
from models.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(first_name="Test", middle_name="Test2", last_name="Testowy", nickname="dsksljd",
                                       company_title="dfdsbf", company_name="dfdsf", company_address="dfdsfds",
                                       home_phone="3232132131", mobile_phone="12313213232", work_phone="2132132133",
                                       fax="213123213213", email="hshs@qwe.com", email_2="ewqe@qwe.com",
                                       email_3="dqweweq@qwe.com", homepage="www.ff.com", birth_year="1986",
                                       ann_year="1996", address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfdgd"))
    app.contact.delete_first_contact()

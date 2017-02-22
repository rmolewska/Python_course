

from models.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="Tomasz", middle_name="Gregorz", last_name="Krawczyk",
                                           nickname="sjdkfkdl", company_title="dfdsbf", company_name="dfdsf",
                                           company_address="dfdsfds", home_phone="3232132131",
                                           mobile_phone="12313213232", work_phone="2132132133", fax="213123213213",
                                           email="hshs@qwe.com", email_2="ewqe@qwe.com", email_3="dqweweq@qwe.com",
                                           homepage="www.ff.com",
                                           birth_day="//div[@id='content']/form/select[1]//option[30]",
                                           birth_month="//div[@id='content']/form/select[2]//option[12]",
                                           birth_year="1987", ann_day="//div[@id='content']/form/select[3]//option[31]",
                                           ann_month="//div[@id='content']/form/select[4]//option[11]", ann_year="1996",
                                           address_2="fgrfgfg", phone_2="453543543543", notes="fgdgfgd"))
    app.session.logout()
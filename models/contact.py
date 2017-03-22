from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, company_title=None,
                 company_name=None, address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 email=None, email_2=None, email_3=None, homepage=None, birth_year=None, ann_year=None, address_2=None,
                 phone_2=None, all_phones_from_home_page=None, all_emails_from_home_page=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.company_title = company_title
        self.company_name = company_name
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birth_year = birth_year
        self.ann_year = ann_year
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.home_phone,
                                                        self.mobile_phone, self.work_phone,
                                                        self.all_phones_from_home_page,
                                                        self.address, self.all_emails_from_home_page, self.email,
                                                        self.email_2, self.email_3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name \
               and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
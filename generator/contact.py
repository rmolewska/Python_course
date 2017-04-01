
from models.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    numbers = string.digits + " "
    return "".join([random.choice(numbers) for i in range(maxlen)])


def random_mail(prefix, maxlen, domain):
    mail = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(mail) for x in range(random.randrange(maxlen))]) + domain

test_data = [
        Contact(first_name="", middle_name="", last_name="", nickname="", company_title="",
                company_name="", address="", home_phone="", mobile_phone="", work_phone="",
                fax="", email="", email_2="", email_3="", homepage="", birth_year="", ann_year="",
                address_2="", phone_2="", notes="")] + [
        Contact(first_name=random_string("firstname", 10), middle_name=random_string("middlename", 20),
                last_name=random_string("lastname", 20), nickname=random_string("nickname", 8),
                company_title=random_string("title", 20), company_name=random_string("company", 20),
                address=random_string("address", 20),
                home_phone=random_numbers(10), mobile_phone=random_numbers(10), work_phone=random_numbers(10),
                fax=random_numbers(10), email=random_mail("email", 7, "@gmail.com"),
                email_2=random_mail("email2", 7, "@gmail.com"), email_3=random_mail("email3", 7, "@gmail.com"),
                homepage=random_string("page", 10), birth_year=random_numbers(4), ann_year=random_numbers(4),
                address_2=random_string("address2", 20), phone_2=random_numbers(10), notes=random_string("notes", 10))
        for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# with open(file, "w") as out:
#    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

with open(file, "w", encoding='utf8') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
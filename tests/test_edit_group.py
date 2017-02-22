
from models.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="yyyy", header="ppppppp", footer="kkkkkkk"))
    app.session.logout()


from models.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="dssdgsg", footer="sdgsdgsG"))
    app.group.delete_first_group()

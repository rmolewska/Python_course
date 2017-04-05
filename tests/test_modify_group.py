
from models.group import Group
import random


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new_name", header="new_header", footer="new_footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "changed_name"
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name="".join(group.name.strip().split()))
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(map(clean, app.group.get_group_list()),
                                                                             key=Group.id_or_max)

# def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test", header="dssdgsg", footer="sdgsdgsG"))
#  old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
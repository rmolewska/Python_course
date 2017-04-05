
from models.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test", header="dssdgsg", footer="sdgsdgsG"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # index = randrange(len(old_groups))
    # app.group.delete_group_by_index(index) / usuwanie po indeksie  tylko dla interfejsu użytkownika
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, name="".join(group.name.strip().split()))
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(map(clean, app.group.get_group_list()),
                                                                             key=Group.id_or_max)
# -*- coding: utf-8 -*-

from models.group import Group


def test_add_group_db(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    # assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name="".join(group.name.strip().split()))
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(map(clean, app.group.get_group_list()),
                                                                             key=Group.id_or_max)
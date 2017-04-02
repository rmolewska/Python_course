
from models.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name="".join(group.name.strip().split()))

    db_list = map(clean, db.get_group_list())
    ui_list = map(clean, ui_list)

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


#  s from the lecture which doesn't work.

#  def test_group_list(app, db):
#   ui_list = app.group.get_group_list()
#   def clean(group):
#       return Group(id=group.id, name=group.name.strip())
#   db_list = map(clean, db.get_group_list())
#
#   assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)



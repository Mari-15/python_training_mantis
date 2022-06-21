from model.project import Project
import string
import random


def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_del_project(app):
    app.session.open_project_page()
    old_projects = app.soap.list_project_for_user(username='administrator', password='root')
    if len(old_projects) == 0:
        app.project.create(Project(name=random_projectname('name_', 10)))
    project = random.choice(old_projects)
    app.project.delete(project)
    new_projects = app.soap.list_project_for_user(username='administrator', password='root')
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects) == sorted(new_projects)

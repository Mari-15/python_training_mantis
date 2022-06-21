from model.project import Project
import string
import random


def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    app.session.open_project_page()
    old_projects = app.soap.list_project_for_user(username='administrator', password='root')
    project = Project(name=random_projectname('name_', 10), description='test1test1')
    if project.name in old_projects:
        project = Project(name=random_projectname('name_', 10), description='test1test1')
    app.project.create(project)
    new_projects = app.soap.list_project_for_user(username='administrator', password='root')
    old_projects.append(project.name)
    assert sorted(old_projects) == sorted(new_projects)


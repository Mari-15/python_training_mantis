from model.project import Project
import random


def test_del_project(app):
    app.session.login('administrator', 'root')
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name='Rickit'))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)

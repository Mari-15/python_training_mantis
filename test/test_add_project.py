from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name='Test042244', description='test1test1')
    if project in old_projects:
        project = Project(name='Rit', description='test1test1')
    app.project.create(project)
    old_projects.append(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)



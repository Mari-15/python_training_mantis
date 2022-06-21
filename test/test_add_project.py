from model.project import Project


def test_add_project(app):
    app.session.open_project_page()
    old_projects = app.soap.list_project_for_user(username='administrator', password='root')
    project = Project(name='Tt044', description='test1test1')
    app.project.create(project)
    new_projects = app.soap.list_project_for_user(username='administrator', password='root')


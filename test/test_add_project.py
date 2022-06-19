from model.project import Project


def test_add_project(app):
    app.session.open_home_page()
    app.session.login('administrator', 'root')
    app.session.open_project_page()
    old_projects = app.project.get_project_list()
    app.project.create(Project(name='Test115', description='test1test1'))
    new_projects = app.project.get_project_list()
    assert len(old_projects) == len(new_projects)



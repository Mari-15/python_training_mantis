from model.project import Project


def test_add_project(app):
    app.session.open_home_page()
    app.session.login('administrator', 'root')
    app.project.create(Project(name='Test1', status='stable', view_status='private', description='test1test1'))



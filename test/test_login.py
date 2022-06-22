def test_login(app, config):
    app.session.login(config['webadmin']['username'], config['webadmin']['password'])
    assert app.session.is_logged_in_as(config['webadmin']['username'])
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + '/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def list_project_for_user(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        client = Client(self.app.base_url + '/api/soap/mantisconnect.php?wsdl')
        try:
            project_list = client.service.mc_projects_get_user_accessible(username, password)
            project_list = list(map(lambda x: x.name, project_list))
            return project_list
        except WebFault:
            return False


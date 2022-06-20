from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.project import Project
import re


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, project):
        wd = self.app.wd
        self.change_field_value('name', project.name)
        #status only: development, release, stable, obsolete
        self.change_selector_value('status', project.status)
        #only: public, private
        self.change_selector_value('view_state', project.view_status)
        self.change_field_value('description', project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def change_selector_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            Select(wd.find_element(by=By.NAME, value=field_name)).select_by_visible_text(text)

    def create(self, project):
        wd = self.app.wd
        wd.find_element(by=By.XPATH, value='/html/body/table[3]/tbody/tr[1]/td/form/input[2]').click()
        #fill form
        self.fill_form(project)
        #off inherit global categories
        wd.find_element(by=By.NAME, value='inherit_global').click()
        #submit creation
        wd.find_element(by=By.XPATH, value='/html/body/div[3]/form/table/tbody/tr[7]/td/input').click()

    project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.app.session.open_project_page()
        self.project_cache = []
        for element in wd.find_elements(By.CLASS_NAME, 'row-1'):
            if element.find_element(by=By.CSS_SELECTOR, value='td:nth-child(1)').text != 'General':
                name = element.find_element(by=By.CSS_SELECTOR, value='td:nth-child(1)').text
                self.project_cache.append(Project(name=name))
        for element in wd.find_elements(By.CLASS_NAME, 'row-2'):
            if element.find_element(by=By.CSS_SELECTOR, value='td:nth-child(1)').text != 'General':
                name = element.find_element(by=By.CSS_SELECTOR, value='td:nth-child(1)').text
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)

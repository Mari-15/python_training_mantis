from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element(by=By.NAME, value="username").click()
        wd.find_element(by=By.NAME, value="username").clear()
        wd.find_element(by=By.NAME, value="username").send_keys(username)
        wd.find_element(by=By.NAME, value="password").clear()
        wd.find_element(by=By.NAME, value="password").send_keys(password)
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(by=By.CSS_SELECTOR, value="td.login-info-left span").text

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)




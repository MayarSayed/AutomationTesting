from Locators.locators import Locators

class LoginPage():
    textbox_username_Name = Locators.login_textbox_username_Name
    textbox_password_Name = Locators.login_textbox_password_Name
    button_login_xpath    = Locators.button_login_xpath
    link_logout_linktext  = Locators.logout_url_xpath
    
    def __init__(self,driver):
        self.driver= driver
        
    def setUserName(self,username):
        self.driver.find_element_by_name(self.textbox_username_Name).send_keys(username)
    
    def setPassword(self,password):
        self.driver.find_element_by_name(self.textbox_password_Name).send_keys(password)
    
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    
    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()
        
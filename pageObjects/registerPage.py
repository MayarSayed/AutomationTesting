from Locators.locators import Locators

class RegisterPage():
    textbox_firstname_Name = Locators.textbox_firstname_Name
    textbox_lastname_Name = Locators.textbox_lastname_Name
    textbox_mobileNum_Name = Locators.textbox_mobileNum_Name
    textbox_email_Name= Locators.textbox_email_Name
    textbox_password_Name= Locators.textbox_password_Name
    textbox_confirmpassword_Name= Locators.textbox_confirmpassword_Name
    button_signUp_xpath = Locators.button_signUp_xpath
    
    def __init__(self,driver):
        self.driver= driver
        
    def setFirstName(self,firstname):
        self.driver.find_element_by_name(self.textbox_firstname_Name).send_keys(firstname)
    
    def setLastName(self,lastname):
        self.driver.find_element_by_name(self.textbox_lastname_Name).send_keys(lastname)
    
    def setMobileNumber(self,mobileNum):
        self.driver.find_element_by_name(self.textbox_mobileNum_Name).send_keys(mobileNum)
    
    def setEmail(self,username):
        self.driver.find_element_by_name(self.textbox_email_Name).send_keys(username)
    
    def setPassword(self,password):
        self.driver.find_element_by_name(self.textbox_password_Name).send_keys(password)
    
    def setConfirmPassword(self,password):
        self.driver.find_element_by_name(self.textbox_confirmpassword_Name).send_keys(password)
    
    def clickSignUp(self):
        self.driver.find_element_by_xpath(self.button_signUp_xpath).click()
    
    
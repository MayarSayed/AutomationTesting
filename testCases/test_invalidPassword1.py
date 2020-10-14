import allure
from allure_commons.types import AttachmentType

from pageObjects.registerPage import RegisterPage
from Utilities.readProperties import ReadConfig
import pytest
from  selenium import webdriver
import time
from Requirements.requirements import Requirement

#Testing with invalid password that doesn't contain capital letter "Should get an error message and prevent registraion"
class Test_Invalid_Password:
    firstname = Requirement.getValidFistName()
    lastname  = Requirement.getValidLastName()
    mobileNum = Requirement.getValidMobileNumber()
    email     = Requirement.getValidEmail()
    password  = Requirement.getInValidPasswordValue()

    def testSignUp(self,setUp):
        self.driver = setUp
        self.driver.get(ReadConfig.getRegisterPageURL())
        regPage = RegisterPage(self.driver)

        regPage.setFirstName(self.firstname)
        regPage.setLastName(self.lastname)
        regPage.setMobileNumber(self.mobileNum)
        regPage.setEmail(self.email)
        regPage.setPassword(self.password)
        regPage.setConfirmPassword(self.password)
        befSignUpValues = self.driver.get_screenshot_as_png()
        regPage.clickSignUp()

        time.sleep(5)
        currentUrl = self.driver.current_url

        if currentUrl == ReadConfig.getRegisterPageURL():
            self.driver.close()
            assert True
        else:
            allure.attach(befSignUpValues,
                          name="SignUp With Invalid Email",
                          attachment_type=AttachmentType.PNG)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Login With Invalid Password",
                          attachment_type=AttachmentType.PNG)

            self.driver.close()
            assert False




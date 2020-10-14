from pageObjects.registerPage import RegisterPage
from Utilities.readProperties import ReadConfig
from Requirements.requirements import Requirement
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import time

#Testing with invalid Email "Should get an error message and prevent registraion"
class Test_Invalid_Email:
    firstname = Requirement.getValidFistName()
    lastname  = Requirement.getValidLastName()
    mobileNum = Requirement.getValidMobileNumber()
    email     = Requirement.getInValidEmail()
    password  = Requirement.getValidPassword()


    def testURL(self):
        self.driver = webdriver.Firefox(executable_path="Drivers\\geckodriver.exe")
        self.driver.get(ReadConfig.getRegisterPageURL())
        currentUrl = self.driver.current_url
        self.driver.close()
        if currentUrl == ReadConfig.getRegisterPageURL():
            assert True
        else:
            assert False

    def testSignUp(self):
        self.driver = webdriver.Firefox(executable_path="Drivers\\geckodriver.exe")
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
                          name="Login With Invalid Email",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False




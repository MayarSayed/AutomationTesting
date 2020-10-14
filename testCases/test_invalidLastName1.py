import allure
from allure_commons.types import AttachmentType
from Utilities.readProperties import ReadConfig

from pageObjects.registerPage import RegisterPage
import pytest
from  selenium import webdriver
import time
from Requirements.requirements import Requirement

#Testing with invalid Last Name that start with lowercase letter "Should get an error message and prevent registraion"
class Test_Invalid_Lastname:
    firstname = Requirement.getValidFistName()
    lastname = Requirement.getInValidLastName()
    mobileNum = Requirement.getValidMobileNumber()
    email     = Requirement.getValidEmail()
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
        befSignUp = self.driver.get_screenshot_as_png()
        regPage.clickSignUp()

        time.sleep(5)
        currentUrl = self.driver.current_url
        if currentUrl == ReadConfig.getRegisterPageURL():
            self.driver.close()
            assert True
        else:
            allure.attach(befSignUp,
                          name="SignUp With Invalid LastName",
                          attachment_type=AttachmentType.PNG)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Login With Invalid LastName",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

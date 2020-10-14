from allure_commons.types import AttachmentType
from pageObjects.registerPage import RegisterPage
from Utilities.readProperties import ReadConfig

import pytest
import allure
from selenium import webdriver
import time
from Requirements.requirements import Requirement

#Testing with invalid Mobile Number "Should get an error message and prevent registraion"
#@allure.severity(allure.severity_level.NORMAL)
class Test_Invalid_MobileNum:
    firstname = Requirement.getValidFistName()
    lastname = Requirement.getValidLastName()
    mobileNum = Requirement.getInValidMobileNumber()
    email     = Requirement.getValidEmail()
    password  = Requirement.getValidPassword()

    
    def testURL(self,setUp):
        self.driver = setUp
        self.driver.get(ReadConfig.getRegisterPageURL())
        currentUrl = self.driver.current_url
        self.driver.close()
        if currentUrl == ReadConfig.getRegisterPageURL():
            assert True
        else:
            assert False

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
        befSignUp = self.driver.get_screenshot_as_png()
        regPage.clickSignUp()

        time.sleep(5)
        currentUrl = self.driver.current_url
        screenshot = self.driver.get_screenshot_as_png()
        
        if currentUrl == ReadConfig.getRegisterPageURL():
            assert True
        else:
            allure.attach(befSignUp,
                          name="Sign Up with Invalid Mobile Num",
                          attachment_type=AttachmentType.PNG)
            allure.attach(screenshot,
                          name="Login with Invalid Mobile Num",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False



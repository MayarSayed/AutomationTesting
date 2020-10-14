from pageObjects.registerPage import RegisterPage
from pageObjects.loginPage import LoginPage

import allure
from allure_commons.types import AttachmentType
from Utilities.readProperties import ReadConfig
import pytest
from selenium import webdriver
import time
from Requirements.requirements import Requirement
class Test_Valid_Registration:
    firstname = Requirement.getValidFistName()
    lastname  = Requirement.getValidLastName()
    mobileNum = Requirement.getValidMobileNumber()
    email     = Requirement.getValidEmail()
    password  = Requirement.getValidPassword()

    def testSignUp(self):
        self.driver = webdriver.Firefox(executable_path="Drivers\\geckodriver.exe")
        self.driver.get(ReadConfig.getRegisterPageURL())
        Rp = RegisterPage(self.driver)

        Rp.setFirstName(self.firstname)
        Rp.setLastName(self.lastname)
        Rp.setMobileNumber(self.mobileNum)
        Rp.setEmail(self.email)
        Rp.setPassword(self.password)
        Rp.setConfirmPassword(self.password)
        Rp.clickSignUp()

        time.sleep(5)
        currentUrl = self.driver.current_url
        self.driver.close()
        if currentUrl == ReadConfig.getHomePageURL():
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Failed Registration With Valid Inputs",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    def testLogin(self):
        self.driver = webdriver.Firefox(executable_path="Drivers\\geckodriver.exe")
        self.driver.get(ReadConfig.getLoginPageURL())
        loginp = LoginPage(self.driver)
        loginp.setUserName(self.email)
        loginp.setPassword(self.password)
        loginp.clickLogin()
        time.sleep(5)
        currentUrl = self.driver.current_url
        if currentUrl == ReadConfig.getHomePageURL():
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Failed Login After Registration",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

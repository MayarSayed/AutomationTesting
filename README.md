# Automation Testing Framework

## Used Language and Packages
* Python Language
* Selenium: selenium libraries for automation
* Pytest: python unit test Framework
* Allure-pytest: To generate allure reports

## Folder Structure
**AutomationTesting** <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pageObjects<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loginPage.py -> Class for a Login page <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;registerPage.py -> Class for a Register page <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Configurations <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config.ini -> containing data values so no hard coded values will be included in testcases <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Drivers<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chromedriver.exe -> exe for using Chrome driver  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;geckodriver ->exe for using Firefox driver <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Locators<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;locators.py -> Containing the pages element locators to abstract them outside the code<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;testCases<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This folder contains all testCase.py files to be performed<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reports <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This folder is used for including the report files after executing the testcases <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Utilities <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;readProperties.py -> to read common data from ini file <br />


## Test Cases

## Running test Cases

## Reporting


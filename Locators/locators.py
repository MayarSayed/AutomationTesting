class Locators():
    #registerPage Locators
    
    registerPageUrl              = 'https://phptravels.net/register'
    
    textbox_firstname_Name       = 'firstname'
    textbox_lastname_Name        = 'lastname'
    textbox_mobileNum_Name       = 'phone'
    textbox_email_Name           = 'email'
    textbox_password_Name        = 'password'
    textbox_confirmpassword_Name = 'confirmpassword'
    button_signUp_xpath          = '/html/body/div[1]/div[1]/section/div/div/div[2]/div/form/div[8]/button'

    #loginPage Locators
    
    loginPageUrl = 'https://phptravels.net/login'
    
    login_textbox_username_Name = 'username'
    login_textbox_password_Name = 'password'
    button_login_xpath          = '/html/body/div/div[1]/section/div/div[1]/div[2]/form/button'
    
    homaPageUrl                 = "https://phptravels.net/account/"
    logout_url_xpath            = '/html/body/div/header/div[1]/div/div/div[2]/div/ul/li[3]/div/div/div/a[2]'

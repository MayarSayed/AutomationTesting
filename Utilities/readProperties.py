import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getRegisterPageURL():
        url=config.get('common URls','registerPageUrl')
        return url

    @staticmethod
    def getLoginPageURL():
        url=config.get('common URls','loginPageUrl')
        return url

    @staticmethod
    def getHomePageURL():
        url=config.get('common URls','homePageUrl')
        return url

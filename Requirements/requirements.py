import random
import string
class Requirement:
    @staticmethod
    def getValidFistName():
        str= ''.join(random.choice(string.ascii_letters) for x in range(5))
        return random.choice(string.ascii_uppercase)+str

    @staticmethod
    def getInValidFistName():
        str= ''.join(random.choice(string.ascii_letters) for x in range(5))
        return random.choice(string.ascii_lowercase)+str

    @staticmethod
    def getValidLastName():
        str= ''.join(random.choice(string.ascii_letters) for x in range(5))
        return random.choice(string.ascii_uppercase)+str

    @staticmethod
    def getInValidLastName():
        str= ''.join(random.choice(string.ascii_letters) for x in range(5))
        return random.choice(string.ascii_lowercase)+str

    @staticmethod
    def getValidMobileNumber():
        num= ''.join(random.choice(string.digits) for x in range(9))
        mob = "01"+num
        return mob

    @staticmethod
    def getInValidMobileNumber():
        num= ''.join(random.choice(string.ascii_letters) for x in range(6))
        return num

    @staticmethod
    def getValidEmail():
        str= ''.join(random.choice(string.ascii_letters+string.digits) for x in range(7))
        email = str+"@gmail.com"
        return email

    @staticmethod
    def getInValidEmail():
        email= ''.join(random.choice(string.ascii_letters+string.digits) for x in range(10))
        return email

    @staticmethod
    def getValidPassword():
        str= ''.join(random.choice(string.ascii_letters+string.digits) for x in range(6))
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+str
        return password

    @staticmethod
    def getInValidPasswordLimit():
        str= ''.join(random.choice(string.ascii_letters+string.digits) for x in range(3))
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+str
        return password

    @staticmethod
    def getInValidPasswordValue():
        password= ''.join(random.choice(string.digits) for x in range(8))
        return password





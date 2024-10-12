import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/inputData.ini")


class ReadConfig():
    def getSauceDemoURL(self):
        # sauceDemoURL = config.get('URLs', 'sauceDemoURL')
        # return sauceDemoURL
        return config.get('URLs', 'sauceDemoURL')

    def getUsername(self):
        username = config.get('Login Details', 'username')
        return username

    def getPasswo2rd(self):
        password = config.get('Login Details', 'password')
        return password

    def getLastName(self):
        lastname = config.get('Billing Information', 'lastName')
        return lastname

    def getFirstName(self):
            return config.get("Billing Information", 'firstName')

    def getZipCode(self):
        return config.get("Billing Information", 'ZipCode')

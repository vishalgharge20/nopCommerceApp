import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def GetApplicationUrl():
        url = config.get('common info','baseUrl_login')
        return url

    @staticmethod
    def GetUsername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common info','password')
        return password

    @staticmethod
    def GetApplicationRegisterUrl():
        register_url = config.get('register info','baseUrl_register')
        return register_url

    @staticmethod
    def GetFirstName():
        first_name = config.get('register info','firstname')
        return first_name

    @staticmethod
    def GetLastName():
        last_name = config.get('register info','lastname')
        return last_name

    @staticmethod
    def GetDay():
        day = config.get('register info','day')
        return day

    @staticmethod
    def GetMonth():
        month = config.get('register info','month')
        return month

    @staticmethod
    def GetYear():
        year = config.get('register info', 'year')
        return year

    @staticmethod
    def GetEmail():
        email = config.get('register info', 'email')
        return email

    @staticmethod
    def GetPassword():
        password = config.get('register info', 'password')
        return password

    @staticmethod
    def GetConfirm_password():
        confirm_password = config.get('register info', 'confirm_password')
        return confirm_password

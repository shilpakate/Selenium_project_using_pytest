import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\One\Desktop\nopcom3\configurations\config.ini")


class ReadConfig:

    def get_base_url(self):
        url = config.get("common info", "base_url")
        return url

    def get_username(self):
        username = config.get("common info", "username")
        return username

    def get_password(self):
        password = config.get("common info", "password")
        return password

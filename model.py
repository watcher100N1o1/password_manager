import random
import json

class PasswordRecord:
    def __init__(self, Service, Username, Password, CreatedAt):
        self.__record = {"Service": Service ,
        "Username": Username, 
        "Password": Password,
        "CreatedAt": CreatedAt}

    def get_rec(self):
        return self.__record


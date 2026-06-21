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


def load_from_json_file(URL):
    try:
        with open(URL, "r", encoding="UTF-8") as file:
            data = json.load(file)

        return data
    
    except FileNotFoundError:

        print("Ошибка: файл несуществует!")
        print(f"Создание файла {URL}")

        file = open(URL, "w", encoding="UTF-8")
        file.close()


def record_to_file(URL, base_lst):
    with open(URL, "w", encoding="UTF-8") as file:
        json.dump(base_lst, file, ensure_ascii=False, indent=4)
import random
import json
import string
from datetime import datetime

def create_password(len_password:int):
    base_str = string.ascii_letters + string.digits
    password_str = ""
    for _ in range(len_password):
        password_str += random.choice(base_str)
    
    return password_str


def now_time():
    return (datetime.now()).strftime("%d.%m.%Y %H:%M")


class PasswordRecord:
    def __init__(self, service, username, len_password):
        self.__service = service 
        self.__username = username
        self.__password = create_password(len_password)
        self.__created_at = now_time()


    def get_rec(self):

        data_dict = {
            "Service": self.__service,
            "Username": self.__username,
            "Password": self.__password,
            "CreatedAt": self.__created_at
            }
        
        return data_dict



def create_record(base_lst:list):

    user = input("Введите имя аккаунта:")
    service = input("Введите название сервиса/ссылку на сервис:")

    try:

        
        len_pass = int(input("Введите длинну пароля:"))
    except ValueError:

        
        print("Ошибка: введено не число.")
        print("Попробуйте в следующий раз вводить только цифры.")
        return None

    data_rec = PasswordRecord(service, user, len_pass)

    base_lst.append(data_rec.get_rec())


def show_records(base_lst:list):

    
    print("\nЗаписи:")
    print("="*10)

    if base_lst:

        
        for rec in base_lst:

            
            print(f"Юзернейм: {rec["Username"]}")
            print(f"Сервис: {rec["Service"]}")
            print(f"Пароль: {rec["Password"]}")
            print(f"Дата создания: {rec["CreatedAt"]}")
            print("="*10)
    else:

        
        print("Список записей пуст.")


def delete_record(base_lst: list):

    
    if base_lst:

        
        need_name = input("Введите юзернейм:")

        for rec in base_lst:
            if rec["Username"] == need_name:

                
                question = "Вы уверены, что хотите удалить запись(Д/Н): "
                choice = input(question).lower()


                if choice == "д" or choice == "l":

                    
                    base_lst.remove(rec)

                    
                    print("Запись удалена!")
                    return None

                else:

                    
                    print("Отмена удаления...")
                    return None

        else:
            print(f"Запись с юзером {need_name} отсутствует в базе данных.")
            print("Попробуйте другой юзерней.")

    else:
        print("Список записей пуст.")




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



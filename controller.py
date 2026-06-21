import model
from view import show_menu

def main():
    base_lst = []
    while True:
        show_menu()

        choice = input("> ")

        if choice == "5":
            print("Завершение программы...")
            print("Всего доброго!")
            break
        else:
            print("Ошибка: невершная команда!")
            print("Попробуйте ввести одну из предложенных комманд.")

try:
    main()
except KeyboardInterrupt:
    print("\nЗавершение программы...")
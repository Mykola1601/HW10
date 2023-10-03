# HW 10

from collections import UserDict

# поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    ...


class Phone(Field):
    # реалізація класу 10 digit
    # Реалізовано валідацію номера телефону(має бути 10 цифр).
    ...


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone():
        ...

    def remove_phone():
        ...

    def edit_phone():
        ...

    def find_phone():
        ...


    # Реалізовано зберігання об'єкта Name в окремому атрибуті.
    # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
    # Реалізовано методи для додавання - add_phone/видалення -
    # remove_phone/редагування - edit_phone/пошуку об'єктів Phone -
    # find_phone.

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    # Додавання записів.
    # Пошук записів за іменем.
    # Видалення записів за іменем.
    def add_record():
        ...

    def find():
        ...

    def delete():
        ...
    # Реалізовано метод add_record, який додає запис до self.data.
    # Реалізовано метод find, який знаходить запис за ім'ям.
    # Реалізовано метод delete, який видаляє запис за ім'ям.
    # Записи Record у AddressBook зберігаються як значення у словнику.
    # В якості ключів використовується значення Record.name.value.
    ...


def main() : 
    book = AddressBook()



# ========================================
if __name__ == "__main__":
    main()

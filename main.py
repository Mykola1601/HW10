# HW 10

from collections import UserDict
import re 


def normalize_phone(phone):
    numbers = re.findall('\d+', str(phone))
    phone = (''.join(numbers))
    iterator = re.finditer(r"0[\d]+", phone)
    if iterator:
        for match in iterator:
            phone = match.group()
            if len(phone) == 10:
                return phone
        else:
            print('value error phone')
            raise ValueError


# поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.name = value
        # return self.name
  


class Phone(Field):
    # реалізація класу 10 digit

    def __init__(self, value):
        self.value = normalize_phone(value)
    
   



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone = str):
        self.phones.append(phone)
        AddressBook.add_record(self , self.name,   phone)

    def remove_phone():
        ...

    def edit_phone():
        ...

    def find_phone():
        ...


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


    # Реалізовано зберігання об'єкта Name в окремому атрибуті.
    # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
    # Реалізовано методи для додавання - add_phone/видалення -
    # remove_phone/редагування - edit_phone/пошуку об'єктів Phone -
    # find_phone.

class AddressBook(UserDict):
    book = {}
    # реалізація класу
    # Додавання записів.
    # Пошук записів за іменем.
    # Видалення записів за іменем.
    def add_record(self, *args):
        self.data[args[0]]= [args[1]]

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

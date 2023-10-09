# HW 10

from collections import UserDict
import re 


def normalize_phone(phone):
    numbers = re.findall('\d+', str(phone))
    phone = (''.join(numbers))
    if len(phone) == 10 :
    # iterator = re.finditer(r"[\d]{10}", phone)
    # if iterator:
    #     for match in iterator:
    #         phone = match.group()
    #         if len(phone) == 10:
        return phone
    else:
        # print('value error phone')
        # raise ValueError
        return None


# поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)




class Name(Field):
    def __init__(self, value):
        self.value = value
        # print(self.name)
  


class Phone(Field):
    # # реалізація класу 10 digit
    # def __init__(self, value):
    #     if type(value) is list:
    #         self.value = value
    #     else:
    #         self.value = normalize_phone(value)
    
    def __init__(self, value):
        if not normalize_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, *args):
        self.phones.append(args[0])
        name = self.name.value
        # phones = self.phones
        # print(name , self.phones)
        # book.add_record(name, phone)
        # book.add_record(self , name, phones)

    def remove_phone(self, *args):
        print(args)
        phone = args[0]
        name = self.name.name
        phones = book.delete(name)
        phones.remove(phone)
        book.add_record(name, phones)
        # book.add_record(self, self.name,  self.phones)

    def edit_phone(self, *args):
        print(args)
        phone = args[0]
        new_phone = args[1]
        name = self.name.value
        # phones = book.delete(name)
        phones = self.phones
        self.phones.append(new_phone)
        self.phones.remove(phone)
        # book.add_record(name, self)
        


    def find_phone(self, *args):
        phone = args[0]
        name = self.name.value
        # phones = book[name]
        result = book.find(name,phone)
        print(result)
        phones = result.phones
        if phone in phones:
            return self.name, phone
 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(self.phones)}"


    # Реалізовано зберігання об'єкта Name в окремому атрибуті.
    # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
    # Реалізовано методи для додавання - add_phone/видалення -
    # remove_phone/редагування - edit_phone/пошуку об'єктів Phone -
    # find_phone.

class AddressBook(UserDict):
    # Додавання записів.
    # Пошук записів за іменем.
    # Видалення записів за іменем.
    def add_record(self, *args): 
        name = args[0].name.value
        phone = args[0].phones
        # name = args[0].name
        # if name in self.data:
        #     p = self.data[name]
        #     p.append(phone)
        #     self.data[name] = p
        # else:
        #     self.data[name] = [phone]

        # self.data[name] = args[0]
        self.data[name] = args[0]
        print(f"added {name = } {phone = }")

    def find(self, *args):
        print(*args)
        name = args[0]
        if name in self.data:
            # a = self.data[name]
            # print({name:a}  )
            # return {name:(self.data[name])} #Record()
            # Record.phones = self.data[name]
            return  self.data[name]
        else:
            return None
        # self.data[args[0]] = args[1]

    def delete(self, *args):
        print(*args)
        if self.data.get(args[0]):
            self.data.pop(args[0])
            print(self.data)

    # Реалізовано метод add_record, який додає запис до self.data.
    # Реалізовано метод find, який знаходить запис за ім'ям.
    # Реалізовано метод delete, який видаляє запис за ім'ям.
    # Записи Record у AddressBook зберігаються як значення у словнику.
    # В якості ключів використовується значення Record.name.value.
    


book = AddressBook()

def main() : 

    # Створення нової адресної книги
    # book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    
    
    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    # print(john)
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.value}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(name , record)


# ========================================
if __name__ == "__main__":
    main()

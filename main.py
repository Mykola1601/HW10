# HW 10

from collections import UserDict
import re 


def normalize_phone(phone):
    numbers = re.findall('\d+', str(phone))
    phone = (''.join(numbers))
    if len(phone) == 10 :
        return phone
    else:
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
  

class Phone(Field):
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

    def remove_phone(self, *args):
        phone = args[0]
        self.phones.remove(phone)

    def edit_phone(self, *args):
        phone = args[0]
        new_phone = args[1]
        self.phones.append(new_phone)
        self.phones.remove(phone)
        
    def find_phone(self, *args):
        phone = args[0]
        if phone in self.phones:
            return Phone(phone)
        return None

 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(self.phones)}"


class AddressBook(UserDict):
    def add_record(self, *args): 
        name = args[0].name.value
        self.data[name] = args[0]

    def find(self, *args):
        name = args[0]
        if name in self.data:
            return  self.data[name]
        else:
            return None

    def delete(self, *args):
        if self.data.get(args[0]):
            self.data.pop(args[0])


book = AddressBook()


def main():
    book = AddressBook()


# ========================================
if __name__ == "__main__":
    main()

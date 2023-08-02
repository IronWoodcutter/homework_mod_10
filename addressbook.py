'''
Користувач взаємодіє з книгою контактів, додаючи, видаляючи та редагуючи записи. Також користувач повинен мати можливість шукати в книзі контактів записи за одним або кількома критеріями (полями).

Про поля також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими (телефон або email наприклад). Також записи можуть містити декілька полів одного типу (декілька телефонів наприклад). Користувач повинен мати можливість додавати/видаляти/редагувати поля у будь-якому записі.

В цій домашній роботі ви повинні реалізувати такі класи:

Клас AddressBook, який наслідується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів.
Клас Name, обов'язкове поле з ім'ям.
Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
Критерії приймання
Реалізовано всі класи із завдання.
Записи Record в AddressBook зберігаються як значення у словнику. Як ключі використовується значення Record.name.value.
Record зберігає об'єкт Name в окремому атрибуті.
Record зберігає список об'єктів Phone в окремому атрибуті.
Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
AddressBook реалізує метод add_record, який додає Record у self.data.

'''

from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def del_phone(self, phone):
        self.phones.remove(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        self.phones[self.phones.index(Phone(old_phone))] = Phone(new_phone)

    


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def value(self, value):

        self.value = value


class Phone(Field):
    def value(self, value):
        self.value = value


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
# test  
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')

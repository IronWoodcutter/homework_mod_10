# homework_mod_10
GoIT Module 10 homework

This code defines a class AddressBook that inherits from the UserDict class. The AddressBook class has a method add_record that takes a record as input and adds it to the data attribute of the AddressBook object.

The Record class represents a record in the address book. It has an __init__ method that takes a name and an optional phone as input. It initializes the name attribute with the given name and initializes an empty list phones. If a phone is provided, it appends it to the phones list.

The Record class also has methods add_phone, del_phone, and change_phone for adding, deleting, and changing phone numbers respectively. These methods manipulate the phones list.

The Field class is a base class for fields in a record. It has an __init__ method that takes a value as input and initializes the value attribute with the given value.

The Name class is a subclass of Field and represents the name field in a record. It has a method value that takes a value as input and sets the value attribute of the Name object.

The Phone class is also a subclass of Field and represents the phone field in a record. It has a method value that takes a value as input and sets the value attribute of the Phone object.

Overall, this code provides a basic implementation of an address book with the ability to add, delete, and change phone numbers for each record.

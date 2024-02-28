import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(self.name, self.email, self.phone, self.favorite)
        return copy_obj

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(self.filename, self.contacts)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts)
        copy_obj.contacts = copy.deepcopy(self.contacts)
        return copy_obj


def copy_class_person(person):
    return copy.copy(person)

def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)
    
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

person = Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False)
print(person)
copy_person = copy.copy(person)
print(copy_person)

persons = Contacts("user_class.dat", contacts)
print(persons)
copy_persons = copy.copy(persons)
print(copy_persons)
deep_persons = copy.deepcopy(persons)
print(deep_persons)
# e_contacts = copy(contacts)

# new_persons = copy_class_contacts(persons)

# new_persons.contacts[0].name = "Another name"

# print(persons.contacts[0].name)  # Allen Raymond
# print(new_persons.contacts[0].name)  # Another name
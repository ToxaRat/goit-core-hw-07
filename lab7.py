
from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, in1: str):
        # Клас Phone:Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр). - це привести до формату +380989456457
        phone = in1
        if in1 == None:
            raise ValueError("Потрібно 10 цифр")
        if len(phone)!=10:
            raise ValueError("Потрібно 10 цифр")
        # Видаліть всі символи, крім цифр та '+', з номера телефону
        pattern = r"[^1234567890]"
        replacement = ""
        phone = re.sub(pattern, replacement, phone)
        # чи номер не 10 цифр
        if len(phone)!=10:
            raise ValueError("Потрібно 10 цифр")
      
        self.value = phone

    def __str__(self):
        return self.value

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    # додаемо тел
    def add_phone(self, tel: str): 
        self.phones.append(Phone(tel))
 
    def remove_phone(self, oldtel: str):
        for i, v in enumerate(self.phones):
            if v.value == Phone(oldtel).value:
               del(self.phones[i])
        
    def edit_phone(self, oldtel: str, newtel: str):
        for i, v in enumerate(self.phones):
              if v.value == Phone(oldtel).value:
                self.phones[i] = Phone(newtel)

    def find_phone(self, oldtel: str) -> Phone:
        for el in self.phones:
            if el.value == oldtel:
                return el
        return None
   
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, Rec: Record):
        self.data[Rec.name.value] = Rec

    def find(self, name: str) -> Record:
        return self.data.get(name)
        
    def delete(self, name: str):
        self.data.pop(name)
        return None

def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    # перевірка на 9 цифр
    #john_record.add_phone(None)
    #john_record.add_phone("123456789")
    john_record.add_phone("5555555555")
    #john_record.add_phone("s555555555")
    #john_record.add_phone("s5555555555")
    john_record.add_phone("0000000000")
    john_record.remove_phone("0000000000")

    # Додавання запису John до адресної книги
    book.add_record(john_record)
  
    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    
    # Виведення всіх записів у книзі
    #for name, record in book.data.items():
    #    print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    #print("Find.John", john)
    john.edit_phone("1234567890", "1112223333")
    #print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    
    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    #print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
    
    # Видалення запису Jane
    book.delete("Jane") # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Виведення всіх записів у книзі
    #for name, record in book.data.items():
    #    print(record)

if __name__ == "__main__":
    main()
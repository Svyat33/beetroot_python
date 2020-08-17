import datetime
import json

PHONE_BOOK_NAME = 'team_phonebook_lesson.json'

class Human:
    def __init__(self, name, second_name, phone):
        self.name = name
        self.second_name = second_name
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def create_dict(self):
        return {
            'Name': self.name,
            'Second name': self.second_name,
            'Phone': self.phone,
            'Is college': False
        }

    def fill_data(self, data):
        self.name = data['Name']
        self.second_name = data['Second name']
        self.phone = data['Phone']


    def __eq__(self, other):
        return (self.name, self.second_name) == (other.name, other.second_name)

    def __str__(self):
        return (f'''
Имя:              {self.name}
Фамилия:          {self.second_name}
Моб. номер:       {self.get_phone()}''')


class College(Human):
    def __init__(self, name, second_name, phone, work_phone):
        super().__init__(name, second_name, phone)
        self.work_phone = work_phone

    def get_phone(self):
        if 10 <= datetime.datetime.now().hour < 18:
            return self.work_phone
        return super().get_phone()

    def create_dict(self):
        return {
            'Name': self.name,
            'Second name': self.second_name,
            'Phone': self.phone,
            'Work phone': self.work_phone,
            'Is college': True
        }

    def fill_data(self, data):
        self.name = data['Name']
        self.second_name = data['Second name']
        self.phone = data['Phone']
        self.work_phone = data['Work phone']


class PhoneBook:
    def __init__(self, name_file):
        self.name_file = name_file
        self.list_contacts_obj = []
        try:
            with open(name_file, 'r') as f_obj:
                temp = json.load(f_obj)
                for contact in temp:
                    new_person = self.return_person(contact['Name'], contact['Last Name'], contact['Phone'], contact.get('Work phone', ''), contact.get('Is college'))
                    self.add_person(new_person)
            print(f'JSON file {PHONE_BOOK_NAME} was loaded\n'
                  f'{temp}\n')
        except FileNotFoundError:
            print(f'JSON file {PHONE_BOOK_NAME}  not found')
            with open(name_file, 'w') as f_obj:
                demo_db = [{'Name': 'Vasiliy', 'Last Name': 'Pupkin', 'Phone': '0501013233', 'Is college': False},
                           {'Name': 'Jonathan', 'Last Name': 'Blame', 'Phone': '0123654987', 'Work phone': '234023502350',
                            'Is college': True}]
                json.dump(demo_db, f_obj)
        except:
            raise
        finally:
            with open(name_file, 'r') as f_obj:
                temp = json.load(f_obj)
            for contact in temp:
                new_person = self.return_person(contact['Name'], contact['Last Name'], contact['Phone'],
                                                contact.get('Work phone', ''), contact.get('Is college'))
                self.add_person(new_person)

    def save(self):
        list_to_write = [x.create_dict() for x in self.list_contacts_obj]
        try:
            with open(self.name_file, 'w') as f_obj:
                json.dump(list_to_write, f_obj)
        except:
            print('Не получилось сохранить файл')

    def return_person(self, name, second_name, phone, work_phone='', is_college=True):
        if is_college:
            return College(name, second_name, phone, work_phone)
        else:
            return Human(name, second_name, phone)

    def add_person(self, contact):
        if contact not in self.list_contacts_obj:
            self.list_contacts_obj.append(contact)


    # TODO: метод не проверен. МОжно добавить подтвреждение/вопрос про удаление
    def delete_contact(self, contact):
        if contact in self.list_contacts_obj:
            self.list_contacts_obj.remove(contact)


    def print_phonebook(self):
        for x in self.list_contacts_obj:
            print(x)



if __name__ == '__main__':
    phone_book_1 = PhoneBook(PHONE_BOOK_NAME)
    person_1 = phone_book_1.return_person('Ivan', 'Jefferson', '0951234567', is_college=False, work_phone='789456')

    phone_book_1.add_person(person_1)

    # a = person_1.create_dict()
    phone_book_1.print_phonebook()
    # phone_book_1.delete_contact(person_1)
    # phone_book_1.delete_contact(person_1)


    # print(a)
    # a['Name'] = 'Nikodim'
    # person_1.fill_data(a)
    # print(person_1)
    # phone_book_1.add_person(person_1)
    # person_2 = phone_book_1.return_person('Jo', 'Stevenson', '05612645', is_college=True, work_phone='0123456')
    # phone_book_1.add_person(person_2)
    # phone_book_1.print_phonebook()
    # phone_book_1.save()

# lesson_9_context_manager_JSON
# Task 2 .Extend Phonebook application
#
# Functionality of Phonebook application:
#
#     Add new entries
#     Search by first name
#     Search by last name
#     Search by full name
#     Search by telephone number
#     Search by city or state
#     Delete a record for a given telephone number
#     Update a record for a given telephone number
#     An option to exit the program
#
# The first argument to the application should be the name of the phonebook. Application should
# load JSON data, if it is present in the folder with application, else raise an error. After the
# user exits, all data should be saved to loaded JSON.
import uuid
import json
from os import path

PHONEBOOK_FILENAME = 'pb.json'


# Checking for exist then asking user: Demo? Create? Quit?
def is_phonebook():
    try:
        with open(PHONEBOOK_FILENAME, 'r') as f_obj:
            # Просто проверка. Можно удалить. Срабатывает лишний вывод.
            print("It's exist")
    except FileNotFoundError:
        while True:
            cmd = input('Phonebook file not found!\n'
                        'You wish to use Demo-phonebook or Create your own, and manually enter all data?\n'
                        'Type "D" for using demo-file, "C" for creating empty file or "Q" to quit: ')
            if cmd == 'Q' or cmd == 'q':
                print("Your Typed Q")
                exit()
            elif cmd == 'D' or cmd == 'd':
                demo_db()
                break
            elif cmd == 'C' or cmd == 'c':
                with open(PHONEBOOK_FILENAME, 'w') as f_obj:
                    print("It's created")
                    break
            else:
                print("You have entered a wrong command")
                continue
    except:
        raise


def demo_db():
    with open(PHONEBOOK_FILENAME, 'w') as f_obj:
        demo_db = [
            {"Record ID": "id_1", "First name": "John", "Last name": "Palmer", "Phone number": "0871234567", "Location": "Iqaluit"},
            {"Record ID": "id_2", "First name": "Jane", "Last name": "Mone", "Phone number": "0872345678", "Location": "Ottawa"},
            {"Record ID": "id_3", "First name": "Kevin", "Last name": "O'Brian", "Phone number": "0873456789", "Location": "Quebec"},
            {"Record ID": "id_4", "First name": "Sara", "Last name": "Conor", "Phone number": "0874567890", "Location": "Bergen"},
            {"Record ID": "id_5", "First name": "Karl", "Last name": "Bateman", "Phone number": "0875678901", "Location": "Stockholm"}
        ]
        # demo_db = {
        #     'id_1': {"First name": "John", "Last name": "Palmer", "Phone number": "0871234567", "Location": "Iqaluit"},
        #     'id_2': {"First name": "Jane", "Last name": "Mone", "Phone number": "0872345678", "Location": "Ottawa"},
        #     'id_3': {"First name": "Kevin", "Last name": "O'Brian", "Phone number": "0873456789", "Location": "Quebec"},
        #     'id_4': {"First name": "Sara", "Last name": "Conor", "Phone number": "0874567890", "Location": "Bergen"},
        #     'id_5': {"First name": "Karl", "Last name": "Bateman", "Phone number": "0875678901", "Location": "Stockholm"}
        # }
        json.dump(demo_db, f_obj)
        print("Demo-file created. And now you will using it.")


def read_phonebook():
    try:
        with open(PHONEBOOK_FILENAME, 'r') as f_obj:
            ret = json.load(f_obj)
        return ret
    except FileNotFoundError:
        return "File not found ERROR"
    except:
        pass

phonebook_read = read_phonebook()

def show_phonebook():
    rec_count = 0
    for contact in phonebook_read:
        rec_count +=1
        try:
            for k, v in contact.items():
                if k == 'Record ID':
                    v = v[:8]
                print(f'{k}: {v}')
        except:
            raise
        print('>==============<')
    print(f'\n<==============<Total number of contacts: {rec_count}>==============>')

# # function is used.
# def print_single_contact(contact):
#     for k, v in contact.items():
#         if k != 'App_No':
#             print(f'{k} : {v}')

def deleting():
    cmd = input('enter id')
    for contact in phonebook_read:
        if cmd == contact['id'][:5]:
            del contact
        else:
            pass

# To print separate contacts another function is used.
def print_single_contact(contact):
    for k, v in contact.items():
          if k != 'App_No':
               print(f'{k} : {v}')






def save_phonebook():
    with open(PHONEBOOK_FILENAME, 'w') as f_obj:
        json.dump(phonebook_read, f_obj)


def add_record():
    try:
        phonebook_read.append({
        'id': str(uuid.uuid4()),
        'name_first': input('Type first name: '),
        'name_last': input('Type last name: '),
        'tel_num': input('Type telephone number: '),
        'city': input('Type city: ')
        })
        save_phonebook()
    except:
        raise


def found_chk(pb_rec, sample):
    try:
        rec_str = ''
        for i in pb_rec.values():
            rec_str += "~~|~~" + str(i)
        return sample.lower() in rec_str.lower()
    except:
        return False


def search_record():
    def search_record():
        ret = []
        sample = input('Type sample:')
        for pb_rec in phonebook_read:
            if found_chk(pb_rec, sample):
                ret.append(pb_rec)
        return ret



# def del_rec():
#
#     # После удаления, обязательно перезаписать.
#     save_phonebook()




if __name__ == '__main__':
    '''MAIN LOOP'''
    is_phonebook()
    while True:
        cmd = input('A - Новая запись; S - поиск; D - удалить; U - обновить номер; L - показать все записи; '
                    'Q - выход. \nВведите команду: ')
        if cmd == 'Q' or cmd == 'Q':
            exit()
        elif cmd == 'L' or cmd == 'l':
            show_phonebook()
        elif cmd == 'A' or cmd == 'a':
            add_record()
        elif cmd == 'S' or cmd == 's':
            print(search_record())



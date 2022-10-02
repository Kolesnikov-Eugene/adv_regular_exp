import re
from pprint import pprint
import csv

PHONE_PATTERN = r'(\+7|8)+[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'

with open('phonebook_raw.csv', 'r') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# выполните пункты 1-3 ДЗ

def create_correct_list(contact_list: list):
    """func creates a correct list"""
    new_list = list()
    for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(PHONE_PATTERN, PHONE_SUB, item[5]), item[6]]
        new_list.append(result)

    return delete_duplicates(new_list)


def delete_duplicates(contacts: list):
    """function deletes duplicates"""
    for contact in contacts:

        first_name = contact[1]
        last_name = contact[0]
        for new_contact in contacts:

            new_first_name = new_contact[1]
            new_last_name = new_contact[0]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == '':
                    contact[2] = new_contact[2]
                if contact[3] == '':
                    contact[3] = new_contact[3]
                if contact[4] == '':
                    contact[4] = new_contact[4]
                if contact[5] == '':
                    contact[5] = new_contact[5]
                if contact[6] == '':
                    contact[6] = new_contact[6]

    final_list = list()

    for line in contacts:

        if not line in final_list:
            final_list.append(line)

    return final_list


# сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open('phonebook.csv', 'w') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(create_correct_list(contacts_list))

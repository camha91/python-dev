"""
Address book program
Implement a simple address book with additions, deletions, and changes
"""


class Record:
    global_id = 0

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        Record.global_id += 1
        self.record_id = Record.global_id

    def set_number(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return "{}\t{}\t{}".format(self.record_id, self.name, self.phone_number)


class PhoneBook:

    def __init__(self):
        self.data = []

    def add_record(self, record):
        self.data.append(record)

    def query_record(self, name):
        query_result = []
        query_ids = []
        for record in self.data:
            if record.name == name:
                query_result.append(record)
                query_ids.append(record.record_id)
        return query_ids, query_result

    def change_record(self, name):
        query_ids, query_result = self.query_record(name)
        if len(query_ids) == 0:
            print("Does not exist")
        else:
            if len(query_result) > 1:
                for record in query_result:
                    print(record)
                record_id = input("Please select the ID to be modified:")
                if int(record_id) in query_ids:
                    for record in self.data:
                        if int(record_id) == record.record_id:
                            phone_number = input("Please enter the modified phone number:")
                            record.set_number(phone_number)
                            print("Successfully modified")
                            break
                else:
                    print("Enter error!!!")
            else:
                print(query_result[0])
                phone_number = input("Please enter the modified phone number:")
                query_result[0].set_number(phone_number)
                print("Successfully modified")

    def delete_record(self, name):
        query_ids, query_result = self.query_record(name)
        if len(query_ids) == 0:
            print("Does not exist")
        else:
            if len(query_result) > 1:
                for record in query_result:
                    print(record)
                record_id = input("Please select the ID you want to delete")
                if int(record_id) in query_ids:
                    for record in self.data:
                        if int(record_id) == record.record_id:
                            self.data.remove(record)
                else:
                    print("Enter error!!!")
            else:
                print(query_result[0])
                while True:
                    s = input("Do you want to confirm the deletion (Y/N):")
                    if s in ["Y", "N"]:
                        if s == "Y":
                            self.data.remove(query_result[0])
                        else:
                            pass
                        break
                    else:
                        print("Enter error!!!")


if __name__ == "__main__":
    phonebook = PhoneBook()
    while True:
        menu = """
        1. Add
        2. Find
        3. Delete
        4. Modify
        5. Exit
        """
        print(menu)
        s = input("Please enter the operation:")
        if s in ["1", "2", "3", "4", "5"]:

            if s == "1":
                name = input("Please enter a name: ")
                phone_number = input("Please enter the phone: ")
                record = Record(name, phone_number)
                phonebook.add_record(record)
                print(record)
            if s == "2":
                name = input("Please enter a name: ")
                query_ids, query_result = phonebook.query_record(name)
                if len(query_ids) == 0:
                    print("Does not exist")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record.record_id, record.name, record.phone_number))
            if s == "3":
                name = input("Please enter a name: ")
                phonebook.delete_record(name)
            if s == "4":
                name = input("Please enter a name: ")
                phonebook.change_record(name)
            if s == "5":
                break
        else:
            print("Input error!!!")
            continue

"""
address book program
Implement a simple address book with additions, deletions, and changes
"""

import json

record_list = []
record_id = 0


def input_record():
    name = input("Please enter a name:")
    phone_number = input("Please enter the phone:")
    record = {"name": name, "phone_number": phone_number}
    return record


def add_record():
    record = input_record()
    global record_id
    record_id += 1
    record["record_id"] = record_id
    record_list.append(record)
    return "Successfully added"


def query_record(name):
    query_result = []
    query_ids = []
    for record in record_list:
        if record["name"] == name:
            query_ids.append(record["record_id"])
            query_result.append(record)
    return query_ids, query_result


def delete_record(name):
    query_ids, query_result = query_record(name)
    if len(query_ids) == 0:
        print("Does not exist")
    else:
        if len(query_result) > 1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            record_id = input("Please select the ID you want to delete")
            if int(record_id) in query_ids:
                for record in record_list:
                    if int(record_id) == record["record_id"]:
                        record_list.remove(record)
            else:
                print("Enter error!!!")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"], query_result[0]["name"], query_result[0]["phone_number"]))
            while True:
                s = input("Do you want to confirm deletion (Y/N): ")
                if s in ["Y", "N"]:
                    if s == "Y":
                        record_list.remove(query_result[0])
                    else:
                        pass
                    break
                else:
                    print("Enter error!!!")


def change_record(name):
    query_ids, query_result = query_record(name)
    if len(query_ids) == 0:
        print("Does not exist!!!")
    else:
        if len(query_result) > 1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            record_id = input("Please select the ID to be modified")
            if int(record_id) in query_ids:
                for record in record_list:
                    if int(record_id) == record["record_id"]:
                        phone_number =input("Please enter the modified phone number")
                        record["phone_number"] = phone_number
                        print("Successfully modified")
                        break
            else:
                print("Enter error!!!")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"],
                                      query_result[0]["name"], query_result[0]["phone_number"]))
            phone_number = input("Please enter the modified phone number")
            query_result[0]["phone_number"] = phone_number
            print("Successfully modified")


def phonebook_save(L):
    with open("/tmp/data.dat", "w") as f:
        json.dump(L, f)


def phonebook_load():
    global record_list
    with open("/tmp/data.dat", "r") as f:
        record_list = json.load(f)
        global record_id
        record_id = record_list[-1]["record_id"]


if __name__ == "__main__":
    try:
        phonebook_load()
    except Exception:
        print("Data file does not exist")
    while True:
        menu = """
        Address book
        1. Add
        2. Find
        3. Delete
        4. Modify
        5. Exit
        """
        print(menu)
        s = input("Please select the operation")
        if s in ["1", "2", "3", "4", "5"]:

            if s == "1":
                msg = add_record()
                print(msg)
            if s == "2":
                name = input("Please enter a name:")
                query_ids, query_result = query_record(name)
                if len(query_ids) == 0:
                    print("Does not exist")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            if s == "3":
                name = input("Please enter a name:")
                delete_record(name)
            if s == "4":
                name = input("Please enter a name:")
                change_record(name)
            if s == "5":
                break
        else:
            print("Input error")
            continue


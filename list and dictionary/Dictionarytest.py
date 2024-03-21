# Simple Student management project in dictionary  with [append/remove/search/update or id increasing automatic]
def add_password():
    try:
        password = int(input("Enter the password:_"))
    except ValueError:
        exit("Input only integer number not string ")
    if password == 1234:
        add_dictionary()
    else:
        print("Wrong password")


addList = []  # initilize the list


def add_dictionary():
    # Using exception for validation
    try:
        # input how many element we need  that can input from user
        numbers = int(input("Enter number how many time you want to add in dic:"))
    except ValueError:
        exit("Hello sir type or input only integer number not string -Thank you")

    for i in range(numbers):
        print("""
    *|================================================|*
    *|---=  Welcome to Student Management System =----|*
    *|================================================|*
    """)
        # Input the elements
        id = int(input("Enter the student id number:"))
        id = check_id(id)
        cname = (input("Enter the college name:").capitalize())  # Make capital to first char of word.
        name = (input("Enter the student name:").capitalize())
        faculty = (input("Enter faculty name:").capitalize())
        phone = int(input("Enter the student phone number:"))
        address = (input("Enter the student address:").capitalize())

        addList.append({
            "Id": id,
            "cname": cname,
            "name": name,

            "Faculty": faculty,
            "phone": phone,
            "address": address
        })

        print("Student details are:", addList)  # display

    exit_element()  # function calling


# Add elements concept and method in dictionary
def add_element1():
    # Using exception for validation
    try:
        # input how many element we need  that can input from user
        numbers = int(input("Enter number how many time you want to add in dic:"))
    except ValueError:
        exit("Hello sir type or input only integer number not string -Thank you")

    for i in range(numbers):
        id = int(input("Enter the student id number:"))
        id = check_id(id)
        cname = str(input("Enter the college name:").capitalize())
        name = str(input("Enter the student name:").capitalize())
        faculty = str(input("Enter faculty name:").capitalize())
        phone = int(input("Enter the student phone number:"))
        address = str(input("Enter the student address:").capitalize())

        addList.append({
            "Id": id,
            "cname": cname,
            "name": name,
            "Faculty": faculty,
            "phone": phone,
            "address": address
        })

        print("\n Student details are:", addList)

        exit_element()


# Remove elements concept and method in dictionary
def remove_element():
    remove_value = int(input("Which element do want to remove:_"))
    i = 0
    for values in addList:
        if values["Id"] == remove_value:
            addList.pop(i)
        i = i + 1
    print("\n", addList)
    exit_element()


# Continue and exit concept
def exit_element():
    yesno = input("Do you want to continue[y or n]:")
    if yesno == "y":
        addRemove = input("What do you want add , remove or search element? [a ,r , s or u]:")
        if addRemove == "a" or addRemove == "A":
            add_element1()
            exit_element()
        elif addRemove == "r" or addRemove == "R":
            remove_element()
            exit_element()
        elif addRemove == "u" or addRemove == "U":
            update_elements()
            exit_element()
        else:
            search_element()
            exit_element()

    else:
        print("Exit the program")


# Information about search with dictionary in python
def search_element():
    search_type = input("How do you want to search[cName/name/Id/Faculty/phone/address]:")
    if search_type in ["cname", "name", "faculty", "address"]:
        srcStd = input("Enter student key to search:_")
        counter = 0
        for key in addList:
            if key[search_type].lower() == srcStd.lower():
                print("Found this information", key)
                counter = counter + 1
        if counter > 0:
            exit_element()
        else:
            print("Not found the information with this value")
            exit_element()
    elif search_type in ["Id", "phone"]:
        srcStd = int(input("Enter student key to search:_"))
        for key in addList:
            if key[search_type] == srcStd:
                print("Found this information", key)
                exit_element()
            else:
                print("Not found details with this value")
                exit_element()
    else:
        print("Invalid value")
        exit_element()


def update_elements():
    key_id = int(input("Enter the id you want to update:"))

    for value in addList:
        if value["Id"] == key_id:
            print(value)
            update_key = input("Which value do you want to update[Id/cname/name/Faculty/address]:")
            if update_key in ("cname", "name", "Faculty", "address"):
                print("old value is :", value[update_key])
                new_value = input("Enter new value:")
                value[update_key] = new_value.capitalize()
            elif update_key in ("phone"):
                print("old value is: ", value[update_key])
                new_value = int(input("Enter new value:"))
                value[update_key] = new_value

            print("New values are", value)


def check_id(id):
    if len(addList) != 0:
        for value in addList:
            if value["Id"] == id:
                print("ID already taken")
                new_id = int(input("Enter new Id: "))
            else:
                new_id = id

    else:
        new_id = id
    return (new_id)


add_password()

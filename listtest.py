def rem_duplicates(user):
    for i in range(user):
        name = input("Enter the name:")
        # Here add the value in oldList how many name are input
        oldList.append(name)

    for i in oldList:
        # Here if there name in duplicate then not print but if not
        # duplicate then will be print in dupli list.
        if i not in dupliCa:
            dupliCa.append(i)

    # Print the all name how many input from user
    print("All name are:", str(oldList))

    # Print the name only without duplicate name in list
    print("Without duplicate name are:", str(dupliCa))
    continue_exit()

def continue_exit():
    a = input("Do You want to contiue[Y/N]:")
    if a == "Y" or a == "y":
        m = input("Do you want to Add or remove element[A/R]:")
        if m =="A" or m =="a":
            add_element()
        else:
            remove_element()
    else:
        print("Program Exit")

def add_element():
    # How many number should be needs to input the name
    user = int(input("Enter  how many number?:_"))

    # Now here user can iterator what input value until will be on.
    for i in range(user):
        name = input("Enter the name:")
        # Here add the value in oldList how many name are input
        oldList.append(name)

    for i in oldList:
        # Here if there name in duplicate then not print but if not
        # duplicate then will be print in dupli list.
        if i not in dupliCa:
            dupliCa.append(i)

    # Print the all name how many input from user
    print("All name are:", str(oldList))

    # Print the name only without duplicate name in list
    print("Without duplicate name are:", str(dupliCa))
    continue_exit()

def remove_element():
    # What and which value you want to remove from list you can choose the value
    rename = input("Which name do you want remove from above list?:_")

    # This is a condition if here input name already in list then sure it will be removed from list
    if rename in dupliCa:
        dupliCa.remove(rename)
        # Now here finally print the value after removing value will be show us and print here
        print("After removing name are:", dupliCa)
        print("Congratulation! your successful to remove the name from above list")
    else:
        print("Sorry! this name is not found in  above list so you can not remove this name")
    continue_exit()

dupliCa = []
oldList = []

x = int(input("How many elements do you want to add: "))
rem_duplicates(x)

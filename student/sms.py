detailslist = []


def details():
    id = int(input("Enter your id:_"))
    name = input("Enter your name:_")
    faculty = input("Enter your faculty name:_")
    college_name = input("Enter your college name:_")
    phone = int(input("Enter your phone number:_"))
    detailslist.append({
        "id": id,
        "name": name,
        "faculty": faculty,
        "college name": college_name,
        "phone": phone,

    })
    print(detailslist)
    exit_function()


def exit_function():
    yesno = input("Do want to continue[y or n]:_")
    if yesno == 'y' and yesno == 'n':
        details()
    else:
        print("Exit program")


details()

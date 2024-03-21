def exit_function():
    yesno = input("Do you want continue[y or n]:_")
    return yesno


def student_info():
    print('Student details')
    name1 = input("Enter the name:")
    Id = int(input("Enter the id:"))
    return name1, Id

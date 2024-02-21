
details=[]
def students_form():
 number=int(input("Enter how many time do you want fill up form?:_"))
 for i in range(number):
     print("Fill up following details")
     sname=input("Enter the student name:_")
     ssname=input("Enter the student school name:_")
     saddress=input("Enter the student address:_")
     sgmail=input("Enter the student gamil:_")
     ssnumber=int(input("Enter the student serial number:_"))

     details.append({
       "sname":sname,
       "ssname":ssname,
         "saddress":saddress,
         "sgmail":sgmail,
         "ssnumber":snumber


                   })
     print(details)
     exit_students()
def add_students():
    students_form()
def remove_students():
    remove_id=int(input("Which student details do you want to remove?Enter serial number:_"))
    i=0
    for value in details:
     if value["ssnumber"]==remove_id:
         details.pop(i)
     i+=1
    print(details)
def exit_students():
    yesno=input("Do you want continue[y] or [n]:_")
    if yesno=='y' or yesno=='Y':
        addremove=input("Do you want add or remove[a or r]:_")
        if addremove=='a' or addremove=='A':
            add_students()
            exit_students()
        else:
            remove_students()
            exit_students()

def search_students():
    search_key=input("How to do want to search?[sname/ssname/saddress/sgmail/ssnumber]:_")
    if search_key in ['sname','ssname','saddress','sgmail']:
        give_key=input("Enter key to search:_")
        for key in details:
            if key[search_key]==give_key:
                print("Found this student details:",key)
            else:
                print("Not found this student details")
    elif search_key in ['ssnumber']:
        give_key=int(input("Enter the key to search:_"))
        for key in details:
            if key[search_key]==give_key:
                print("Found this student details:",key)
            else:
                print("Not found this student details")
    else:
        print("Invalid information")









students_form()

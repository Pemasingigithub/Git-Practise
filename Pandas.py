import pandas as pd

dict1 = []


def data_entry():
    number_type = int(input("How many times do you want to entry data?:_"))
    for i in range(number_type):
        Id = int(input("Enter the id:_"))
        Name = input("Enter the name:_")
        Address = input("Enter the address:_")
        Faculty = input("Enter the faculty:_")
        dict1.append({
            "Id": Id,
            "Name": Name,
            "Address": Address,
            "Faculty": Faculty
        })


data_entry()
df = pd.DataFrame(dict1)
print(df)

yesno = input("Do want to continue?[y or n]:_")
if yesno == 'y' or yesno == 'Y':
    data_entry()
    print(df)
else:
    print("Exit program")

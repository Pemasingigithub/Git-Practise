import numpy as np
import pandas as pd
detail_list = []
number = int(input("How many times do want add information:_"))
for i in range(number):
    Id = int(input("Enter the id:_"))
    Name = input("Enter the name:_")
    Address = input("Enter the address:_")
    Faculty = input("Enter the faculty:_")
    detail_list.append({
        "Id": Id,
        "Name": Name,
        "Address": Address,
        "Faculty": Faculty
            })
    print(detail_list)
df = pd.DataFrame(detail_list)
df.head()



import pandas as pd
dict1 = {
    "Id": [1, 2, 3],
    "Name": ['Pema', 'Ram', 'Sita'],
    "Address": ['sindhu', 'Usa', 'kathmandu'],
    "Faculty": ['Management', 'Science', 'Education']
}

df = pd.DataFrame(dict1)
print(df.head())

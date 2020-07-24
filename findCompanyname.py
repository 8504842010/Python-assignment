import  re
str = "yash@datagrokr.com"

companyName = str.split('@')[1].split('.')[0]
print(companyName)
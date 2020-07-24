import  os

#print(os.listdir("."))
#print(os.path.abspath("/binarySearch.py"))

path = 'E:\mysql-test'     # As per Requirement
files = os.listdir(path)
for file in files:
    print(file)

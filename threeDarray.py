r = int(input("Enter the number of 2D array"))
c = int(input("Enter the number of rows"))
z=int(input("Enter the number of columns"))
array=[]
for i in range(r):
    a=[]
    for j in range(c):
        b=[]
        for k in range(z):
            b.append(0)
        a.append(b)
    array.append(a)

for i in range(r):
    for j in range(c):
        for k in range(z):
            print(array[i][j][k],end=" ")
        print(end="\n")
    print("\n")

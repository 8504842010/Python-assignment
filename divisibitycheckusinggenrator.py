def checkdivisibilty(n):
    i=1
    for i in range(1, n):
        if i % 5 == 0 and i % 7 == 0:
            yield i





val = int(input("Enter the Number: "))
print(*checkdivisibilty(val),sep=",")

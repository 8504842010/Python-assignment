import mysql.connector
dataBase = mysql.connector.connect(user='root',
                               host='localhost',
                               password="",
                               database='solution')

def fetch_data_using_genrator():
    cursorObject = dataBase.cursor()
    query = "SELECT * FROM employees"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    for x in myresult:
        yield x


for row in fetch_data_using_genrator():
    print(row)



# selecting query


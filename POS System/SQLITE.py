import sqlite3
from DatabaseOpen import DatabaseOpen
#ADMINLOGIN Name, Password: admin 123

conn = sqlite3.connect('./Settings/Database/AdminLogin.db')

c= conn.cursor()


def a():
    test= input("try:")
    passw= input()
    c.execute(f"SELECT * FROM ADMINLOGIN WHERE Name=? and Password=?",[test,passw])

    print(c.execute(f"SELECT * FROM ADMINLOGIN WHERE Name=? and Password=?",[test,passw]))

    if(c.fetchone()==None):
        print("Wrong Password")
    else:
        print("1241658")
    

    c.execute("""CREATE TABLE Items(
            ItemName Text NOT NULL,
            Price REAL,
            ImageName Text
    ) """)

#c.execute("SELECT * FROM Items")

#print(c.fetchall())
#conn.commit()

aa = DatabaseOpen()



wao =aa.FetchData()
print(wao)

for i in wao:
    print(wao[i][1]['ItemName'])
    print(wao[i][1]['Price'])
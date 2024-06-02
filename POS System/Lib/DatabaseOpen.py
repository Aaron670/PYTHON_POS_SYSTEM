import sqlite3
import json
class DatabaseOpen():
    def __init__(self):
        self.conn = sqlite3.connect('./Settings/Database/AdminLogin.db')

        self.c= self.conn.cursor()

    def Connect(self):
        return self.conn    
    
    def FetchData(self):
        # SPAGHETTI CODE
        conn= self.conn

        conn.row_factory = DatabaseOpen.dict_factory
        cur = conn.row_factory
        cur = conn.cursor()
        cur.execute("SELECT * FROM Foods as a")
        
        e = str(cur.fetchall())
        e =e[:-2]
        e=e[2:]
        e = e.replace('"',"")
        e=f'"{e}"'
        e = json.loads(e)
        e =eval(e)
        f={}
        j=0
        for i in e:
            print("THIS IS i",i)
            i=str(i)
            i=eval(i)        
            f[j]=i
            j=j+1
        
        return f
        # IF IT WORKS DONT QUESTION IT

    def dict_factory(cursor, row):
        d = {}
        i=0
        e={}
        for idx, col in enumerate(cursor.description):
            
            d[col[0]] = row[idx]
            i=i+1
            if i==3:
                e[1]=d
        e=str(e)

        return e    
    

        

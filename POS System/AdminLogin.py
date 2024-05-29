import sqlite3
from tkinter import *
from tkinter import messagebox
from DatabaseOpen import DatabaseOpen

class AdminPanel(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.db =DatabaseOpen()
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title("Admin Login")
        self.master.geometry("400x700")
        self.Login()
        self.array = ["Name of Product: ","Price: ","ImageName: "]
        self.conn = self.db.Connect()

    #Back-End   
    def Check(self,num):
        if(num==1):
            login = self.Login.get()
            passw = self.Pass.get()
            
            c= self.conn.cursor()
            c.execute(f"SELECT * FROM ADMINLOGIN WHERE Name=? and Password=?",[login,passw])
            if(c.fetchone()==None):
                print("Wrong Password")
                messagebox.showwarning("Error","Wrong Password or Admin")
            else:
                print("Login Success!")
                self.master.bind("<Return>",lambda event:self.Check(2))
                self.master1.destroy()
                self.create_widgets()
            
        else:
            print("Button pressed")
        c.close()

        

    def Login(self):
        self.master1 = Canvas(self.master)
        self.master1.pack()

        self.Login = Entry(self.master1)
        self.Pass = Entry(self.master1)
        LoginLabel = Label(self.master1,text='Login: ')
        PassLabel = Label(self.master1,text='Password:')

        self.Login.grid(column=2,row=1)
        self.Pass.grid(column=2,row=2)

        LoginLabel.grid(column=1,row=1)
        PassLabel.grid(column=1,row=2)
        button = Button(self.master1,text="LOGIN",command=lambda :self.Check(1))
        self.master.bind("<Return>",lambda event:self.Check(1))
        button.grid(column=2,row=3)

#Front-End

    def AddProduct(self):
        def save():
            for entry in entries:
                a= entry.get()
                if(a==""):
                  print("Please complete the form")
                  break
                else:
                    print("yay")
                    
                    Items.append(a)  
            a = self.conn.cursor()
            
            a.execute(f"INSERT INTO Items VALUES(?,?,?)",[entries[0].get(),entries[1].get(),entries[2].get()])
            self.conn.commit()
            

        NewWindow = Tk()
        NewWindow.title("ADD PRODUCT")
        entries = []
        Items = []
        j=1
        for name in self.array:
            label1 = Label(NewWindow,text=name)
            label1.grid(column=1,row=j, sticky=W)
            name = Entry(NewWindow)
            name.grid(column=2,row=j)
            entries.append(name)
            j=j+1
        button1= Button(NewWindow,text="Save", command=save)
        button1.grid(column=3,row=4)

        print("Add")

    def UpdateProduct(self):
        def save():
            Save=[]
            for i in entries:

                Save.append(i.get())
                print(Save)
                pass
            

        print("Up")
        NewWindow= Tk()
        array=["Product Name: ","Change Price: "]
        entries =[]
        j=0
        for i in array:
            i= Label(NewWindow,text=f"{array[j]}").grid(column=0,row=j)
            name = Entry(NewWindow)
            name.grid(column=1,row=j)
            entries.append(name)
            j=j+1
        Button(NewWindow,text="Submit",command=save).grid(column=4,row=j+2)

        


    def DeleteProduct(self):
        def save():
            entry1= entry.get()
            a = self.conn.cursor()
        
            a.execute(f"DELETE FROM Items WHERE ItemName=?",[entry1])

            self.conn.commit()
            print("Successfully Deleted")
        
        NewWindow= Tk()
        label1 =Label(NewWindow,text="Insert ProductName")
        entry = Entry(NewWindow)
        label1.grid(column=0,row=0)
        entry.grid(column=0,row=1)
        button1= Button(NewWindow,text="Save", command=save)
        button1.grid(column=3,row=4)
        NewWindow.title("DELETE PRODUCT")

    def ProductList(self):
        print("Check")
        NewWindow=Tk()
        v_scrollbar = Scrollbar(NewWindow, orient='vertical')
        v_scrollbar.pack(side='right', fill='y')

        NewWindow.geometry("300x900")
        canvas = Canvas(NewWindow, yscrollcommand=v_scrollbar.set)
        canvas.pack(fill='both', expand=True)
        NewWindow.title("PRODUCT LIST")
        
        v_scrollbar.config(command=canvas.yview)


        db=self.db.FetchData()
        j=0
        for i in db:
            print(i)
            w=Label(canvas,text="=================").pack()
            i=Label(canvas,text=f"Item Name: {db[j][1]['ItemName']}",justify=LEFT).pack()
            i=Label(canvas,text=f"Item Price: {db[j][1]['Price']}",justify=LEFT).pack()

            j=j+1
        canvas.config(scrollregion=canvas.bbox('all'))


    def create_widgets(self):
        self.Canva1= Canvas(self.master)
        self.Canva1.pack(anchor=CENTER)
        self.master.title("ADMIN PAGE")
        # List ng mga buttons // NOTE: Mag iiba na pangalan nung buttons once na initialize ng gantong paraan
        buttons = ["Add New Product:", "Update Product: ","Delete Product: ","Check Product List: "]
        # List ng mga func names na nasa loob nung class
        methods= [self.AddProduct,self.UpdateProduct,self.DeleteProduct,self.ProductList]
        #Counter
        j=0
        for i in buttons:
            i = Button(self.Canva1,text=i,command=methods[j])
            i.pack()
            j=j+1


root= Tk()
AdminPanel(root)

root.mainloop()
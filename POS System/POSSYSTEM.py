from tkinter import *
from tkinter import ttk
from DatabaseOpen import DatabaseOpen
import locale

locale.setlocale(locale.LC_ALL, 'en_PH')

class Items(Button):
    def __init__(self,name,price,img):
        self.name= name
        self.price= price
        self.img =img

class PosSystem_Start(Frame):

    def __init__(self, master):
        #=========DATABASE HERE=========
        a= DatabaseOpen()
        self.db= a.FetchData()
        #===============================
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title("Python POS project")
        self.master.geometry("1280x720")
        self.tasks = []
        self.ItemsN=0
        self.GrandTotal=0.00
        self.create_widgets()
        root.bind("<BackSpace>", lambda event: self.delete())
        
    #Back-End 
    def AddItems(self, item,quantity, price):
        self.ItemList.insert("", "end", values=(self.ItemsN, item, quantity, price))
        price= price*quantity
        self.GrandTotal= self.GrandTotal+price
        self.ItemsN=self.ItemsN+1
        self.UpdateTotal()

        pass
    def UpdateTotal(self):
        global formatted_currency
        formatted_currency = locale.currency(self.GrandTotal, grouping=True)

        self.GrandTotalLabel.configure(text=f"Grand Total: {formatted_currency}")


        


    def ClearList(self):
        self.GrandTotal=0
        for SelectItems in self.ItemList.get_children():
            print(SelectItems)
            self.ItemList.delete(SelectItems)
        self.ItemsN=0
        self.UpdateTotal()

    def delete(self):
        for SelectItems in self.ItemList.get_children():
            pass
        
        amount = self.ItemList.item(SelectItems)['values'][2]
        Price = self.ItemList.item(SelectItems)['values'][3]
        Price = float(Price)*amount

        self.ItemList.delete(SelectItems)
        
        self.GrandTotal = self.GrandTotal-Price
        self.ItemsN=self.ItemsN-1
        self.UpdateTotal()
        
#FRONT END HERE
    def create_widgets(self):
        self.Empty= Frame(root)
        self.Empty.pack(side=LEFT,padx=15)
        self.FrameItems =Frame(root)
        self.FrameItems.pack(side=LEFT)


        self.FrameTotal = Frame(root)
        self.FrameTotal.pack(side=RIGHT)
        self.GrandTotalLabel= Label(text=f"Grand Total: ₱{self.GrandTotal:.2f}",font="Arial 20")
        self.GrandTotalLabel.pack()



        self.ItemList = ttk.Treeview(self.FrameItems, columns=("#", "Item Info", "Quantity", "Price"), show="headings")

        self.ItemList.heading("#",text="#",anchor=W)
        self.ItemList.heading("Item Info",text="Item Info",anchor=W)
        self.ItemList.heading("Quantity",text="Quantity",anchor=W)
        self.ItemList.heading("Price",text="Price",anchor=W)



        self.ItemList.pack(fill="both", expand=True)


        self.button2= Button(root,command=self.delete,text="Remove Last in List")
        self.button3 = Button(root,command=self.ClearList,text="Clear List")
        self.button2.pack()
        self.button3.pack()


        self.FrameItemsC =Frame(root,bg="gray")
        self.FrameItemsC.pack(side=RIGHT)
        self.AddStuff()

    def getItem(self,k):
        j=0
        db=self.db
        print(k)
        self.AddItems(db[k][1]['ItemName'],1,db[k][1]['Price'])
        

    def AddStuff(self):
        Label(self.FrameItemsC,text="ITO UNG MENU").pack
        db=self.db
        print(db)
        j=0
        alAr=["q","w","e","r"]
        for i in db:
            i = Button(self.FrameItemsC,text=db[j][1]['ItemName'],command=lambda i=i: self.getItem(i))
            root.bind(f"<KeyPress-{alAr[j]}>", lambda event: self.getItem(i))
            self.tasks.append(i)
            i.grid(column=1,row=j)
            
            j=j+1



root=Tk()
PosSystem_Start(root)


root.mainloop()
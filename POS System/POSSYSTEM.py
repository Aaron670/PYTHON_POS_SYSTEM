from tkinter import *
from tkinter import ttk


class PosSystem_Start(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title("Python POS project")
        self.master.geometry("1280x720")
        self.tasks = []
        self.ItemsN=0
        self.GrandTotal=0.00
        self.create_widgets()
        
    #Back-End 
    def AddItems(self, item,quantity, price):
        self.ItemList.insert("", "end", values=(self.ItemsN, item, quantity, price))
        price= price*quantity
        self.GrandTotal= self.GrandTotal+price
        self.ItemsN=self.ItemsN+1
        self.UpdateTotal()

        pass
    def UpdateTotal(self):
        self.GrandTotalLabel.configure(text=f"Grand Total: ${self.GrandTotal:.2f}")

    def DebugAdd(self): #Remove in Final Build
        array = ["TestItem",10,200]
        self.AddItems(array[0],array[1],array[2])
        
        

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
        global GrandTotal
        self.Empty= Frame(root)
        self.Empty.pack(side=LEFT,padx=15)
        self.FrameItems =Frame(root)
        self.FrameItems.pack(side=LEFT)


        self.FrameTotal = Frame(root)
        self.FrameTotal.pack(side=RIGHT)
        self.GrandTotalLabel= Label(text=f"Grand Total: ₱{self.GrandTotal:.2f}")
        self.GrandTotalLabel.pack()



        self.ItemList = ttk.Treeview(self.FrameItems, columns=("#", "Item Info", "Quantity", "Price","Button"), show="headings")

        self.ItemList.heading("#",text="#",anchor=W)
        self.ItemList.heading("Item Info",text="Item Info",anchor=W)
        self.ItemList.heading("Quantity",text="Quantity",anchor=W)
        self.ItemList.heading("Price",text="Price",anchor=W)



        self.ItemList.pack(fill="both", expand=True)


        self.button1= Button(root,command=self.DebugAdd,text="Debug: Add To List")
        self.button2= Button(root,command=self.delete,text="Remove Last in List")
        self.button3 = Button(root,command=self.ClearList,text="Clear List")
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()


    







root=Tk()
PosSystem_Start(root)

root.mainloop()
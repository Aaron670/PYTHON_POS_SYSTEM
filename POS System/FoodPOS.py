from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import locale
import AdminLogin
import datetime
import time
import sys
sys.path.insert(1, './Lib')
from DatabaseOpen import DatabaseOpen

locale.setlocale(locale.LC_ALL, 'en_PH')

class PosSystem_Start(Frame):
    def __init__(self, master):
        self.name1="FOOD STORE X"
        self.master = master
        self.master.geometry("1300x650")
        self.master.title("FOOD STORE P.O.S")
        self.master.resizable(0,0)
        self.master.configure(bg = "light gray")
        a=DatabaseOpen()
        self.db=a.FetchData()
        self.tasks=[]
        self.GrandTotal=0
        
        self.openadPress=0

        #   Frames
        self.frame = Frame(self.master, width = 1300, height = 80, bg = "gray") # top header 
        self.frame.pack()

        self.frame1 = Frame(self.master, width = 300, height = 520, bg = "white") #display screen for the list of purchases
        self.frame1.place(x= 40, y = 100)

        self.frame2 = Frame(self.frame1, width = 300, height = 50, bg = "gray") #frame for the small header in the list
        self.frame2.pack(fill=X)

        self.frame3 = Frame(self.master, width = 900, height = 520, bg = "light gray") #frame for the grid in the buttons
        self.frame3.place(x= 380, y= 100)
        
        self.LabelGrandTotal= Label(self.frame1, text=f"Grand Total: ₱{self.GrandTotal:.2f}", bg= "white", fg = "black", font = "Arial 12")
        
        self.master.bind("<BackSpace>", lambda event: self.deleteLast())

        self.CreateWidgets()
        self.CreateButtons()
        self.master.mainloop()
    
    def AddItems(self, item,quantity, price):
        a=self.ItemList.get_children()
        if(a!=()):
            for SelectItems in self.ItemList.get_children():
                name=self.ItemList.item(SelectItems)["values"][0]
                if(item==name):
                    curquan=self.ItemList.item(SelectItems)["values"][1]
                    self.DelItem(item)
                    quantity=quantity+curquan
                    self.ItemList.insert("", "end",values=(item, quantity, price))
                    
                    self.GrandTotal=self.GrandTotal+(quantity*price)
                    break

                else:
                 pass   
            if(item!=name):
                self.ItemList.insert("", "end",values=(item, quantity, price),)
                price= price*quantity
                self.GrandTotal= self.GrandTotal+price
            
    
        else:
            self.ItemList.insert("", "end",values=(item, quantity, price),)
            price= price*quantity
            self.GrandTotal= self.GrandTotal+price

        

        self.UpdateTotal()
    
    def getItem(self,k,c):
        print("waa")
        db=self.db
        if(c==""):
            print(k)
            self.AddItems(db[k][1]['ItemName'],1,db[k][1]['Price'])
        else:
            Item=f"{db[k][1]['ItemName']}({c})"
            self.AddItems(Item,1,db[k][1]['Price'])
        
    def ItemWhat(self,k):
        newWind=Tk()
        Label(newWind,text="Comment: ").grid(row=0)
        Comment=Entry(newWind)
        Comment.grid(row=1)
        newWind.bind(f"<Tab>", lambda event: [self.getItem(k,Comment.get()),newWind.destroy()])
        self.master.bind(f"<Tab>", lambda event: [self.getItem(k,Comment.get()),newWind.destroy()])
        button=Button(newWind,text="Save",command=lambda:[self.getItem(k,Comment.get()),newWind.destroy()]).grid(column=2,row=3)
        
  

    def UpdateTotal(self):
        global formatted_currency
        formatted_currency = locale.currency(self.GrandTotal, grouping=True)

        self.LabelGrandTotal.configure(text=f"Grand Total: {formatted_currency}")


        


    def ClearList(self):
        self.GrandTotal=0
        for SelectItems in self.ItemList.get_children():
            self.ItemList.delete(SelectItems)
        self.UpdateTotal()

    def DelItem(self,item1):
            for SelectItems in self.ItemList.get_children():
                name1=self.ItemList.item(SelectItems)["values"][0]
                if(name1==item1):
                    print(name1,item1)
                    amount = self.ItemList.item(SelectItems)['values'][1]
                    Price = self.ItemList.item(SelectItems)['values'][2]
                    print(Price,"AND",amount)
                    Price = float(Price)*amount
                    self.ItemList.delete(SelectItems)
                    print("DELETED")

                    self.GrandTotal = self.GrandTotal-Price
                    self.UpdateTotal()
                    break
                else:
                    print(f"FAILED {name1}!={item1}")

                


    def deleteLast(self,Sitem=None):
            if Sitem==None:
                print("None")
                for SelectItems in self.ItemList.get_children():
                    print(SelectItems)
                    pass
                
                Sitem=SelectItems
                amount = self.ItemList.item(Sitem)['values'][1]
                Price = self.ItemList.item(SelectItems)['values'][2]
                Price = float(Price)*amount


            self.ItemList.delete(Sitem)
            
            print(f"{self.GrandTotal}-{Price}")
            self.GrandTotal = self.GrandTotal-Price
            self.UpdateTotal()[[[[[[]]]]]]
    def OpenAd(self):
            print("hello")
            if(self.openadPress!=5):
                self.openadPress=self.openadPress+1
            else:
                root1= Tk()
                AdminLogin.AdminPanel(root1)
                self.master.destroy()
         
    def PrintOrder(self):
        OrderWind=Tk()
        for i in range(5):
            Label(OrderWind,text="").grid(row=i+2,column=0)
        x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Label(OrderWind,text=self.name1,font="Arial 20").grid(columnspan=3,row=0,sticky=N)
        Label(OrderWind,text=x).grid(sticky=E,row=1,column=0)
        j=4
        
        Label(OrderWind,text=f"========================").grid(columnspan=3,row=3)
        for i in self.ItemList.get_children():
            a= str(self.ItemList.item(i)['values'][0])
            b= str(self.ItemList.item(i)['values'][1])
            c= str(self.ItemList.item(i)['values'][2])
            
            Label(OrderWind,text=f"{a}").grid(column=0,row=j,sticky=W)
            Label(OrderWind,text=f"{b}").grid(column=1,row=j)
            Label(OrderWind,text=f"{c}").grid(column=2,row=j)
            j=j+1
            
            
            print(f"{a}     {b}     {c}")
            pass
        Label(OrderWind,text=f"========================").grid(columnspan=3,row=j+1)
        Label(OrderWind,text=f"Total: {self.GrandTotal}").grid(column=0,row=j+2,sticky=W)
        Label(OrderWind,text=f"-------------------------------------").grid(columnspan=3,row=j+3,sticky=S)
        Label(OrderWind,text=f"    ***THANK YOU***     ").grid(columnspan=3,row=j+4,sticky=S)
        self.ClearList()
    
    def CreateWidgets(self):
        
        self.master.bind(f"<KeyPress-m>", lambda event: self.OpenAd())

        self.spFrame = Frame(self.master, width = 100, height = 520, bg= "light gray")
        self.spFrame.place(x= 1225, y = 100)

        #labels
        widthItem=100
        self.ItemList = ttk.Treeview(self.frame1, columns=("Item Info", "Quantity", "Price"), show="headings",height=15)
        self.columnTree=["Item Info", "Quantity", "Price"]
        for i in self.columnTree:
            self.ItemList.column(i,width=widthItem, stretch=0,anchor=CENTER, minwidth=100)
            self.ItemList.heading(i,text=i,anchor=CENTER)

        self.ItemList.pack()

        
        Labell = Label(self.master, text= self.name1, bg= "gray", fg = "black", font = "Arial 45")
        Labell.place(x= 0.5, y = 0.5)

        Label2 = Label(self.master, text = "ITEM/S", bg= "gray", fg = "black", font = "Arial 15")
        Label2.place(x = 55, y = 100)

        Label3 = Label(self.master, text = "QTY", bg= "gray", fg = "black", font = "Arial 15")
        Label3.place(x = 160, y = 100)

        Label4 = Label(self.master, text = "PRICE", bg= "gray", fg = "black", font = "Arial 15")
        Label4.place(x = 260, y = 100)

        Label5 = Label(self.master, text = "CATEGORY", bg= "light gray", fg = "black", font = "Arial 8")
        Label5.pack(side = TOP)

        #LABELS FOR THE ITEMS, QTY, PRICE (IT, QTY, PRI)


        LabelLINE= Label(self.frame1, text = "------------------------------------", bg= "white", fg = "black", font = "Arial 18").pack()
        

        self.LabelGrandTotal.pack()
        #buttonRemoveLast=Button(self.master,text="REMOVE LAST",command=self.deleteLast)

        

    

    def CreateButtons(self):
        frameArray=["1","self.framefood2","self.framefood3","4","5","6","7","8"]
        self.frameArrayLoop=[]
        j=1
        k=1
        for i in frameArray:
            if(j==3)or(j==5)or(j==7):
                print(j)
                j=1
                k=k+1
                
            i=Frame(self.frame3, width = 400, height = 130, bg = "light gray")
            self.frameArrayLoop.append(i)
            i.grid(row=k,column=j,sticky=W)
            j=j+1
                

        spButton1 = Button(self.master, text = "VOID ORDER", bg = "red", fg= "black", font = "Arial 12", activebackground= "red",command=self.ClearList)
        spButton1.place(x = 120, y = 585)

        spButton2 = Button(self.master, text = "CHECK OUT", bg = "green", fg= "black", font = "Arial 12", activebackground= "green",command=self.PrintOrder)
        spButton2.place(x = 230, y = 585)

        spbutton3 = Button(self.spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton3.grid(row = 1, column = 1)

        spbutton4 = Button(self.spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton4.grid(row = 2, column = 1)

        spbutton5 = Button(self.spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton5.grid(row = 3, column = 1)

        spbutton6 = Button(self.spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton6.grid(row = 4, column = 1)



        #food section 
        

        db=self.db
        j=0
        alAr="qwertyuiopasdfghjkl;'zxcvbn"
        for i in db:
            #phIMG = PhotoImage(f"./Settings/ImageLinks/{db[j][1]['ImageName']}")
            iImg=db[j][1]['ImageName']
            phIMG = PhotoImage(file=f"Settings/ImageLinks/Menu50/{iImg}")
            RowNum=int(db[j][1]['ItemNum'])
            
            #i = Button(self.frameArrayLoop[RowNum-1], text=db[j][1]['ItemName'],command=lambda i=i: self.getItem(i), width= 10, height=8, bg= "yellow", fg = "black", activebackground= "yellow")
            i = Button(self.frameArrayLoop[RowNum-1],image=phIMG,command=lambda i=i: self.ItemWhat(i))   # Photo INSTEAD OF TEXT

            i.phIMG=phIMG
            self.tasks.append(i)
            i.grid(column=j,row=1)
            
            j=j+1








        


if __name__ == "__main__":

    root=Tk()
    PosSystem_Start(root)



from tkinter import *
from tkinter import ttk
import locale
import time
locale.setlocale(locale.LC_ALL, 'en_PH')

class PosSystem_Start(Frame):
    def __init__(self, master,name):
        self.master = master
        self.master.geometry("1310x650")
        self.master.title("DEPARTMENT STORE P.O.S")
        self.master.resizable(0,0)
        self.master.configure(bg = "light gray")
        self.db=[]
        self.GrandTotal=0
        self.name1=name

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
                    print(True)
                    curquan=self.ItemList.item(SelectItems)["values"][1]
                    self.DelItem(item)
                    quantity=quantity+curquan
                    self.ItemList.insert("", "end",values=(item, quantity, price))
                    
                    self.GrandTotal=self.GrandTotal+(quantity*price)

                else:
                 pass   
            if(item!=name):
                print("Not Equal",item,name)
                self.ItemList.insert("", "end",values=(item, quantity, price),)
                price= price*quantity
                self.GrandTotal= self.GrandTotal+price
            
            
        else:
            print("faield")
            self.ItemList.insert("", "end",values=(item, quantity, price),)
            price= price*quantity
            self.GrandTotal= self.GrandTotal+price

        

        self.UpdateTotal()
    
    
        
    def DebugAdd(self):
        #for i in range(2):
            #i=i+1
            i=1
            self.AddItems(f"Hello{i}",i,i+100) 
    def DebugAdd2(self):
        #for i in range(2):
            #i=i+1
            i=2
            self.AddItems(f"Hello{i}",i,i+100) 

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
            self.UpdateTotal()

    def CreateWidgets(self):
        

        

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
        #buttons for special features
        spButton1 = Button(self.master, text = "VOID ORDER", bg = "red", fg= "black", font = "Arial 12", activebackground= "red",command=self.ClearList)
        spButton1.place(x = 120, y = 585)

        spButton2 = Button(self.master, text = "CHECK OUT", bg = "green", fg= "black", font = "Arial 12", activebackground= "green")
        spButton2.place(x = 230, y = 585)


        
        spbutton3 = Button(self.frame3, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton3.grid(row = 1, column = 11)

        spbutton4 = Button(self.frame3, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton4.grid(row = 2, column = 11)

        spbutton5 = Button(self.frame3, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton5.grid(row = 3, column = 11)

        spbutton6 = Button(self.frame3, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
        spbutton6.grid(row = 4, column = 11)



        #dress section
        buttond1 = Button(self.frame3, width= 10, height=8, text = "DRESS 1", bg= "yellow", fg = "black", activebackground= "yellow")
        buttond1.grid(row = 1, column = 1)

        buttond2 = Button(self.frame3, width= 10, height=8, text = "DRESS 2", bg= "yellow", fg = "black", activebackground= "yellow")
        buttond2.grid(row = 1, column = 2)

        buttond3 = Button(self.frame3, width= 10, height=8, text = "DRESS 3", bg= "yellow", fg = "black", activebackground= "yellow")
        buttond3.grid(row = 1, column = 3)

        buttond4 = Button(self.frame3, width= 10, height=8, text = "DRESS 4", bg= "yellow", fg = "black", activebackground= "yellow")
        buttond4.grid(row = 1, column = 4)

        buttond5 = Button(self.frame3, width= 10, height=8, text = "DRESS 5", bg= "yellow", fg = "black", activebackground= "yellow")
        buttond5.grid(row = 1, column = 5)


        #t shirt section
        buttont1 = Button(self.frame3, width= 10, height=8, text = "T SHIRT 1", bg= "green", fg = "black", activebackground= "green")
        buttont1.grid(row = 2, column = 1)

        buttont2 = Button(self.frame3, width= 10, height=8, text = "T SHIRT 2", bg= "green", fg = "black", activebackground= "green")
        buttont2.grid(row = 2, column = 2)

        buttont3 = Button(self.frame3, width= 10, height=8, text = "T SHIRT 3", bg= "green", fg = "black", activebackground= "green")
        buttont3.grid(row = 2, column = 3)

        buttont4 = Button(self.frame3, width= 10, height=8, text = "T SHIRT 4", bg= "green", fg = "black", activebackground= "green")
        buttont4.grid(row = 2, column = 4)

        buttont5 = Button(self.frame3, width= 10, height=8, text = "T SHIRT 5", bg= "green", fg = "black", activebackground= "green")
        buttont5.grid(row = 2, column = 5)

        #short section
        buttons1 = Button(self.frame3, width= 10, height=8, text = "SHORT 1", bg= "cyan", fg = "black", activebackground= "cyan")
        buttons1.grid(row = 3, column = 1)

        buttons2 = Button(self.frame3, width= 10, height=8, text = "SHORT 2", bg= "cyan", fg = "black", activebackground= "cyan")
        buttons2.grid(row = 3, column = 2)

        buttons3 = Button(self.frame3, width= 10, height=8, text = "SHORT 3", bg= "cyan", fg = "black", activebackground= "cyan")
        buttons3.grid(row = 3, column = 3)

        buttons4 = Button(self.frame3, width= 10, height=8, text = "SHORT 4", bg= "cyan", fg = "black", activebackground= "cyan")
        buttons4.grid(row = 3, column = 4)

        buttons5 = Button(self.frame3, width= 10, height=8, text = "SHORT 5", bg= "cyan", fg = "black", activebackground= "cyan")
        buttons5.grid(row = 3, column = 5)

        #shoes section
        buttonsh1 = Button(self.frame3, width= 10, height=8, text = "SHOES 1", bg= "magenta", fg = "black", activebackground= "magenta")
        buttonsh1.grid(row = 4, column = 1)

        buttonsh2 = Button(self.frame3, width= 10, height=8, text = "SHOES 2", bg= "magenta", fg = "black", activebackground= "magenta")
        buttonsh2.grid(row = 4, column = 2)

        buttonsh3 = Button(self.frame3, width= 10, height=8, text = "SHOES 3", bg= "magenta", fg = "black", activebackground= "magenta")
        buttonsh3.grid(row = 4, column = 3)

        buttonsh4 = Button(self.frame3, width= 10, height=8, text = "SHOES 4", bg= "magenta", fg = "black", activebackground= "magenta")
        buttonsh4.grid(row = 4, column = 4)

        buttonsh5 = Button(self.frame3, width= 10, height=8, text = "SHOES 5", bg= "magenta", fg = "black", activebackground= "magenta")
        buttonsh5.grid(row = 4, column = 5)

        #accessories section # columns 6-10
        buttona1 = Button(self.frame3, width= 10, height=8, text = "ACCESSORY 1", bg= "orange", fg = "black", activebackground= "orange")
        buttona1.grid(row = 1, column = 6)

        buttona2 = Button(self.frame3, width= 10, height=8, text = "ACCESSORY 2", bg= "orange", fg = "black", activebackground= "orange")
        buttona2.grid(row = 1, column = 7)

        buttona3 = Button(self.frame3, width= 10, height=8, text = "ACCESSORY 3", bg= "orange", fg = "black", activebackground= "orange")
        buttona3.grid(row = 1, column = 8)

        buttona4 = Button(self.frame3, width= 10, height=8, text = "ACCESSORY 4", bg= "orange", fg = "black", activebackground= "orange")
        buttona4.grid(row = 1, column = 9)

        buttona5 = Button(self.frame3, width= 10, height=8, text = "ACCESSORY 5", bg= "orange", fg = "black", activebackground= "orange")
        buttona5.grid(row = 1, column = 10)

        #toys section # columns 6-10
        buttonto1 = Button(self.frame3, width= 10, height=8, text = "TOYS 1", bg= "purple", fg = "black", activebackground= "purple")
        buttonto1.grid(row = 2, column = 6)

        buttonto2 = Button(self.frame3, width= 10, height=8, text = "TOYS 2", bg= "purple", fg = "black", activebackground= "purple")
        buttonto2.grid(row = 2, column = 7)

        buttonto3 = Button(self.frame3, width= 10, height=8, text = "TOYS 3", bg= "purple", fg = "black", activebackground= "purple")
        buttonto3.grid(row = 2, column = 8)

        buttonto4 = Button(self.frame3, width= 10, height=8, text = "TOYS 4", bg= "purple", fg = "black", activebackground= "purple")
        buttonto4.grid(row = 2, column = 9)

        buttonto5 = Button(self.frame3, width= 10, height=8, text = "TOYS 5", bg= "purple", fg = "black", activebackground= "purple")
        buttonto5.grid(row = 2, column = 10)

        #furniture section # columns 6-10
        buttonfur1 = Button(self.frame3, width= 10, height=8, text = "FURNITURE 1", bg= "pink", fg = "black", activebackground= "pink")
        buttonfur1.grid(row = 3, column = 6)

        buttonfur2 = Button(self.frame3, width= 10, height=8, text = "FURNITURE 2", bg= "pink", fg = "black", activebackground= "pink")
        buttonfur2.grid(row = 3, column = 7)

        buttonfur3 = Button(self.frame3, width= 10, height=8, text = "FURNITURE 3", bg= "pink", fg = "black", activebackground= "pink")
        buttonfur3.grid(row = 3, column = 8)

        buttonfur4 = Button(self.frame3, width= 10, height=8, text = "FURNITURE 4", bg= "pink", fg = "black", activebackground= "pink")
        buttonfur4.grid(row = 3, column = 9)

        buttonfur5 = Button(self.frame3, width= 10, height=8, text = "FURNITURE 5", bg= "pink", fg = "black", activebackground= "pink")
        buttonfur5.grid(row = 3, column = 10)

        #cosmetic section # columns 6-10
        buttoncos1 = Button(self.frame3, width= 10, height=8, text = "COSMETIC 1", bg= "sienna", fg = "black", activebackground= "sienna")
        buttoncos1.grid(row = 4, column = 6)

        buttoncos2 = Button(self.frame3, width= 10, height=8, text = "COSMETIC 2", bg= "sienna", fg = "black", activebackground= "sienna")
        buttoncos2.grid(row = 4, column = 7)

        buttoncos3 = Button(self.frame3, width= 10, height=8, text = "COSMETIC 3", bg= "sienna", fg = "black", activebackground= "sienna")
        buttoncos3.grid(row = 4, column = 8)

        buttoncos4 = Button(self.frame3, width= 10, height=8, text = "COSMETIC 4", bg= "sienna", fg = "black", activebackground= "sienna")
        buttoncos4.grid(row = 4, column = 9)

        buttoncos5 = Button(self.frame3, width= 10, height=8, text = "COSMETIC 5", bg= "sienna", fg = "black", activebackground= "sienna")
        buttoncos5.grid(row = 4, column = 10)
        
        buttonDebug= Button(self.frame3,text="DEBUG",command=self.DebugAdd).grid()
        buttonDebug2= Button(self.frame1,text="DEBUG",command=self.DebugAdd2).pack()

root=Tk()
name="DEPRATMENT STORE X"
PosSystem_Start(root,name)



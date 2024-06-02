from tkinter import *

root = Tk()
root.geometry("1300x650")
root.title("DEPARTMENT STORE P.O.S")
root.maxsize(1300, 650)
root.minsize(1300, 650)
root.configure(bg = "light gray")

frame = Frame(root, width = 1300, height = 80, bg = "gray") # top header 
frame.pack()

frame1 = Frame(root, width = 300, height = 520, bg = "white") #display screen for the list of purchases
frame1.place(x= 40, y = 100)

frame2 = Frame(root, width = 300, height = 50, bg = "gray") #frame for the small header in the list
frame2.place(x= 40, y = 100)

frame3 = Frame(root, width = 900, height = 520, bg = "light gray") #frame for the grid in the buttons
frame3.place(x= 380, y= 100)

#labels
Labell = Label(root, text = "BRAND NAME", bg= "gray", fg = "black", font = "Arial 45")
Labell.place(x= 500, y = 0)

Label2 = Label(root, text = "ITEM/S", bg= "gray", fg = "black", font = "Arial 15")
Label2.place(x = 55, y = 100)

Label3 = Label(root, text = "QTY", bg= "gray", fg = "black", font = "Arial 15")
Label3.place(x = 160, y = 100)

Label4 = Label(root, text = "PRICE", bg= "gray", fg = "black", font = "Arial 15")
Label4.place(x = 260, y = 100)

Label5 = Label(root, text = "CATEGORY", bg= "light gray", fg = "black", font = "Arial 8")
Label5.pack(side = TOP)

#LABELS FOR THE ITEMS, QTY, PRICE (IT, QTY, PRI)
LabelIT1= Label(root, text = "PRODUCT 1", bg= "white", fg = "black", font = "Arial 12")
LabelIT1.place(x = 55, y = 150)

LabelQTY1= Label(root, text = "1", bg= "white", fg = "black", font = "Arial 12")
LabelQTY1.place(x = 180, y = 150)

LabelPRI1= Label(root, text = "₱ 299.99", bg= "white", fg = "black", font = "Arial 12")
LabelPRI1.place(x = 260, y = 150)

LabelLINE= Label(root, text = "------------------------------------", bg= "white", fg = "black", font = "Arial 18")
LabelLINE.place(x = 42, y = 500)

LabelTOTAL1= Label(root, text = "TOTAL", bg= "white", fg = "black", font = "Arial 12")
LabelTOTAL1.place(x = 55, y = 520)

LabelPRI2= Label(root, text = "₱ 299.99", bg= "white", fg = "black", font = "Arial 12")
LabelPRI2.place(x = 260, y = 520)

#buttons for special features
spButton1 = Button(root, text = "VOID ORDER", bg = "red", fg= "black", font = "Arial 12", activebackground= "red")
spButton1.place(x = 120, y = 585)

spButton2 = Button(root, text = "CHECK OUT", bg = "green", fg= "black", font = "Arial 12", activebackground= "green")
spButton2.place(x = 230, y = 585)

spFrame = Frame(root, width = 100, height = 520, bg= "light gray")
spFrame.place(x= 1190, y = 100)

spbutton3 = Button(spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
spbutton3.grid(row = 1, column = 1)

spbutton4 = Button(spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
spbutton4.grid(row = 2, column = 1)

spbutton5 = Button(spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
spbutton5.grid(row = 3, column = 1)

spbutton6 = Button(spFrame, width= 10, height=8, text = "SPEC BUTTON", bg= "gray", fg = "black", activebackground= "gray")
spbutton6.grid(row = 4, column = 1)

#food section 
frameFood1 = Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood1.grid(row = 1, column = 1)

buttond1 = Button(frameFood1, width= 10, height=8, text = "FOOD 1", bg= "yellow", fg = "black", activebackground= "yellow")
buttond1.grid(row = 1, column = 1)

buttond2 = Button(frameFood1, width= 10, height=8, text = "FOOD 2", bg= "yellow", fg = "black", activebackground= "yellow")
buttond2.grid(row = 1, column = 2)

buttond3 = Button(frameFood1, width= 10, height=8, text = "FOOD 3", bg= "yellow", fg = "black", activebackground= "yellow")
buttond3.grid(row = 1, column = 3)

buttond4 = Button(frameFood1, width= 10, height=8, text = "FOOD 4", bg= "yellow", fg = "black", activebackground= "yellow")
buttond4.grid(row = 1, column = 4)

buttond5 = Button(frameFood1, width= 10, height=8, text = "FOOD 5", bg= "yellow", fg = "black", activebackground= "yellow")
buttond5.grid(row = 1, column = 5)

#food section
frameFood2 = Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood2.grid(row = 2, column = 1)

buttont1 = Button(frameFood2, width= 10, height=8, text = " FOOD 1", bg= "green", fg = "black", activebackground= "green")
buttont1.grid(row = 1, column = 1)

buttont2 = Button(frameFood2, width= 10, height=8, text = " FOOD 2", bg= "green", fg = "black", activebackground= "green")
buttont2.grid(row = 1, column = 2)

buttont3 = Button(frameFood2, width= 10, height=8, text = " FOOD 3", bg= "green", fg = "black", activebackground= "green")
buttont3.grid(row = 1, column = 3)

buttont4 = Button(frameFood2, width= 10, height=8, text = " FOOD 4", bg= "green", fg = "black", activebackground= "green")
buttont4.grid(row = 1, column = 4)

buttont5 = Button(frameFood2, width= 10, height=8, text = " FOOD 5", bg= "green", fg = "black", activebackground= "green")
buttont5.grid(row = 1, column = 5)

#food section
frameFood3 = Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood3.grid(row = 3, column = 1)

buttons1 = Button(frameFood3, width= 10, height=8, text = "FOOD 1", bg= "cyan", fg = "black", activebackground= "cyan")
buttons1.grid(row = 1, column = 1)

buttons2 = Button(frameFood3, width= 10, height=8, text = "FOOD 2", bg= "cyan", fg = "black", activebackground= "cyan")
buttons2.grid(row = 1, column = 2)

buttons3 = Button(frameFood3, width= 10, height=8, text = "FOOD 3", bg= "cyan", fg = "black", activebackground= "cyan")
buttons3.grid(row = 1, column = 3)

buttons4 = Button(frameFood3, width= 10, height=8, text = "FOOD 4", bg= "cyan", fg = "black", activebackground= "cyan")
buttons4.grid(row = 1, column = 4)

buttons5 = Button(frameFood3, width= 10, height=8, text = "FOOD 5", bg= "cyan", fg = "black", activebackground= "cyan")
buttons5.grid(row = 1, column = 5)

#food section
frameFood4 = Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood4.grid(row = 4, column = 1)

buttonsh1 = Button(frameFood4, width= 10, height=8, text = "FOOD 1", bg= "magenta", fg = "black", activebackground= "magenta")
buttonsh1.grid(row = 1, column = 1)

buttonsh2 = Button(frameFood4, width= 10, height=8, text = "FOOD 2", bg= "magenta", fg = "black", activebackground= "magenta")
buttonsh2.grid(row = 1, column = 2)

buttonsh3 = Button(frameFood4, width= 10, height=8, text = "FOOD 3", bg= "magenta", fg = "black", activebackground= "magenta")
buttonsh3.grid(row = 1, column = 3)

buttonsh4 = Button(frameFood4, width= 10, height=8, text = "FOOD 4", bg= "magenta", fg = "black", activebackground= "magenta")
buttonsh4.grid(row = 1, column = 4)

buttonsh5 = Button(frameFood4, width= 10, height=8, text = "FOOD 5", bg= "magenta", fg = "black", activebackground= "magenta")
buttonsh5.grid(row = 1, column = 5)

#food section
frameFood5 = Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood5.grid(row = 1, column = 2)

buttona1 = Button(frameFood5, width= 10, height=8, text = "FOOD 1", bg= "orange", fg = "black", activebackground= "orange")
buttona1.grid(row = 1, column = 1)

buttona2 = Button(frameFood5, width= 10, height=8, text = "FOOD 2", bg= "orange", fg = "black", activebackground= "orange")
buttona2.grid(row = 1, column = 2)

buttona3 = Button(frameFood5, width= 10, height=8, text = "FOOD 3", bg= "orange", fg = "black", activebackground= "orange")
buttona3.grid(row = 1, column = 3)

buttona4 = Button(frameFood5, width= 10, height=8, text = "FOOD 4", bg= "orange", fg = "black", activebackground= "orange")
buttona4.grid(row = 1, column = 4)

buttona5 = Button(frameFood5, width= 10, height=8, text = "FOOD 5", bg= "orange", fg = "black", activebackground= "orange")
buttona5.grid(row = 1, column = 5)

#food section 
frameFood6 = Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood6.grid(row = 2, column = 2)

buttonto1 = Button(frameFood6, width= 10, height=8, text = "FOOD 1", bg= "purple", fg = "black", activebackground= "purple")
buttonto1.grid(row = 1, column = 1)

buttonto2 = Button(frameFood6, width= 10, height=8, text = "FOOD 2", bg= "purple", fg = "black", activebackground= "purple")
buttonto2.grid(row = 1, column = 2)

buttonto3 = Button(frameFood6, width= 10, height=8, text = "FOOD 3", bg= "purple", fg = "black", activebackground= "purple")
buttonto3.grid(row = 1, column = 3)

buttonto4 = Button(frameFood6, width= 10, height=8, text = "FOOD 4", bg= "purple", fg = "black", activebackground= "purple")
buttonto4.grid(row = 1, column = 4)

buttonto5 = Button(frameFood6, width= 10, height=8, text = "FOOD 5", bg= "purple", fg = "black", activebackground= "purple")
buttonto5.grid(row = 1, column = 5)

#food section
frameFood7 = Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood7.grid(row = 3, column = 2)

buttonfur1 = Button(frameFood7, width= 10, height=8, text = "FOOD 1", bg= "pink", fg = "black", activebackground= "pink")
buttonfur1.grid(row = 1, column = 1)

buttonfur2 = Button(frameFood7, width= 10, height=8, text = "FOOD 2", bg= "pink", fg = "black", activebackground= "pink")
buttonfur2.grid(row = 1, column = 2)

buttonfur3 = Button(frameFood7, width= 10, height=8, text = "FOOD 3", bg= "pink", fg = "black", activebackground= "pink")
buttonfur3.grid(row = 1, column = 3)

buttonfur4 = Button(frameFood7, width= 10, height=8, text = "FOOD 4", bg= "pink", fg = "black", activebackground= "pink")
buttonfur4.grid(row = 1, column = 4)

buttonfur5 = Button(frameFood7, width= 10, height=8, text = "FOOD 5", bg= "pink", fg = "black", activebackground= "pink")
buttonfur5.grid(row = 1, column = 5)

#food section
frameFood8= Frame(frame3, width = 400, height = 130, bg = "light gray")
frameFood8.grid(row = 4, column = 2)

buttoncos1 = Button(frameFood8, width= 10, height=8, text = "FOOD", bg= "sienna", fg = "black", activebackground= "sienna")
buttoncos1.grid(row = 1, column = 1)

buttoncos2 = Button(frameFood8, width= 10, height=8, text = "FOOD 2", bg= "sienna", fg = "black", activebackground= "sienna")
buttoncos2.grid(row = 1, column = 2)

buttoncos3 = Button(frameFood8, width= 10, height=8, text = "FOOD 3", bg= "sienna", fg = "black", activebackground= "sienna")
buttoncos3.grid(row = 1, column = 3)

buttoncos4 = Button(frameFood8, width= 10, height=8, text = "FOOD 4", bg= "sienna", fg = "black", activebackground= "sienna")
buttoncos4.grid(row = 1, column = 4)

buttoncos5 = Button(frameFood8, width= 10, height=8, text = "FOOD 5", bg= "sienna", fg = "black", activebackground= "sienna")
buttoncos5.grid(row = 1, column = 5)




root.mainloop()



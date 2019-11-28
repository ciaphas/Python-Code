from tkinter import *
import backend
from shutil import copyfile
import barcode

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def add_command():
    backend.add_shipment(tkvar.get(),firstname_title.get(),surname_title.get(),addr1_title.get(),addr2_title.get(),town_title.get(),pcode_title.get(),service.get(),con_title.get(),quantity_title.get(),prod.get())
    list1.delete(0,END)
    list1.insert(END,(tkvar.get(),firstname_title.get(),surname_title.get(),addr1_title.get(),addr2_title.get(),town_title.get(),pcode_title.get(),service.get(),con_title.get(),quantity_title.get(),prod.get()))

def search_command():
    list1.delete(0,END)
    for row in backend.search(tkvar.get(),firstname_title.get(),surname_title.get(),addr1_title.get(),addr2_title.get(),town_title.get(),pcode_title.get(),service.get(),con_title.get(),quantity_title.get(),prod.get()):
        list1.insert(END,row)

def export_command():
    backend.export()


window=Tk()

window.wm_title("Consignor")

tkvar=StringVar()
choices = {'Mr', 'Miss', 'Ms','Dr','Mrs'}
popupMenu = OptionMenu(window,tkvar, *choices)
tkvar.set('Mr')
Label(window, text="Title").grid(row=0, column=0)
popupMenu.grid(row=0, column=1)

l1=Label(window,text="First Name")
l1.grid(row=0,column=2)
firstname_title=StringVar()
e1=Entry(window,textvariable=firstname_title)
e1.grid(row=0,column=3)

l1a=Label(window,text="Surname")
l1a.grid(row=0,column=4)
surname_title=StringVar()
e1a=Entry(window,textvariable=surname_title)
e1a.grid(row=0,column=5)

l2=Label(window,text="Address1")
l2.grid(row=1,column=2)
addr1_title=StringVar()
e2=Entry(window,textvariable=addr1_title)
e2.grid(row=1,column=3)

l2a=Label(window,text="Address2")
l2a.grid(row=2,column=2)
addr2_title=StringVar()
e2a=Entry(window,textvariable=addr2_title)
e2a.grid(row=2,column=3)

l3=Label(window,text="Town")
l3.grid(row=3,column=2)
town_title=StringVar()
e3=Entry(window,textvariable=town_title)
e3.grid(row=3,column=3)

l3=Label(window,text="Post Code")
l3.grid(row=4,column=2)
pcode_title=StringVar()
e3=Entry(window,textvariable=pcode_title)
e3.grid(row=4,column=3)

service=StringVar()
choices = {'B410', 'B412', 'Next Day','Two Day'}
popupMenu = OptionMenu(window,service, *choices)
service.set('B410')
Label(window, text="Service").grid(row=0, column=6)
popupMenu.grid(row=0, column=7)

l3=Label(window,text="Quantity")
l3.grid(row=1,column=4)
quantity_title=IntVar()
e3=Entry(window,textvariable=quantity_title)
e3.grid(row=1,column=5)

l4=Label(window,text="Con Number")
l4.grid(row=2,column=4)
con_title=IntVar()
e4=Entry(window,textvariable=con_title)
e4.grid(row=2,column=5)

l5=Label(window,text="Product Code")
l5.grid(row=3,column=4)
prod=IntVar()
e5=Entry(window,textvariable=prod)
e5.grid(row=3,column=5)

list1=Listbox(window, height=12,width=40)
list1.grid(row=6,column=3,rowspan=12,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=7,column=5,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All", width=12,command=view_command)
b1.grid(row=7,column=5)

b2=Button(window,text="Search Entry", width=12,command=search_command)
b2.grid(row=8,column=5)

b3=Button(window,text="Add Entry", width=12,command=add_command)
b3.grid(row=6,column=5)

b4=Button(window,text="Export Data", width=12,command=export_command)
b4.grid(row=9,column=5)



window.mainloop()

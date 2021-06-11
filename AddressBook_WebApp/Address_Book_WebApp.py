# import library
from tkinter import *

# initialize window
root = Tk()
root.geometry('800x600')
root.config(bg='SlateGray3')
root.title('AddressBook-WebApplication')
root.resizable(0, 0)
contactlist = [
    ["Dave","Smith","123 main st.","seattle","wa","43"],
    ["Alice","Smith","123 Main St.","Seattle","WA","45"],
    ["bob","Williams","234 2nd Ave.","Tacoma","WA","26"],
    ["Carol","Johnson","234 2nd Ave","Seattle","WA","67"],
    ["Tom","Bombadillo","1212 Maple Street","Florida","GA","520"],
    ["Jimbo","Jones","82 Pine Street","Atlanta","GA","2"],
    ["Jackie","Jones","82 Pine Street","Atlanta","GA","6"],
    ["Tommy","Jones","82 Pine Street","Atlanta","GA","29"],
    ["tammy","Jones","82 Pine Street","Atlanta","GA","27"],
    ["EvE","Smith","234 2nd Ave.","Tacoma","WA","25"],
    ["Frank","Jones","234 2nd Ave.","Tacoma","FL","23"],
    ["george","Brown","345 3rd Blvd., Apt. 200","Seattle","WA","19"],
    ["Helen","Brown","345 3rd Blvd. Apt. 200","Seattle","WA","18"],
    ["Ian","smith","123 main st ","Seattle","Wa","18"],
    ["Jane","Smith","123 Main St.","Seattle","WA","13"],

]

FirstName = StringVar()
LastName = StringVar()
Address = StringVar()
City = StringVar()
Country = StringVar()
AreaCode = StringVar()

# create frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=50, width= 40)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


#####function to get select value

def Selected():
    return int(select.curselection()[0])


##function to add new contact
def AddContact():
    contactlist.append([FirstName.get(), LastName.get(), Address.get(), City.get(), Country.get(), AreaCode.get()])
    Select_set()


##function to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [FirstName.get(), LastName.get(), Address.get(), City.get(), Country.get(), AreaCode.get()]
    Select_set()


##function to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()


##function to view selected contact(first select then click on view button)
def VIEW():
    FIRSTNAME, LASTNAME , ADDRESS, CITY, COUNTRY , AREACODE = contactlist[Selected()]
    FirstName.set(FIRSTNAME)
    LastName.set(LASTNAME)
    Address.set(ADDRESS)
    City.set(CITY)
    Country.set(COUNTRY)
    AreaCode.set(AREACODE)


##function to exit the window
def EXIT():
    root.destroy()


##empty name and number field
def RESET():
    FirstName.set('')
    LastName.set('')
    Address.set('')
    City.set('')
    Country.set('')
    AreaCode.set('')


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for FirstName, LastName, Address, City, Country, AreaCode in contactlist:
        select.insert(END, FirstName)

Select_set()

####define buttons #####labels and entry widget####
Label(root, text='FIRST NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=FirstName).place(x=150, y=20)
Label(root, text='LAST NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=LastName).place(x=150, y=70)
Label(root, text='ADDRESS', font='arial 12 bold', bg='SlateGray3').place(x=30, y=120)
Entry(root, textvariable=Address).place(x=150, y=120)
Label(root, text='CITY', font='arial 12 bold', bg='SlateGray3').place(x=30, y=170)
Entry(root, textvariable=City).place(x=150, y=170)
Label(root, text='COUNTRY', font='arial 12 bold', bg='SlateGray3').place(x=30, y=220)
Entry(root, textvariable=Country).place(x=150, y=220)
Label(root, text='AREACODE', font='arial 12 bold', bg='SlateGray3').place(x=30, y=270)
Entry(root, textvariable=AreaCode).place(x=150, y=270)

Button(root, text=" ADD", font='arial 12 bold', bg='SlateGray4', command=AddContact).place(x=50, y=380)
Button(root, text="EDIT", font='arial 12 bold', bg='SlateGray4', command=EDIT).place(x=120, y=380)
Button(root, text="DELETE", font='arial 12 bold', bg='SlateGray4', command=DELETE).place(x=190, y=380)
Button(root, text="VIEW", font='arial 12 bold', bg='SlateGray4', command=VIEW).place(x=290, y=380)
Button(root, text="EXIT", font='arial 12 bold', bg='tomato', command=EXIT).place(x=210, y=480)
Button(root, text="RESET", font='arial 12 bold', bg='SlateGray4', command=RESET).place(x=370, y=380)

root.mainloop()


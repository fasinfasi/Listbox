
from tkinter import *

def submit():
    items = []
    for food in listbox.curselection():
        items.insert(food,listbox.get(food))
    
    print("You have ordered : ")
    for i in items:
        print(i)

def add():
        print("You added :",entry.get())
        listbox.insert(listbox.size(),entry.get())
        listbox.config(height=listbox.size())
        
def deletebutton():
    delete_item = []
    
    for index in reversed(listbox.curselection()):
        delete_item.insert(index,listbox.get(index)) 
        listbox.delete(index)
    listbox.config(height=listbox.size())
        
    print("Deleted item: ")
    for d in delete_item:
        print(d)

window = Tk()
window.title("Food Listbox")

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("constantia",15),
                  selectmode=MULTIPLE
                  )
listbox.pack()
listbox.insert(1,"Pizza")
listbox.insert(2,"Hotdog")
listbox.insert(3,"sandwich")
listbox.insert(4,"Hamburger")
listbox.insert(5,"Donut")

listbox.config(height=listbox.size())

entry = Entry(window)
entry.config(fg="red")
entry.pack()

submit = Button(window,text="Submit",command=submit)
submit.pack()

add = Button(window,text="Add",command=add)
add.pack()

deletebutton = Button(window,text="Delete",command=deletebutton)
deletebutton.pack()

window.mainloop()
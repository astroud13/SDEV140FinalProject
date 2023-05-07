"""
Author:  Austin Stroud
Date written: 05/6/2023
Assignment:   Module 8 Final Project
Short Desc: A GUI program takes input from the user and tracks
prizes selected for participation in a library reading program. 
"""
#import tkinter, imaging library, webbrowser, and messagebox
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox 
import webbrowser


#Creates a tkinter window object and sets its size and title
reading = Tk()
reading.geometry("700x500")
reading.title("Summer reading prize app")

#Creates labels and entry boxes to collect user information 
name_label = Label(reading, text="What is your name? ")
name_label.grid(row=0, column=0)

name_entry = Entry(reading, width=30)
name_entry.grid(row=0, column=1)

address_label = Label(reading, text="What is your address? ")
address_label.grid(row=1, column=0)

address_entry = Entry(reading, width=30)
address_entry.grid(row=1, column=1)

phone_label = Label(reading, text="What is your phone number? ")
phone_label.grid(row=2, column=0)

phone_entry = Entry(reading, width=30)
phone_entry.grid(row=2, column=1)

email_label = Label(reading, text="What is your email address? ")
email_label.grid(row=3, column=0)

email_entry = Entry(reading, width=30)
email_entry.grid(row=3, column=1)

# Creates a list of possible prizes and a listbox to display them
my_reading_list = ["ink pen", "magnet", "canvas bag", "button", "bookmark"]
my_reading_list.insert(0, "select a participation prize")
print(my_reading_list)

reading_list = Listbox(reading, bg="yellow", fg="red")
reading_list.grid(row=4, column=1)

#Populates the listbox with the possible prizes
for item in my_reading_list:
    reading_list.insert(END, item)

#Defines a function to add selected prizes to a label 
def add_reading():
    result = ""
    for item in reading_list.curselection():
        result = result + str(reading_list.get(item)) + "\n"

        add_lbl.config(text="Your Prize Selection: " + "\n" + result)

#Creates a label to display the user's selected prizes
add_lbl = Label(reading, text="")
add_lbl.grid(row=5, column=1) 

#Creates a button to trigger the add_reading function
add_button = Button(reading, text="Add Prize" , command= add_reading)
add_button.grid(row=5, column=0)

#Defines a function to display the user's information upon clicking a checkout
def check():
    text1 = name_entry.get()
    new_lbl = Label(reading, text="Name: " + text1)
    new_lbl.grid(row=5, column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(reading, text="Address: " + text2)
    new_lbl2.grid(row=6, column=2)

    text3 = phone_entry.get()
    new_lb3 = Label(reading, text="Phone Number: " + text3)
    new_lb3.grid(row=7, column=2)

    text4 = email_entry.get()
    new_lb4 = Label(reading, text="Email Address: " + text4)
    new_lb4.grid(row=8, column=2)

#Creates a button to trigger the check function and display user's information
check_button = Button(reading, text="Checkout Prize" , command=check)
check_button.grid(row=6, column=0)

#Defines a function to remove selected prizes from the listbox
def deleteme():
    reading_list.delete(0,1)

del_button = Button(reading, text="Delete Prize", command=deleteme)
del_button.grid(row=7, column=0)

#Option menu to select a grand prize drawing
drawingprizes = StringVar()
drawingprizes.set("Choose a grand prize drawing.")

drawingprizes = OptionMenu(reading, drawingprizes, "Indians Tickets", "Colts Tickets", "State Park Pass", "Museum Pass", "State Fair Pass", "Gas Card")
drawingprizes.grid(row=8, column=0)

#Code for the images in the application 
reading_pic = ImageTk.PhotoImage(Image.open("books2.jpg"))
pic_lbl = Label(reading, image=reading_pic, text="books")
pic_lbl.grid(row=1, column=6)

reading_pic2 = ImageTk.PhotoImage(Image.open("ribbon.png"))
pic_lbl = Label(reading, image=reading_pic2, text="ribbon")
pic_lbl.grid(row=8, column=1)

# Defines a function to access the GitHub Repository in a web browser window
def open_github():
    webbrowser.open_new('repositorylink.html')

button = Button(reading, text="Open GitHub Repository", command=open_github)
button.grid(row=9, column=0)


#Defines a function to exit the application 
def exit():
    answer = messagebox.askyesno("Hi", "Are you sure you want to exit? ")
    if answer == 1:
        reading.destroy()
    else:
        return

exit_button = Button(reading, text="Exit", command=exit)
exit_button.grid(row=4, column=6)

#Start the main event loop
reading.mainloop()

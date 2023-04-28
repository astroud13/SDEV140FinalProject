"""
Author:  Austin Stroud
Date written: 04/27/2023
Assignment:   Module 8 Final Project
Short Desc: A GUI program takes input from the user and tracks
prizes selected for participation in a library reading program. 
"""
#import tkinter 

from tkinter import *

#Settings for the app

reading = Tk()
reading.geometry("600x500")
reading.title("Summer reading prize app")

#Gather user inputs

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

# Create first prize list
my_reading_list = ["ink pen", "magnet", "canvas bag", "button", "bookmark"]

reading_list = Listbox(reading, selectmode=MULTIPLE, bg="yellow", fg="red")
reading_list.grid(row=4, column=1)

for item in my_reading_list:
    reading_list.insert(END, item)

def add_reading():
    result = ""
    for item in reading_list.curselection():
        result = result + str(reading_list.get(item)) + "\n"

        add_lbl.config(text="Your Prize Selection: " + "\n" + result)

add_lbl = Label(reading, text="")
add_lbl.grid(row=5, column=1) 

add_button = Button(reading, text="Add Prize" , command= add_reading)
add_button.grid(row=5, column=0)

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

check_button = Button(reading, text="Checkout Prize" , command=check)
check_button.grid(row=6, column=0)

def deleteme():
    reading_list.delete(0,5)

del_button = Button(reading, text="Delete Prize", command=deleteme)
del_button.grid(row=7, column=0)

drawingprizes = StringVar()
drawingprizes.set("Choose a grand prize drawing.")

drawingprizes = OptionMenu(reading, drawingprizes, "Indians Tickets", "Colts Tickets", "State Park Pass", "Museum Pass", "State Fair Pass", "Gas Card")
drawingprizes.grid(row=8, column=0)
reading.mainloop()


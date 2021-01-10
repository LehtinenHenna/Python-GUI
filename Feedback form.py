# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:53:44 2020

@author: henna
"""

#Simple feedback form that writes the submitted info to a csv file. It will create a csv file named "feedback"
# unless there is already a csv file with that name in the same folder with the program.

from tkinter import *

root = Tk()
root.geometry("1000x500")   #size of the window
root.title("Product Feedback Form") #title of the window
root.configure(bg="#77978a")    # backround color of the window

def submit_button():    # when the submit button is pressed, the program will retrieve the information from the entry boxes
    firstname_info = firstname_entry.get()
    lastname_info = lastname_entry.get()
    email_info = email_entry.get()
    product_info = product_entry.get()
    describe_info = describe_entry.get()
 
#save the submitted data to a separate file "feedback.txt" if all the fields are filled correctly .
    if len(firstname_info)>0 and len(lastname_info)>0 and len(email_info)>0 and len(product_info)==6 and len(describe_info)>0:
        file = open("feedback.csv", "a")
        file.write("\n"+firstname_info+",")
        file.write(lastname_info+",")
        file.write(email_info+",")
        file.write(product_info+",")
        file.write(describe_info)
        file.close()
        print("Product feedback by", firstname_info, lastname_info, "has been submitted successfully.")
        
    # next, empty all the entry boxes
        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        email_entry.delete(0, END)
        product_entry.delete(0, END)
        describe_entry.delete(0, END)
        
        success_label = Label(root, text="Thank you for your feedback. We will be in touch with you within 7 business days.", bg="white", fg="#000069")
        success_label.place(x=60, y=275)

    else:
        invalid = Label(root, text="Your input is invalid. Please check that all fields are filled out properly.                     ", bg="white", fg="#df2828")
        invalid.place(x=60, y=275)
        
        
firstname = StringVar()
lastname = StringVar()
email = StringVar()
product = IntVar()
describe = StringVar()

#define widgets
title_label = Label(root, text="Product Feedback Form", font=("Arial", 20))

firstname_label = Label(root, text="Enter first name:")
firstname_entry = Entry(root, width=50, borderwidth=5, textvariable=firstname)

lastname_label = Label(root, text="Enter last name:")
lastname_entry = Entry(root, width=50, borderwidth=5, textvariable=lastname)

email_label = Label(root, text="Enter your email address:")
email_entry = Entry(root, width=50, borderwidth=5, textvariable=email)

product_label= Label(root, text="Enter product code (6 digit number):")
product_entry = Entry(root, width=50, borderwidth=5, textvariable=product)


describe_label = Label(root, text="Describe feedback. Max number of characters is 100.")
describe_entry = Entry(root, width=165, borderwidth=5, textvariable=describe)

submit_button = Button(root, text="Submit", command=submit_button)





#place widgets on the screen
title_label.place(x=0, y=0)
firstname_label.place(x=0, y= 50)
firstname_entry.place(x=0, y= 75)
lastname_label.place(x=400, y= 50)
lastname_entry.place(x=400, y= 75)
email_label.place(x=0, y= 125)
email_entry.place(x=0, y= 150)
product_label.place(x=400, y= 125)
product_entry.place(x=400, y= 150)

describe_label.place(x=0, y= 200)
describe_entry.place(x=0, y= 225)
submit_button.place(x=0, y= 275)

root.mainloop() 

#Import the required Libraries
from ipaddress import ip_address
from lib2to3.pgen2.token import NEWLINE
from tkinter import *
import autopy
# from tkinter import tk
import tkinter as tk


def get_details():
    details=open("details.txt",'w')
    details.write(device_name.get())
    details.write('\n')
    details.write(reciever_IP.get() )
    details.write('\n')
    details.write(folder_name.get())
    details.close()

#Create an instance of Tkinter frame
win= Tk()

titl = tk.Label(win, bg="black", relief="flat", bd=10, font=("arial", 35))
titl.pack(fill=X)

title1=tk.Label(win, text = "Enter", bg = "black", fg = "dark orange", font=("arial", 27),borderwidth=0)
title1.place(x=605,y=12)

title2=tk.Label(win, text = "your", bg = "black", fg = "white", font=("arial", 27),borderwidth=0)
title2.place(x=702,y=12)

title3=tk.Label(win, text = "Details", bg = "black", fg = "green", font=("arial", 27),borderwidth=0)
title3.place(x=780,y=12)

#Set the geometry of Tkinter frame
# width,height=autopy.screen.size()
win.geometry("1000x1000")


name = tk.Label(
        win,
        text="Username",
        width=10,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="dark orange",
        borderwidth=0,
    )
name.place(x=500, y=200)

#Create an Entry widget to accept User Input
device_name= Entry(win,
        width=17,
        bd=5,
        validate="key",
        bg="grey",
        fg="red",
        # relief=RIDGE,
        font=("times", 25, "bold"),
        borderwidth=1,
        relief="groove")
device_name.focus_set()

device_name.place(x=610,y=200)


IP_address = tk.Label(
        win,
        text="Enter IP",
        width=10,
        height=2,
        
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="white",
        borderwidth=0,

    )
IP_address.place(x=500, y=270)


reciever_IP= Entry(win,
        width=17,
        bd=5,
        validate="key",
        bg="grey",
        fg="red",
        # relief=RIDGE,
        font=("times", 25, "bold"),
        borderwidth=1,
        relief="groove")
reciever_IP.focus_set()
reciever_IP.place(x=610,y=270) 


folder= tk.Label(
        win,
        text="Folder Name",
        width=10,
        height=2,
        
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
folder.place(x=500, y=340)

folder_name= Entry(win,
        width=17,
        bd=5,
        validate="key",
        bg="grey",
        fg="red",
        # relief=RIDGE,
        font=("times", 25, "bold"),
        borderwidth=1,
        relief="groove")
folder_name.focus_set()
folder_name.place(x=610,y=340)


                                           

#Create a Button to validate Entry Widget

submit = tk.Button(
        win,
        text="Submit",
        command=get_details,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="red",
        height=0,
        width=10,
        # relief=RIDGE,
        borderwidth=0
    )
submit.place(x=680, y=410)


win.mainloop()

# Reading from the file 

f=open("details.txt",'r')
l=f.readlines()
print(l[0],l[1],l[2])



# sudo mount.cifs -o username=(window_username) //ip_address/folder_share_name ubuntu_destination_folder



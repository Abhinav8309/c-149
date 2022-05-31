from tkinter import *
import random

root=Tk()
root.title("Lucky ticket Wheel")
root.geometry("400x400")

tickets=['n','y','t','h']
print(tickets)
label_tickets=Label(root)

def lucky_tickets():
    randomnumber=random.randint(0,3)
    print(randomnumber)
    randomLuckytickets=tickets[randomnumber]
    print("Your Lucky tickets Is : "+ randomLuckytickets )
    label_tickets['text']="Your genereted letter is : "+ randomLuckytickets 


btn=Button(root,text="Genreted letters",command=lucky_tickets)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_tickets.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
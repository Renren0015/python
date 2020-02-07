from tkinter import *
import time

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    number_info = str(number.get())
    purpose_info = purpose.get()
    time_info = time.get()
    time1_info = time1.get()
    selection = var.get()
    
    print(firstname_info.capitalize(), lastname_info.capitalize(), number_info)

    file = open(firstname_info.capitalize() + '.txt', 'w')
    file.write('Firstname: ' + firstname_info.capitalize() + '\n')
    file.write('Lastname: ' + lastname_info.capitalize() + '\n')
    file.write('Student number: ' + number_info + '\n')
    file.write('Purpose: ' + purpose_info.capitalize() + '\n')
    file.write('Time in: ' + time_info + ':' + time1_info + ' ' + selection + '\n')
    file.write('Time out: ' + b)
    file.close()
    print(firstname_info.capitalize(), " has been registered successfully")

screen = Tk()
screen.geometry("600x510")
screen.title("Saint Jude College")
heading = Label(text="Saint Jude College", bg="#4a8b2c", fg="white", width="500", height="3")
heading.pack()

photo = PhotoImage(file="phinma.png")
photos = Label(screen, image=photo)
photos.pack()

a = time.localtime()
b = time.asctime(a)
firstname_text = Label(text="Firstname")
lastname_text = Label(text="Lastname")
number_text = Label(text="Student number")
purpose_text = Label(text="Purpose")
time_text = Label(text="Time in")
time1_text = Label(text=":")

var = StringVar()

am = Radiobutton(screen, text="AM", variable=var, value='AM')
pm = Radiobutton(screen, text="PM", variable=var, value='PM')

firstname_text.place(x=15, y=80)
lastname_text.place(x=15, y=140)
number_text.place(x=15, y=200)
purpose_text.place(x=15, y=260)
time_text.place(x=15, y=320)
time1_text.place(x=35, y=340)
am.place(x=70, y=340)
pm.place(x=115, y=340)

firstname = StringVar()
lastname = StringVar()
number = IntVar()
purpose = StringVar()
time = StringVar()
time1 = StringVar()

firstname_entry = Entry(textvariable=firstname, width="30")
lastname_entry = Entry(textvariable=lastname, width="30")
number_entry = Entry(textvariable=number, width="30")
purpose_entry = Entry(textvariable=purpose, width="30")
time_entry = Entry(textvariable=time, width="2")
time1_entry = Entry(textvariable=time1, width="2")

firstname_entry.place(x=15, y=100)
lastname_entry.place(x=15, y=160)
number_entry.place(x=15, y=220)
purpose_entry.place(x=15, y=280)
time_entry.place(x=15, y=340)
time1_entry.place(x=50, y=340)

register = Button(screen, text="Register", width="30", height="2", command=save_info, bg="#4a8b2c", fg="white")
register.place(x=15, y=430)

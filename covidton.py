from tkinter import *
from tkinter import messagebox
import sqlite3
import sys
import time
top = Tk()

top.geometry("800x800")
top.title("covid detection offline Form")
Fullname=StringVar()
var1= IntVar()
E=StringVar()
c=StringVar()
v = IntVar()
g=StringVar()
d=StringVar()
def database():
   name1=Fullname.get()
   duration=E.get()
   disease=v.get()
   age=var1.get()
   country=c.get()
   gender=g.get()
   date=d.get()
   conn = sqlite3.connect('Covid Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS patient (Fullname TEXT,age TEXT,duration TEXT,disease TEXT,country TEXT,gender TEXT,date TEXT)')
   cursor.execute('INSERT INTO patient (FullName,age,duration,disease,country,gender,date) VALUES(?,?,?,?,?,?,?)',(name1,age,duration,disease,country,gender,date))
   conn.commit()


name = Label(top, text = "FullName", fg ="blue").place(x = 300,y = 220)

age = Label(top, text = "Age", fg = "blue").place(x = 300, y = 280)

dur = Label(top, text = "How long have you been suffering", fg = "blue").place(x = 300, y = 315)

e1 = Entry(top,textvar=Fullname).place(x = 520, y = 225)


e2 = Entry(top,textvar=var1).place(x = 520, y =285)


e3 = Entry(top,textvar=E).place(x = 520, y = 315)

Radiobutton(top, text="Male",padx = 5, variable=g, value=1).place(x=295,y=250)
Radiobutton(top, text="Female",padx = 20, variable=g, value=2).place(x=350,y=250)
Radiobutton(top, text="Others",padx = 20, variable=g, value=3).place(x=440,y=250)

def selection():
    print(v.get())
    selection = "You Have selected" + str(radio.get())
    label.config(text = selection)
v.set(None)
radio = IntVar()
lab = Label(text="COVID 19 Tester", bg="red")
lab.pack(anchor= W)
lbl = Label(text = "Symptoms:")
lbl.pack(anchor= W )
R1 = Radiobutton(top, text="Fever", variable=v, value=1,
                  command=selection)
R1.pack(anchor= W)
print(R1)
R2 = Radiobutton(top, text="Fatigue", variable=v, value=2,
                  command=selection)
R2.pack( anchor = W )
print(R2)
R3 = Radiobutton(top, text="Dry Cough", variable=v, value=3,
                  command=selection)
R3.pack( anchor = W)
print(R3)
R4 = Radiobutton(top, text="Loss of Appetite", variable=v, value=4,
                  command=selection)
R4.pack( anchor = W)
R5 = Radiobutton(top, text="Body Aches", variable=v, value=5,
                  command=selection)
R5.pack( anchor = W)
R6 = Radiobutton(top, text="Shortness of breath", variable=v, value=6,
                  command=selection)
R6.pack( anchor = W)
R7 = Radiobutton(top, text="Mucus or Phlegm", variable=v, value=7,
                  command=selection)
R7.pack( anchor = W)
R8 = Radiobutton(top, text="Sore Throat", variable=v, value=8,
                  command=selection)
R8.pack( anchor = W)
R9 = Radiobutton(top, text="Head Ache", variable=v, value=9,
                  command=selection)
R9.pack( anchor = W)
R10 = Radiobutton(top, text="Diarrhea", variable=v, value=10,
                  command=selection)
R10.pack( anchor = W)
R11 = Radiobutton(top, text="Constant pain or pressure in the chest", variable=v, value=11,
                  command=selection)
R11.pack( anchor = W)
R12 = Radiobutton(top, text="Bluish Lips Or Face", variable=v, value=12,
                  command=selection)
R12.pack( anchor = W)
R13 = Radiobutton(top, text="Sudden Confusion", variable=v, value=13,
                  command=selection)
R13.pack( anchor = W)

"""def covid(): #mypolls
    def proceed():
        global plname
        plname=psel.get()
        if plname=='-select-':
            return messagebox.showerror('Error','select options')
        else:
            mpolls.destroy()
            pollpage()
    cursor.execute('select name')
    data=cursor.fetchall()
    pollnames=['-select-']
    for i in range(len(data)):
        data1=data[i]
        ndata=data1[0]
        pollnames.append(ndata)
    psel=StringVar()
    mpolls=Toplevel()
    mpolls.geometry('270x200')
    Label(mpolls,text='Select',font='Helvetica 12 bold').grid(row=1,column=3)
    select=ttk.Combobox(mpolls,values=pollnames,state='readonly',textvariable=psel)
    select.grid(row=2,column=3)
    select.current(0)
    Button(mpolls,text='Proceed',command=proceed).grid(row=2,column=4)"""
#Button(top,text='data',command=covid).grid(row=4,column=2)
from PIL import ImageTk,Image
canvas=Canvas(top,width=10000,height=10000)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\yesh\\Desktop\\h\\112.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

a=['north america', 'europe', 'asia', 'south america', 'oceania', 'africa', 'world', 'usa', 'spain', 'italy', 'france', 'germany', 'uk', 'turkey', 'iran', 'russia', 'brazil', 'belgium', 'canada', 'netherlands', 'switzerland', 'india', 'portugal', 'ecuador', 'peru', 'ireland', 'sweden', 'austria', 'israel', 'saudi arabia', 'mexico', 'japan', 'singapore', 'chile', 'pakistan', 'poland', 's. korea', 'romania', 'belarus', 'qatar', 'uae', 'indonesia', 'denmark', 'ukraine', 'serbia', 'norway', 'philippines', 'czechia', 'australia', 'dominican republic', 'malaysia', 'panama', 'bangladesh', 'colombia', 'finland', 'south africa', 'egypt', 'morocco', 'luxembourg', 'argentina', 'algeria', 'moldova', 'thailand', 'kuwait', 'kazakhstan', 'bahrain', 'greece', 'hungary', 'croatia', 'oman', 'uzbekistan', 'iceland', 'iraq', 'armenia', 'estonia', 'azerbaijan', 'bosnia and herzegovina', 'afghanistan', 'new zealand', 'cameroon', 'lithuania', 'slovenia', 'slovakia', 'north macedonia', 'cuba', 'ghana', 'bulgaria', 'nigeria', 'ivory coast', 'hong kong', 'djibouti', 'guinea', 'tunisia', 'bolivia', 'cyprus', 'latvia', 'andorra', 'albania', 'diamond princess', 'lebanon', 'costa rica', 'niger', 'kyrgyzstan', 'burkina faso', 'senegal', 'honduras', 'uruguay', 'channel islands', 'san marino', 'palestine', 'georgia', 'malta', 'jordan', 'guatemala', 'taiwan', 'sri lanka', 'drc', 'réunion', 'mayotte', 'kenya', 'mauritius', 'somalia', 'mali', 'montenegro', 'venezuela', 'isle of man', 'tanzania', 'jamaica', 'el salvador', 'vietnam', 'paraguay', 'equatorial guinea', 'congo', 'faeroe islands', 'rwanda', 'sudan', 'gabon', 'martinique', 'guadeloupe', 'myanmar', 'brunei', 'maldives', 'gibraltar', 'ethiopia', 'cambodia', 'madagascar', 'liberia', 'trinidad and tobago', 'french guiana', 'aruba', 'bermuda', 'monaco', 'togo', 'cabo verde', 'zambia', 'sierra leone', 'liechtenstein', 'barbados', 'uganda', 'sint maarten', 'bahamas', 'guyana', 'haiti', 'cayman islands', 'mozambique', 'libya', 'french polynesia', 'benin', 'guinea-bissau', 'nepal', 'macao', 'syria', 'eswatini', 'chad', 'eritrea', 'saint martin', 'mongolia', 'malawi', 'zimbabwe', 'angola', 'antigua and barbuda', 'timor-leste', 'botswana', 'laos', 'belize', 'fiji', 'new caledonia', 'curaçao', 'car', 'dominica', 'namibia', 'grenada', 'saint kitts and nevis', 'saint lucia', 'st. vincent grenadines', 'falkland islands', 'nicaragua', 'burundi', 'montserrat', 'turks and caicos', 'greenland', 'seychelles', 'gambia', 'suriname', 'ms zaandam', 'vatican city', 'papua new guinea', 'mauritania', 'bhutan', 'st. barth', 'western sahara', 'british virgin islands', 'caribbean netherlands', 'south sudan', 'sao tome and principe', 'anguilla', 'saint pierre miquelon', 'yemen', 'china']
droplist=OptionMenu(top,c, *a)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=300,y=335)

def covid():

    for x in range (1):

        if R1!=1 and R2!=2 and R3!=3 and R4!=4 and R5!=5 and R6!=6 and R7!=7 and R8!=8 and R9!=9 and R10!=10 and R11!= 11 and R12!=12 and R13!=13:

            answer=messagebox.showinfo("You are not good","have a doc")

        else:

            answer=messagebox.showinfo("You are good","have a great day")

Button(top, text ="click here to save",bg="red", fg="white", activebackground = "pink", activeforeground = "blue",command=database).place(x = 550, y = 340)
Button(top, text ="Submit",bg="brown", fg="white", activebackground = "pink", activeforeground = "blue",command=covid).place(x = 690, y = 340)

def tick():
    time_string=time.strftime("%H:%M:%S %p")
    clock.config(text=time_string)
    clock.after(200,tick)

clock=Label(top, font=("times",20,"italic"),bg="black",fg="red")
clock.place(x=630,y=1)
tick()

dt= Label(top, text = "date", fg = "yellow",bg="black").place(x = 630, y = 49)
e4 = Entry(top,textvar=d).place(x = 670, y =50)
label = Label(top)
label.pack()
top.mainloop()

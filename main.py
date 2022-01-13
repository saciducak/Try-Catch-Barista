import tkinter as tk
from tkinter import*
from tkinter import messagebox
import random
import time
def anaekran():
    ekran = Tk()
    frame = tk.Frame(ekran)

    ekran.title("Menü Otomasyon Sistemi")
    ekran.geometry("650x450+0+0")
    # -----------------------------
    Tops = Frame(ekran,bg="gray",width = 1000,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)
    Tops2 = Frame(ekran,bg="gray",width = 1600,height=50,relief=SUNKEN)
    #Tops2.pack(side=TOP)

    sol = Frame(ekran,width = 300,height=150,relief=SUNKEN)
    sol.pack(side=LEFT)

    sag = Frame(ekran,width = 300,height=150,relief=SUNKEN)
    sag.pack(side=RIGHT)

    bottom = Frame(ekran,width = 600,height=300,relief=SUNKEN)
    bottom.pack(side=BOTTOM)

    # -----------------------------
    localtime=time.asctime(time.localtime(time.time()))
    # -----------------------------
    lblinfo = Label(Tops, font=( 'aria' ,10, 'bold' ),text="          Restaurant Management System         ",fg="red",bd=8,anchor='w')
    lblinfo.pack(side=LEFT)
    lblinfo = Label(Tops, font=( 'aria' ,10,'bold'  ),text="          "+ localtime + "          ",fg="red",bd=8,anchor=W)
    lblinfo.pack(side=RIGHT)



    LabelWelcome = Label(Tops, font=( 'aria' ,9, 'bold' ),text="Hoşgeldiniz!",fg="black",bd=10,anchor=W)
    LabelWelcome.pack()
    #-----------------------------
    tatli = tk.Label(sol,text="Lluvia  ", fg='purple', bg='light gray', font='Times 12 bold')
    tatli.pack(side=TOP)
    tatli2 = tk.Label(sol,text="Sebastian ", fg='purple', bg='light gray', font='Times 12 bold')
    tatli2.pack(anchor=S)
    tatli3 = tk.Label(sol, text="Brownie  ", fg='purple', bg='light gray', font='Times 12 bold')
    tatli3.pack(anchor=S)
    icecek = tk.Label(sol, text="Çay  ", fg='purple', bg='light gray', font='Times 12 bold')
    icecek.pack(anchor=S)
    icecek2 = tk.Label(sol, text="Limonata  ", fg='purple', bg='light gray', font='Times 12 bold')
    icecek2.pack()

    mealLogin = tk.Entry()
    mealLogin.place(x=150, y=180)
    mealLogin2 = tk.Entry()
    mealLogin2.place(x=150, y=205)
    mealLogin3 = tk.Entry()
    mealLogin3.place(x=150, y=230)
    mealLogin4 = tk.Entry()
    mealLogin4.place(x=150, y=255)
    mealLogin5 = tk.Entry()
    mealLogin5.place(x=150, y=280)

    x=tk.IntVar()
    x.set(0)


    def control2():
        if x.get()==0:
            pass
        else:
            messagebox.showinfo('Dikkat ', 'Tatlıların İçeceği Var!')

    check = tk.Checkbutton(ekran,text="Bu Tatlıların İçeceği Var Mı?",variable = x ,command = control2)
    check.pack()

    def price():
        ekran2 = Tk()
        ekran2.title("Price List")
        ekran2.geometry("300x200")
        Topsinside = Frame(ekran2, bg="gray", width=400, height=40, relief=SUNKEN)
        Topsinside.pack(side=TOP)
        sol = Frame(ekran2, width=400, height=120, relief=SUNKEN)
        sol.pack(side=LEFT)
        sag = Frame(ekran2, width=400, height=120, relief=SUNKEN)
        sag.pack(side=RIGHT)
        orta = Frame(ekran2, width=400, height=120, relief=SUNKEN)
        orta.pack()

        price = tk.Label(Topsinside, font=( 'aria' ,12, 'bold' ) ,text="     ÜRÜN       ")
        price.pack(side=LEFT)
        price = tk.Label(Topsinside, font=( 'aria' ,12, 'bold' ) ,text="     FİYAT     ")
        price.pack(side=LEFT)

        price = tk.Label(sol, font=('aria', 10 ,'bold'), text="    Lluvia")
        price.pack()
        price = tk.Label(sag, font=('aria', 10 ,'bold'),  text="30         ")
        price.pack()
        price = tk.Label(orta, font=('aria', 10, 'bold'), text="   ")
        price.pack()
        price = tk.Label(sol, font=('aria', 10, 'bold'), text="    Sebastian")
        price.pack()
        price = tk.Label(sag, font=('aria', 10, 'bold'), text="25         ")
        price.pack()
        price = tk.Label(orta, font=('aria', 10, 'bold'), text="  ")
        price.pack()
        price = tk.Label(sol, font=('aria', 10 ,'bold'), text="   Brownie")
        price.pack()
        price = tk.Label(sag, font=('aria', 10 ,'bold'), text="30        ")
        price.pack()
        price = tk.Label(sol, font=('aria', 10, 'bold'), text="   Çay")
        price.pack()
        price = tk.Label(sag, font=('aria', 10, 'bold'), text="5        ")
        price.pack()
        price = tk.Label(sol, font=('aria', 10, 'bold'), text="   Limonata")
        price.pack()
        price = tk.Label(sag, font=('aria', 10, 'bold'), text="15         ")
        price.pack()

        ekran2.mainloop()
        #roo.mainloop()
    def calculate():
        meal1 = 0
        meal2 = 0
        meal3 = 0
        meal4 = 0
        meal5 = 0
        meal1 = int(mealLogin.get())
        meal2 = int(mealLogin2.get())
        meal3 = int(mealLogin3.get())
        meal4 = int(mealLogin4.get())
        meal5 = int(mealLogin5.get())

        sum = (meal1*30)+(meal2*25)+(meal3*30)+(meal4*5)+(meal5*15)

        total = tk.Label(sag, font=('aria', 16, 'bold'), text="Your Total Cheque : " )
        total.pack(anchor=W)
        total2 = tk.Label(sag, font=('aria', 16, 'bold'), text = sum)
        total2.pack(anchor=W)
    buttonCalculate= Button(bottom, fg="black", font=('ariel', 10, 'bold'), width=10, text="Calculate", bg="light gray",command=calculate)
    buttonCalculate.pack( anchor=SE)

    buttonPrice=Button(ekran,fg="black",font=('ariel' ,10,'bold'),width=10, text="PRICE", bg="gray",command=price)
    buttonPrice.pack(anchor=SE)

    def print():
        if(mealLogin4 != 0 or mealLogin5 != 0 ):
            messagebox.showwarning("Önemli Uyarı : ", "Bu İçeceklerin Tatlı Siparişi Var !!" )
        messagebox.showinfo("Lluvia " , mealLogin.get())
        messagebox.showinfo("Sebastian", mealLogin2.get())
        messagebox.showinfo("Brownnie" , mealLogin3.get())
        messagebox.showinfo("Çaylar ", mealLogin4.get())
        messagebox.showinfo("Limonata ", mealLogin5.get())
    def qexit():
        ekran.destroy()

    buttonprint = tk.Button(bottom, fg="black", font=('ariel', 10, 'bold'), width=10, text="Order", bg="green",command=print)
    buttonprint.pack(anchor=SE)
    buttonexit=tk.Button(bottom,fg="black",font=('ariel' ,10,'bold'),width=10, text="EXIT", bg="red",command=qexit)
    buttonexit.pack( anchor=SE)

    ekran.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

form=tk.Tk()
form.title("Hoşgeldiniz...")
form.geometry("600x550")
resim=ImageTk.PhotoImage(Image.open("C://Users//sacid//OneDrive//Masaüstü//la_vie_praline.jpg"))

parola="123"
#--------------------------
def qexit():
    form.destroy()
def register():
    ad = tk.Label(text="Name ", fg='purple', bg='light gray', font='Times 12 bold')
    ad.place(x=183, y=400)
    sifre = tk.Label(text="Password ", fg='purple', bg='light gray', font='Times 12 bold')
    sifre.place(x=183, y=430)
    user_login = tk.Entry()
    user_login.place(x=270, y=401)
    passwordlogin = tk.Entry(show = '*')
    passwordlogin.place(x=270, y=429)
def login():
    sifre=passwordlogin.get()
    if(sifre==parola):
        form.destroy()
        anaekran()
    else:
        control.config(text="Incorrect Entry!")
def help():
    messagebox.showinfo("Help","Yardım icin support.menu@apply.com adresine mail atınız..")
#--------------------------
kisi=tk.Label(text="User ",fg='purple',bg='light gray',font='Times 12 bold')
kisi.place(x=183,y=300)
sifre=tk.Label(text="Password ",fg='purple',bg='light gray',font='Times 12 bold')
sifre.place(x=183,y=326)
control=tk.Label(text="",fg='red',bg='white',font='Times 14 bold')
control.place(x=270,y=409)
#-------------------------
user_login = tk.Entry()
user_login.place(x=270,y=301)
passwordlogin = tk.Entry(show = '*')
passwordlogin.place(x=270,y=327)

#-------------------------
buttonexit=tk.Button(form,text="EXIT ",fg='white',bg='red',font='Times 13 bold',command=qexit)
buttonexit.place(x=540,y=489)
entryButton=tk.Button(form,text="LOGIN",fg='black',bg='gray',command=login)
entryButton.place(x=270,y=359)
loginButton= tk.Button(form,text="Sign Up",fg='black',bg='gray',command=register)
loginButton.place(x=320,y=359)
yardım=tk.Button(text="Help ",fg='white',bg='green',font='Times 12 bold',command = help)
yardım.place(x=10,y=10)

button= tk.Button(form,image=resim,activebackground="red")
button.pack()
#-------------------------
form.mainloop()



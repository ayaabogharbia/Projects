from tkinter import*


window = Tk()
window.geometry("500x500")
window.title("Asab shop")
label = Label(window , text = "Welcome TO ITI Shop",bg="#ECF87F" ,fg="black",font=('calibre',15, 'bold'))
label.pack(side = TOP)

photo_0 =PhotoImage(file = 'bk.png')
label_0 = Label(window ,image = photo_0).place(x =0 , y = 30)




# photo = PhotoImage( file = "ITI.png")
# photo = photo.subsample(30,30)
label_1 = Label(window, text="Large" ,height=5,width=10 ,bg="#ECF87F", fg="black").place(x=150,y=300)
# label_1.pack(side=LEFT)
label_2 = Label(window, text="Mediam",height=5,width=10,bg="#ECF87F", fg="black").place(x=280, y=300)
# #label_2.pack(side=TOP)
label_3 = Label(window, text="Small",height=5,width=10 ,bg="#ECF87F", fg="black").place(x=400, y=300)
# #label_3.pack(side=RIGHT)

button_0=Button(window,text="Exit",background="#ECF87F",fg="black",command=window.destroy)
button_0.pack(side = BOTTOM)

def ButtonPressTracker():
	ButtonPressTracker.counter += 1
	print("button large pressed" ,ButtonPressTracker.counter)

ButtonPressTracker.counter=0
photo = PhotoImage( file = "bk.png")
photo = photo.subsample(2,2)
b_1 = Button(window,text ="Large Size",background = "#ECF87F",fg ="black" ,bd = "5" ,command =ButtonPressTracker).place(x=150,y=400)
#b_1.pack(side = TOP)

def ButtonPressTracker_1():
	ButtonPressTracker_1.counter += 1
	print("button mad pressed" ,ButtonPressTracker_1.counter)

ButtonPressTracker_1.counter=0
# photo = PhotoImage( file = "ITI.png")
# photo = photo.subsample(1,1)
b_2 = Button(window,text ="Mediam Size",background = "#ECF87F",fg ="black" ,bd = "5",command =ButtonPressTracker_1).place(x=270,y=400)
#b_2.pack(side = TOP)

def ButtonPressTracker_2():
	ButtonPressTracker_2.counter += 1
	print("button small pressed" ,ButtonPressTracker_2.counter)

ButtonPressTracker_2.counter=0
# photo = PhotoImage( file = "ITI.png")
# photo = photo.subsample(1,1)
b_3 = Button(window,text ="Small Size",background = "#ECF87F",fg ="black" ,bd = "5",command =ButtonPressTracker_2).place(x=400,y=400)
#b_3.pack(side = TOP)

def open_popup():
	top=Tk()
	top.geometry('100x100')
	top.title("BILL")
	Label(top,text="your Bill is=").place(x=0,y=60)
	def button_bill():
		bill=((ButtonPressTracker.counter*20)+(ButtonPressTracker_1.counter*15)+(ButtonPressTracker_2.counter*10))
		label_3=Label(top,text=bill).place(x=100,y=60)	
	button_5=Button(top,text="Bill",background="#ECF87F",fg="black",command=button_bill,height=1,width=2).place(x=70,y=60)
button_4=Button(window,text="BILL",background="#ECF87F",fg="black",command=open_popup,height=3,width=6).place(x=40,y=350)
# button_6=Button(window,text="Exit",background="#ECF87F",fg="black",command=window.destroy)
# button_6.pack(side = BOTTOM)

window.mainloop()








from cProfile import label
from  tkinter import *
root =Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Head name
Label(root,text="Python Registration form",font="ar 15 bold").grid(row=0,column=3)

#Fieldname
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
Emergency=Label(root,text="Emergency")
Paymentmode=Label(root,text="Payment  mode")

#packing  Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
Emergency.grid(row=4,column=2)
Paymentmode.grid(row=5,column=2)


#Variable for storing data
namevalue =StringVar
phonevalue =StringVar
gendervalue =StringVar
Emergencyvalue =StringVar
Paymentmodevalue =StringVar
checkvalue =IntVar


#creatin entryfield
nameentry =Entry(root,textvariable=namevalue)
phoneentry =Entry(root,textvariable=phonevalue)
genderentry =Entry(root,textvariable=gendervalue)
Emergencyentry =Entry(root,textvariable=Emergencyvalue)
Paymentmodeentry =Entry(root,textvariable=Paymentmodevalue)


#packing entry field

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
Emergencyentry.grid(row=4,column=3)
Paymentmodeentry.grid(row=5,column=3)


#checkbox
checkbtn=Checkbutton(text="Save info",variable=checkvalue)

#packing check value
checkbtn.grid(row=6,column=3)

#submit button
Button(text="Submit",command=getvals).grid(row=7,column=3)

root.mainloop()
#23-10-2024
#a1:write python program using tkinter to to check speed of the car and give waring penalty if the speed exceeded
#business conditions:
#speed_limit=90 kmph
#1. speed<=speed_limit:No penality
#2.speed<=speed_limit+20: warning
#3.speed>speed_limit+20:penality

from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("checking speed limit")
window.config(bg="green")
window.geometry("350x400")
def speed_check():
    speed=int(e1.get())
    speed_limit=90
    if(speed<=speed_limit):
        messagebox.showinfo("maximun","the car speed maximun")
    elif(speed<=speed_limit+20):
        messagebox.showinfo("maximun speed"," the car is speed penality speed car")
    elif(speed>=speed_limit+20):
        messagebox.showinfo(" maximun speed","the car is speed warning speed car")
    else:
        messagebox.showinfo("maximun speed","penalty")

l1=Label(window,text="ENTER The speed:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
b1=Button(window,text="Speed",command="Speed_Check")
b1.grid(row=2,column=0)
window.mainloop()
#
from tkinter import*
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
import time
import datetime
import winsound
from threading import *

def Threading():
    t1=Thread(target=alarm)
    t1.start()
    
def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if current_time == set_alarm_time:
            
            messagebox.showinfo("alarm","Time to wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ALIAS)
            
            break

def time():
    str = datetime.datetime.now().strftime('%H:%M:%S')
    l.config(text=str)
    l.after(1000,time)
            
root = Tk()
root.title("ALARM CLOCK")
root.geometry("500x350")

Label(root,text="ALARM CLOCK",font=("Cambria 30 bold"),fg="blue").pack(pady=10)

Label(root,text="CURRENT TIME",font=("Cambria 20 bold"),fg="green").pack()

l=Label(root,font=("Cambria 15"))
l.pack(anchor='center')
time()

Label(root,text="SET TIME",font=("Cambria 20 bold"),fg="green").pack(pady=10)

frame=Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00','01','02','03','04','05','06','07','08','09','10','11','12'
         ,'13','14','15','16','17','18','19','20','21','22','23','24')
hour.set(hours[0])

hrs = OptionMenu(frame,hour,*hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15'
           ,'16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'
           ,'31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46'
           ,'47','48','49','50','51','52','53','54','55','56','57','58','59','60')
minute.set(minutes[0])

mins = OptionMenu(frame,minute,*minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15'
           ,'16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'
           ,'31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46'
           ,'47','48','49','50','51','52','53','54','55','56','57','58','59','60')
second.set(seconds[0])

secs = OptionMenu(frame,second,*seconds)
secs.pack(side=LEFT)

Button(root,text="SET ALARM",font=("Cambria 20 bold"),fg="red",command=Threading).pack(pady=20)

root.mainloop()
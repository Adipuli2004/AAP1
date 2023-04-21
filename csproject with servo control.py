#importing libraries
import tkinter as tk
import sys
import time
import datetime
import RPi.GPIO as GPIO
#Pi set up
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(0)
GPIO.setup(12,GPIO.OUT)
servo2=GPIO.PWM(12,50)
servo2.start(0)
#functions
def lron():
    def lrond():
        labellron.destroy()
        blrond.destroy()
    servo1.changedutycycle(7)
    time.sleep(2)
    labellron=tk.Label(root,text="Living room light turned on",bg="yellow",fg="red",font=("Arial",24))
    labellron_canvas=canvas.create_window(230,550,window=labellron)
    blrond=tk.Button(root,text="OK",bg="yellow",fg="red",height=2,command=lrond)
    blrond_canvas=canvas.create_window(550,550,window=blrond )                                      
def lroff():
    def lroffd():
        labellroff.destroy()
        blroffd.destroy()
    servo1.changedutycycle(2)
    time.sleep(2)
    labellroff=tk.Label(root,text="Living room light turned off",bg="yellow",fg="red",font=("Arial",24))
    labellroff_canvas=canvas.create_window(230,550,window=labellroff)
    blroffd=tk.Button(root,text="OK",bg="yellow",fg="red",height=2,command=lroffd)
    blroffd_canvas=canvas.create_window(550,550,window=blroffd)    
def br1on():
    def br1ond():
        labelbr1on.destroy()
        bbr1ond.destroy()
    servo2.changedutycycle(7)
    time.sleep(2)
    labelbr1on=tk.Label(root,text="bedroom room1 light turned on",bg="yellow",fg="red",font=("Arial",24))
    labelbr1on_canvas=canvas.create_window(260,610,window=labelbr1on)
    bbr1ond=tk.Button(root,text="OK",bg="yellow",fg="red",height=2,command=br1ond)
    bbr1ond_canvas=canvas.create_window(550,610,window=bbr1ond)    
def br1off():
    def br1offd():
        labelbr1off.destroy()
        bbr1offd.destroy()
    servo2.changedutycycle(2)
    time.sleep(2)
    labelbr1off=tk.Label(root,text="bedroom room1 light turned off",bg="yellow",fg="red",font=("Arial",24))
    labelbr1off_canvas=canvas.create_window(260,610,window=labelbr1off)
    bbr1offd=tk.Button(root,text="OK",bg="yellow",fg="red",height=2,command=br1offd)
    bbr1offd_canvas=canvas.create_window(550,610,window=bbr1offd)    
def on():
    lron()
    br1on()    
def off():
    lroff()
    br1off()    
def time1():   
    def timecheck():
        try:    
            x=txt.get()
            dto=datetime.datetime.strptime(x,"%d/%m/%y %H:%M:%S")
            while True:
                now=datetime.datetime.now()
                current_time=now.strftime("%d/%m/%y %H:%M:%S")
                ct=datetime.datetime.strptime(current_time,"%d/%m/%y %H:%M:%S")
                if ct>=dto:
                    on()
                    break
                else:
                    time.sleep(5)
        except ValueError:
            def error():
                labelerror.destroy()
                berror.destroy()
            labelerror=tk.Label(root,text="Invalid input",bg="yellow",fg="red",font=("Arial",24))
            labeterror_canvas=canvas.create_window(550,380,window=labelerror)
            berror=tk.Button(root,text="OK",bg="yellow",fg="red",height=2,command=error)
            berror_canvas=canvas.create_window(700,380,window=berror)        
    def timecheck_():
        try:
            y=txt_.get()
            dto_=datetime.datetime.strptime(y,"%d/%m/%y %H:%M:%S")
            while True:
                now=datetime.datetime.now()
                currenttime=now.strftime("%d/%m/%y %H:%M:%S")
                ct_=datetime.datetime.strptime(currenttime,"%d/%m/%y %H:%M:%S")
                if ct_>=dto_:
                    off()
                    break
                else:
                    time.sleep(5)
        except ValueError:
            def error1():
                labelerror1.destroy()
                berror1.destroy()
            labelerror1=tk.Label(root,text="Invalid input",bg="yellow",fg="red",font=("Arial",24))
            labeterror1_canvas=canvas.create_window(550,500,window=labelerror1)
            berror1=tk.Button(root,text="OK",bg="yellow",fg="red",height=2,command=error1)
            berror1_canvas=canvas.create_window(700,500,window=berror1)            
    #on button
    txt=tk.Entry(root,width=10,font=("Arial bold",24))
    tx_canvas=canvas.create_window(130,380,window=txt)
    labeltime=tk.Label(root,text="enter the date and time(dd/mm/yy hh:mm:ss) to turn on",bg="yellow",fg="red",font=("Arial",24))
    labetime_canvas=canvas.create_window(430,320,window=labeltime)
    but=tk.Button(root,text="enter",bg="yellow",fg="red",height=2,command=timecheck)
    but_canvas=canvas.create_window(300,380,window=but)
    #off button
    txt_=tk.Entry(root,width=10,font=("Arial bold",24))
    txt_canvas=canvas.create_window(130,500,window=txt_)
    label_time=tk.Label(root,text="enter the date and time(dd/mm/yy hh:mm:ss) to turn off",bg="yellow",fg="red",font=("Arial",24))
    label_time_canvas=canvas.create_window(430,440,window=label_time)
    but_=tk.Button(root,text="enter",bg="yellow",fg="red",height=2,command=timecheck_)
    but__canvas=canvas.create_window(300,500,window=but_)    
def distime():
    now=datetime.datetime.now()
    ct1=now.strftime("%d/%m/%y %H:%M:%S")
    ct2=datetime.datetime.strptime(ct1,"%d/%m/%y %H:%M:%S")
    label_distime=tk.Label(root,text=ct2,bg="yellow",fg="red",font=("Arial",24))
    label_distime_canvas=canvas.create_window(195,670,window=label_distime)    
def exit():
    sys.exit()   


#main
    
#gui setup
#background
root=tk.Tk()
root.title("CS project 2021-22")
img=tk.PhotoImage(file="bulb.png")
canvas=tk.Canvas(root)
canvas.pack(fill="both",expand=True)
canvas.create_image(0,0,image=img,anchor="nw")

#widgets
#labels

label1=tk.Label(root,text="LIGHT CONTROL",bg="yellow",fg="red",font=("Arial bold",30))
label1_canvas=canvas.create_window(800,30,window=label1)

label2=tk.Label(root,text="toggle all lights",bg="yellow",fg="red",font=("Arial",24))
label2_canvas=canvas.create_window(150,80,window=label2)

label_lr=tk.Label(root,text="toggle living room lights",bg="yellow",fg="red",font=("Arial",24))
label_lr_canvas=canvas.create_window(210,140,window=label_lr)

label_br1=tk.Label(root,text="toggle bedroom 1 lights",bg="yellow",fg="red",font=("Arial",24))
label_br1_canvas=canvas.create_window(210,200,window=label_br1)

labeltime=tk.Label(root,text="would you like to time all lights?",bg="yellow",fg="red",font=("Arial ",24))
labeltime_canvas=canvas.create_window(265,260,window=labeltime)

#buttons

b1=tk.Button(root,text="ON",bg="yellow",fg="red",height=2,command=on)
b1_canvas=canvas.create_window(450,80,window=b1)

b2=tk.Button(root,text="OFF",bg="yellow",fg="red",height=2,command=off)
b2_canvas=canvas.create_window(550,80,window=b2)

lr=tk.Button(root,text="ON",bg="yellow",fg="red",height=2,command=lron)
lr_canvas=canvas.create_window(450,140,window=lr)

lr1=tk.Button(root,text="OFF",bg="yellow",fg="red",height=2,command=lroff)
lr1_canvas=canvas.create_window(550,140,window=lr1)

br1_on=tk.Button(root,text="ON",bg="yellow",fg="red",height=2,command=br1on)
br1_on_canvas=canvas.create_window(450,200,window=br1_on)

br1_off=tk.Button(root,text="OFF",bg="yellow",fg="red",height=2,command=br1off)
br1_off_canvas=canvas.create_window(550,200,window=br1_off)

time1=tk.Button(root,text="YES",bg="yellow",fg="red",height=2,command=time1)
time1_canvas=canvas.create_window(550,260,window=time1)

btime=tk.Button(root,text="Display current date and time",bg="yellow",fg="red",height=2,command=distime)
btime_canvas=canvas.create_window(550,670,window=btime)

button_exit=tk.Button(root,text="CLOSE",bg="yellow",fg="red",height=2,command=exit)
button_exit=canvas.create_window(450,750,window=button_exit)

root.mainloop()
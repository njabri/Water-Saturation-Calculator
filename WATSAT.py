##WaterSaturation.py Calculate Water Saturation using Two different methods
##Author: Nidal Jabri
##Copyright: Copyright 2019

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
from PIL import ImageTk, Image

# SWA = (A*RWFT/(PHIE**M)/RESD)**(1/N))

def archies(*args):
    try:
        value1 = float(a.get())
        value2 = float(m.get())
        value3 = float(n.get())
        value4 = float(phie.get())
        value5 = float(resd.get())
        value6 = float(rwft.get())
        swa.set((value1*value6/(value4**value2)/value5)**(1/value3)*100)
    except ValueError:
        pass

def archies_m(*args):
    try:
        value1 = float(a.get())
        value2 = float(m.get())
        value3 = float(n.get())
        value4 = float(phie.get())
        value5 = float(resd.get())
        value6 = float(rwft.get())
        value7 = float(vsh.get())
        value8 = float(rsh.get())
        swa.set((((0.4*value6)/(value4**2))*(math.sqrt((value7/value8)**2)+((value4**2)*5)/(value5*value6))-(value7/value8))*100)
    except ValueError:
        pass  
      
def client_exit():
    root.destroy()
    
def about():
   lines = ['WATER SATURATION CALULATOR', 'Created by: Nila Holding Group LLC','Contact: Nidal.Jabri@Mavs.Uta.Edu']
   messagebox.showinfo('V1.2.0', "\n".join(lines))
    
    
    
root = Tk()
pw = PanedWindow(orient='vertical')
pw.grid(row=1,column=0,sticky=(N, W, E, S),padx=5,pady=5)
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=3)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="about", command=about)
filemenu.add_command(label="exit", command=client_exit)


root.title("Water Saturation")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


bckgrnd = ImageTk.PhotoImage(file='NilaLogo.gif')
root.tk.call('wm', 'iconphoto',root._w, bckgrnd)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


a = StringVar()
m = StringVar()
n = StringVar()
phie = StringVar()
resd = StringVar()
rwft = StringVar()
swa = StringVar()
vsh = StringVar()
rsh = StringVar()
path = "simandoux.png"
pathsw = "archie1.png"



img = ImageTk.PhotoImage(Image.open(path))
img1 = ImageTk.PhotoImage(Image.open(pathsw))

a_entry = ttk.Entry(mainframe, width=5, textvariable=a)
a_entry.bind('<Return>', lambda event: m_entry.focus())
a_entry.grid(column=2, row=2, sticky=(W, E))

m_entry = ttk.Entry(mainframe, width=5, textvariable=m)
m_entry.bind('<Return>', lambda event: n_entry.focus())
m_entry.grid(column=2, row=3, sticky=(W, E))

n_entry = ttk.Entry(mainframe, width=5, textvariable=n)
n_entry.bind('<Return>', lambda event: phie_entry.focus())
n_entry.grid(column=2, row=4, sticky=(W, E))

phie_entry = ttk.Entry(mainframe, width=5, textvariable=phie)
phie_entry.bind('<Return>', lambda event: resd_entry.focus())
phie_entry.grid(column=2, row=5, sticky=(W, E))

resd_entry = ttk.Entry(mainframe, width=5, textvariable=resd)
resd_entry.bind('<Return>', lambda event: rwft_entry.focus())
resd_entry.grid(column=2, row=6, sticky=(W, E))

rwft_entry = ttk.Entry(mainframe, width=5, textvariable=rwft)
rwft_entry.bind('<Return>', lambda event: vsh_entry.focus())
rwft_entry.grid(column=2, row=7, sticky=(W, E))

vsh_entry = ttk.Entry(mainframe, width=5, textvariable=vsh)
vsh_entry.bind('<Return>', lambda event: rsh_entry.focus())
vsh_entry.grid(column=2, row=8, sticky=(W, E))

rsh_entry = ttk.Entry(mainframe, width=5, textvariable=rsh)
rsh_entry.grid(column=2, row=9, sticky=(W, E))

ttk.Label(mainframe,font="bold", textvariable=swa).grid(column=2, row=10, sticky=(W, E))
tk.Button(pw, text="ARCHIES",image=img1, font="bold", command=archies).grid(column=1, row=11,padx=5, sticky=W)
tk.Button(pw, text="ARCHIES_SIMANDOUX",image=img, font="bold", command=archies_m).grid(column=1, row=12, sticky=E)
tk.Button(pw, fg="gray",font="bold", text='QUIT', command = root.destroy).grid(column=1, row=11, sticky=E)


tk.Label(mainframe, text="Enter value:").grid(column=1, row=1, sticky=W)
tk.Label(mainframe, text="TORTUOSITY EXPONENT (A):").grid(column=1, row=2, sticky=W)
tk.Label(mainframe, text="CEMENTATION EXPONENT(M):").grid(column=1, row=3, sticky=W)
tk.Label(mainframe, text="SATURATION EXPONENT(N):").grid(column=1, row=4, sticky=W)
tk.Label(mainframe, text="ARCHIE").grid(column=3, row=2)
tk.Label(mainframe, text="ARCHIE").grid(column=3, row=3)
tk.Label(mainframe, text="ARCHIE").grid(column=3, row=4)
tk.Label(mainframe, text="ARCHIE/SIMANDOUX").grid(column=3, row=5)
tk.Label(mainframe, text="ARCHIE/SIMANDOUX").grid(column=3, row=6)
tk.Label(mainframe, text="ARCHIE/SIMANDOUX").grid(column=3, row=7)
tk.Label(mainframe, text="SIMANDOUX").grid(column=3, row=8)
tk.Label(mainframe, text="SIMANDOUX").grid(column=3, row=9)
tk.Label(mainframe, text="EFFECTIVE POROSITY(PHIE):").grid(column=1, row=5, sticky=W)
tk.Label(mainframe, text="RESISTIVITY OF ZONE(RESD):").grid(column=1, row=6, sticky=W)
tk.Label(mainframe, text="WATER RESISTIVITY(RWFT):").grid(column=1, row=7, sticky=W)
tk.Label(mainframe, text="VOLUME OF SHALE(VSH):").grid(column=1, row=8, sticky=W)
tk.Label(mainframe, text="RESISTIVITY OF SHALE(RSH):").grid(column=1, row=9, sticky=W)
tk.Label(mainframe, text="WATER SATURATION:").grid(column=1, row=10, sticky=W)
tk.Label(mainframe, text="%").grid(column=3, row=10, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

a_entry.focus()

root.mainloop()

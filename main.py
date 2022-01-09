from tkinter import *
from tkinter import ttk
from datetime import datetime
from dateutil import relativedelta
import tkinter.font as tkFont

root = Tk()
root.title("Izračunaj staž")
root.minsize(360,420)
#fonts
fontStyle = tkFont.Font(family="Lucida Grande", size=18)
fontRezultat = tkFont.Font(family="Lucida Grande", size=12, weight="bold")
fontButton = tkFont.Font(family="Lucida Grande", size=14)

#get result
def izracunaj():
    try:
        dan_pocetni = int(dan_poc_entry.get())
        mesec_pocetni = int(mes_poc_entry.get())
        godina_pocetni = int(god_poc_entry.get())
        dan_zavrsni = int(dan_zav_entry.get())
        mesec_zavrsni = int(mes_zav_entry.get())
        godina_zavrsni = int(god_zav_entry.get())
        date_1 = datetime(godina_pocetni, mesec_pocetni, dan_pocetni)
        date_2 = datetime(godina_zavrsni, mesec_zavrsni, dan_zavrsni)
        # Get the interval between two dates
        diff = relativedelta.relativedelta(date_2, date_1)
        rezultat.set(str(diff.years)+" godina "+str(diff.months)+" meseci i "+str(diff.days)+" dana.")
    except:
        rezultat.set("Moraš uneti sve ispravne vrednosti")

##first label frame for početni datum
lf1 = ttk.LabelFrame(root, text='Početni datum', width=340, height=160)
lf1.grid(column=0, row=0, padx=20, pady=20)
#labels from first labelframe
dan_poc_label= ttk.Label(lf1, text="Dan")
dan_poc_label.grid(row=0, column=0, sticky = (W, E), padx=30)

mes_poc_label= ttk.Label(lf1, text="Mesec")
mes_poc_label.grid(row=0, column=1, sticky = (W, E), padx=30)

god_poc_label= ttk.Label(lf1, text="Godina")
god_poc_label.grid(row=0, column=2, sticky = (W, E), padx=30)
#entry fields from first labelframe
dan_poc_entry= ttk.Entry(lf1, width=6)
dan_poc_entry.grid(row=1, column=0, sticky = (W, E), padx=10, pady=10)

mes_poc_entry= ttk.Entry(lf1, width=6)
mes_poc_entry.grid(row=1, column=1, sticky = (W, E), padx=10, pady=10)

god_poc_entry= ttk.Entry(lf1, width=12)
god_poc_entry.grid(row=1, column=2, sticky = (W, E), padx=30, pady=10)

##second labelframe for zavrsni datum

lf2 = ttk.LabelFrame(root, text='Završni datum', width=340, height=160)
lf2.grid(column=0, row=1, padx=20, pady=20)
#labels from first labelframe
dan_zav_label= ttk.Label(lf2, text="Dan")
dan_zav_label.grid(row=0, column=0, sticky = (W, E), padx=30)

mes_zav_label= ttk.Label(lf2, text="Mesec")
mes_zav_label.grid(row=0, column=1, sticky = (W, E), padx=30)

god_zav_label= ttk.Label(lf2, text="Godina")
god_zav_label.grid(row=0, column=2, sticky = (W, E), padx=30)
#entry fields from second labelframe
dan_zav_entry= ttk.Entry(lf2, width=6)
dan_zav_entry.grid(row=1, column=0, sticky = (W, E), padx=10, pady=10)

mes_zav_entry= ttk.Entry(lf2, width=6)
mes_zav_entry.grid(row=1, column=1, sticky = (W, E), padx=10, pady=10)

god_zav_entry= ttk.Entry(lf2, width=12)
god_zav_entry.grid(row=1, column=2, sticky = (W, E), padx=30, pady=10)
##third labelframe - result
lf3 = ttk.LabelFrame(root, text='Rezultat', width=340)
lf3.grid(column=0, row=2, padx=20, pady=20, sticky=(W, E))
#label with result or except message
rezultat = StringVar()
rez= ttk.Label(lf3, textvariable=rezultat, font=fontRezultat)
rez.grid(row=0, column=0, sticky = (W, E), padx = 10, pady = 10)

# button widget count result
c1 = Button(root, text = "Izračunaj staž", bg="#3066be", fg="white", font=fontButton, command=izracunaj)
c1.grid(row = 3, column = 0, sticky = (W, E), padx = 10, pady = 5)


root.mainloop()

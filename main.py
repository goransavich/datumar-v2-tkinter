from tkinter import *
from tkinter import ttk
from datetime import datetime
from dateutil import relativedelta
import tkinter.font as tkFont

root = Tk()
root.title("Izračunaj staž")
root.minsize(200,400)

def izracunaj():
    try:
        dan_pocetni = int(dan_entry.get())
        mesec_pocetni = int(mesec_entry.get())
        godina_pocetni = int(godina_entry.get())
        dan_zavrsni = int(dan2_entry.get())
        mesec_zavrsni = int(mesec2_entry.get())
        godina_zavrsni = int(godina2_entry.get())
        date_1 = datetime(godina_pocetni, mesec_pocetni, dan_pocetni)
        date_2 = datetime(godina_zavrsni, mesec_zavrsni, dan_zavrsni)
        # Get the interval between two dates
        diff = relativedelta.relativedelta(date_2, date_1)
        rezultat.set(str(diff.years)+" godina "+str(diff.months)+" meseci i "+str(diff.days)+" dana.")
    except:
        rezultat.set("Moras uneti sve ispravne vrednosti")


##POCETNI DATUM
fontStyle = tkFont.Font(family="Lucida Grande", size=18)
fontRezultat = tkFont.Font(family="Lucida Grande", size=16, weight="bold")
ttk.Label(root, text="Datum početka", font=fontStyle).grid(row=0, column=1, pady=20, columnspan=3, sticky=(W, E))
ttk.Label(root, text="Dan").grid(row=1, column=0, padx = 5, pady = 5)
ttk.Label(root, text="Mesec").grid(row=1, column=1, padx = 5, pady = 5)
ttk.Label(root, text="Godina").grid(row=1, column=2, padx = 5, pady = 5)

dan_entry = ttk.Entry(root)
dan_entry.grid(column=0, row=2, padx=10, pady = 5)

mesec_entry = ttk.Entry(root)
mesec_entry.grid(column=1, row=2, padx = 10, pady = 5)

godina_entry = ttk.Entry(root)
godina_entry.grid(column=2, row=2, padx = 10, pady = 5)

##ZAVRSNI DATUM
ttk.Label(root, text="Datum završetka", font=fontStyle).grid(row=3, column=1,pady=10, columnspan=3,sticky=(W, E))
ttk.Label(root, text="Dan").grid(row=4, column=0, padx = 5, pady = 5)
ttk.Label(root, text="Mesec").grid(row=4, column=1, padx = 5, pady = 5)
ttk.Label(root, text="Godina").grid(row=4, column=2, padx = 5, pady = 5)


dan2_entry = ttk.Entry(root)
dan2_entry.grid(column=0, row=5, padx = 10, pady = 5)


mesec2_entry = ttk.Entry(root)
mesec2_entry.grid(column=1, row=5, padx = 10, pady = 5)


godina2_entry = ttk.Entry(root)
godina2_entry.grid(column=2, row=5, padx = 10, pady = 5)

rezultat = StringVar()
ttk.Label(root, textvariable=rezultat, font=fontRezultat).grid(row=6, column=0, padx=30, pady=20, columnspan=3,sticky=(W, E))

# checkbutton widget
c1 = Button(root, text = "Izračunaj staž", bg="#3066be", fg="white", command=izracunaj)
c1.grid(row = 7, column = 0, sticky = (W, E), columnspan = 3, padx = 10, pady = 25)

root.mainloop()

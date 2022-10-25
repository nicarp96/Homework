import read_data as rd
import os
import add_data as wd

print("1.Adaugare\n2.Citire\n")
choise = int(input("1-2 -> "))
if choise==1:
    if os.path.isfile('../Homework7/catalog.txt'):
        wd.append_data(wd.prepareData())
    else:
        wd.add_data(wd.prepareData())

else:
    rd.read_data()

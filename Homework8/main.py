import read_data as rd
import os
import add_data as wd
while True:
    print("1.Adaugare\n2.Citire\n")
    choise = int(input("1-2 -> "))
    if choise == 1:
        if os.path.isfile('../Homework7/catalog.txt'):
            wd.DataAppending.append_data(wd.Student.prepare_data())
        else:
            wd.DataAppending.add_data(wd.Student.prepare_data())

    else:
        reader = rd.Reader.read_data();

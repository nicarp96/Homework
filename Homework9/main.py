import read_data as rd
import os
import add_data as wd
while True:
    print("1.Adaugare\n2.Citire\n3.Sterge ultimul elev\n")
    choise = int(input("1-3 -> "))
    if choise == 1:
        if os.path.isfile('catalog.txt'):
            wd.DataAppending.append_data(wd.Student.prepare_data())
        else:
            wd.DataAppending.add_data(wd.Student.prepare_data())

    elif choise == 2:
        reader = rd.Reader.read_data();
    elif choise == 3:
        wd.DeleteStudent.delete_data()

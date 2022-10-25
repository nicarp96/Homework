class Student:
    @staticmethod
    def prepare_data():
        register = []
        student = {}
        st_num = int(input(' Numarul de studenti -> '))
        sub_num = int(input(' Numarul de obiecte -> '))
        total_note = 0
        for i in range(st_num+1):
            st_name = input(' Numele studentului -> ')
            student.update({' Name ': st_name})
            st_class = input(' Clasa studentului -> ')
            student.update({"Clasa": st_class})
            for j in range(sub_num):
                subject = input(' Denumirea obiectului -> ')
                mark_nr = int(input(" Numarul de note -> "))
                for z in range(mark_nr):
                    mark = float(input(' Nota -> '))
                    student.update({subject + " nota nr.{}".format(z + 1): mark})
                    total_note += float(student[subject + " nota nr.{}".format(z + 1)])
                    if z == mark_nr - 1:
                        student.update({subject + " nota semestriala ": total_note / mark_nr})
            register.append(student.copy())
            return register


class DataAppending:
    @staticmethod
    def add_data(register):
        catalog = open("catalog.txt", "w")
        catalog.write(" ".join(str(e) for e in register))
        catalog.close()

    @staticmethod
    def append_data(register):
        catalog = open("catalog.txt", "a")
        catalog.write("\n")
        catalog.write(" ".join(str(e) for e in register))
        catalog.close()

class DeleteStudent:
    @staticmethod
    def delete_data():
        catalog = open("catalog.txt", "rt")
        lines = catalog.readlines()[:-1]
        lines = str(lines)
        catalog.close()
        catalog1 = open("catalog.txt", "w")
        catalog1.write(lines)
        catalog1.close()



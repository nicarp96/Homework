class Reader:
    @staticmethod
    def read_data():
        file = open("../Homework7/catalog.txt", "r")
        print(file.read())
        file.close()
class Reader:
    @staticmethod
    def read_data():
        file = open("catalog.txt", "r")
        print(file.read())
        file.close()
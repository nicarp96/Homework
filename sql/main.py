import sqlite3 as db
con = db.connect('SQL.db')
cursor = con.cursor()
cursor.execute("create table if not exists Impact("
               "Nume text,"
               "Email text,"
               "Varsta int);")
cursor.execute("Insert into Impact values('Ion', 'email@carp.com', 17)")
cursor.execute("Insert into Impact values('Mihai', 'ealt@carp.com', 14)")
cursor.execute("Insert into Impact values('Vasile', 'eml@cyup.com', 22)")
data = cursor.execute("select * from Impact")
print(data.fetchall())
update = cursor.execute("update Impact set Varsta = 21 where Nume = 'Ion'")
data = cursor.execute("select * from Impact")
print(data.fetchall())
con.commit()
delete = cursor.execute("delete from impact where Nume = 'Ion'")
data = cursor.execute("select * from Impact")
print(data.fetchall())
con.close()

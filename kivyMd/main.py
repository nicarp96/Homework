from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
import sqlite3 as db

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.l = MDLabel(text = "hi", halign = 'center', text_color= (0.5,0,0.5,1), font_style = 'Caption')
        self.n = MDTextField(text = 'Enter Name', pos_hint={'center_x':0.5, 'center_y':0.8}, width =100)
        self.t = MDLabel(text="", halign='justify', text_color=(0.5, 0, 0.5, 1), font_style='Caption')
        btn =MDRectangleFlatButton(text= 'Submit', pos_hint={'center_x':0.5,'center_y':0.3 }, on_release = self.db_sync())
        btn1 =MDRectangleFlatButton(text= 'Submit', pos_hint={'center_x':0.5,'center_y':0.1 }, on_release = self.db_show())

        screen.add_widget(self.n)
        screen.add_widget(self.l)
        screen.add_widget(self.t)
        screen.add_widget(btn1)
        screen.add_widget(btn)
        return screen

    def db_sync(self):
        self.l.text = self.n.text
        con = db.connect('SQL.db')
        cursor = con.cursor()
        cursor.execute("create table if not exists Label("
                       "Nume text);")
        cursor.execute('insert into Label values('+self.n.text+');')
        con.commit()
        con.close()
    def db_show(self):
        con = db.connect('SQL.db')
        cursor = con.cursor()
        self.t.text = cursor.execute('select * from Label')


MainApp().run()

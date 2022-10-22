from kivy.app import App
from kivy.lang.builder import Builder

class MainApp(App):
    def build(self):
        return Builder.load_file('file.kv')

MainApp().run()
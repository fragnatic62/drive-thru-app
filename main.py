import os

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Window.maximize()

Builder.load_file(os.path.abspath('main.kv'))

class AppLayout(Widget):
    pass

class CommonScreen(Screen):
    pass

class CustomerScreen(CommonScreen):
    pass

class OrderTakerScreen(CommonScreen):
    pass


class AdvertisementScreen(CommonScreen):
    pass

class DriveThruApp(App):
    def build(self):
        return AppLayout()
    
if __name__=='__main__':
    DriveThruApp().run()
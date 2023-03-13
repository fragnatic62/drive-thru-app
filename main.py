import os

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen



Builder.load_file(os.path.abspath('main.kv'))

class MyLayout(Widget):
    pass

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__=='__main__':
    AwesomeApp().run()
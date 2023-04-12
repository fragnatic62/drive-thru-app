import os

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.video import Video

Window.maximize()

Builder.load_file(os.path.abspath('main.kv'))

class OrderTakerCamera(BoxLayout):
    pass

class CustomerCamera(BoxLayout):
    pass


class AdvertisementSpace(BoxLayout):
    pass

class FullImage(Image):
    pass
class AppLayout(Widget):
    pass

class DriveThruApp(App):
    def build(self):
        return AppLayout()
    
if __name__=='__main__':
    DriveThruApp().run()
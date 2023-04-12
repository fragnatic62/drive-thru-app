import os

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.video import Video

Window.maximize()

Builder.load_file(os.path.abspath('main.kv'))

class FullImage(Image):
    pass
    
class AppLayout(Widget):
    img_src = StringProperty('assets/test-image.png')
    video_src = StringProperty('assets/big_buck_bunny_720p_1mb.mp4')

    # handles the streaming/image event on advertisement component section
    def ads_component_handler(self):
        if(self.img_src=='assets/test.png'):
            self.img_src = 'assets/test-image.png'
        else:
            self.img_src = 'assets/test.png'

    # handles the streaming event on customer and ordertaker component section
    def video_component_handler(self):
        if(self.video_src=='assets/big_buck_bunny_720p_1mb.mp4'):
            self.video_src = 'assets/Free_Test_video.mp4'
        else:
            self.video_src = 'assets/big_buck_bunny_720p_1mb.mp4'
    
    # handles the event simulation of the sensor trigger event
    def button_clicked(self):
        self.ads_component_handler()
        self.video_component_handler()


class DriveThruApp(App):
    def build(self):
        return AppLayout()
    
if __name__=='__main__':
    DriveThruApp().run()
import os

# Kivy imports
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.clock import Clock

# Orange Pi Pins imports
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

#initialize the gpio module
gpio.init()

#initialize GPIO pin
gpio.setcfg(port.PA12,gpio.INPUT)
gpio.pullup(port.PA12,gpio.PULLUP)
gpio.pullup(port.PA12,gpio.PULLDOWN)

Window.maximize()

Builder.load_file(os.path.abspath('main.kv'))

class FullImage(Image):
    pass
    
class AppLayout(Widget):
    img_src = StringProperty('assets/test-image.png')
    video_src = StringProperty('assets/big_buck_bunny_720p_1mb.mp4')

    def __init__(self,**kwargs):
        super(AppLayout,self).__init__(**kwargs)
        Clock.schedule_interval(self.event_handler,0.1)
    
    #event callback to change screen view to camera
    def event_handler(self,dt):
        value = gpio.input(port.PA12)
        if(value==0):
            self.set_screen_to_video_stream()
            Clock.schedule_once(self.reset_event_to_default,5)
    
    #event callback to reset screen view
    def reset_event_to_default(self,dt):
        self.set_screen_to_default()

    
    def set_screen_to_default(self):
        self.img_src = 'assets/test-image.png'
        self.video_src = 'assets/big_buck_bunny_720p_1mb.mp4'
    
    def set_screen_to_video_stream(self):
        self.img_src = 'assets/test.png'
        self.video_src = 'assets/Free_Test_video.mp4'

    

class DriveThruApp(App):
    def build(self):
        return AppLayout()
    
if __name__=='__main__':
    DriveThruApp().run()
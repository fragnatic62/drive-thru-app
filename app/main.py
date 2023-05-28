import os
import socket
import time

# Kivy imports
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
import cv2
from kivy.graphics.texture import Texture
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen, ScreenManager


Builder.load_file(os.path.abspath('main.kv'))

Window.maximize()



"""rtsp address of camera to be stream"""
# channel_one = 'rtsp://admin:*adminpassword@192.168.1.109:554/cam/realmonitor?channel=1&subtype=0'
channel_two = 'rtsp://admin:*adminpassword@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0'


class FullScreenImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1)
            self.rect = Rectangle(texture=self.texture, size=(self.width + 20, self.height + 20), pos=(self.x - 10, self.y - 10))

    def on_size(self, *args):
        self.rect.size = self.width + 20, self.height + 20
        self.rect.pos = self.x - 10, self.y - 10

class Camera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(Camera, self).__init__(**kwargs)
        self.capture = capture
        self.fps = fps
        Clock.schedule_interval(self.update, 1.0 / self.fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Flip the frame vertically
            frame = cv2.flip(frame, 0)
            # Convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Create a texture from the frame data
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            # Update the Image widget with the new texture
            self.texture = texture

class CustomerCamera(BoxLayout):
     def __init__(self,**kwargs):
        super(CustomerCamera, self).__init__(**kwargs)
        # Create a capture object from the RTSP URLs
        capture = cv2.VideoCapture(channel_two)

        # Set the capture resolutions
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Create Camera widgets using the capture objects and a frame rate of 30 FPS
        self.camera = Camera(capture, fps=1000)

        # Create a horizontal BoxLayout to hold the cameras
        cameras_layout = BoxLayout()
        cameras_layout.add_widget(self.camera)

        self.add_widget(cameras_layout)


class AdsCarousel(Carousel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_images()
        self.current_page_index = 0
        Clock.schedule_interval(self.load_next_page, 5)
        self.scroll_wheel_distance = 10000

    def load_images(self):
        for i in range(1, 21, 3):
            page = GridLayout(cols=3)
            for j in range(i, i+3):
                img = FullScreenImage(source=f"assets/image{j}.jpeg")
                page.add_widget(img)
            self.add_widget(page)
        self.direction = 'right'

    def load_next_page(self, dt):
        slides = self.slides
        current_slide_index = slides.index(self.current_slide)
        next_slide_index = (current_slide_index + 1) % len(slides)
        if next_slide_index == 0:
            self.direction = 'right'
        else:
            self.direction = 'left'
        self.load_slide(slides[next_slide_index])


# This screen contains the camera display
class ScreenOne(Screen):
    pass

# This screen contains the menu when there's no active customer available
class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        grid = GridLayout(cols=4, spacing=10, padding=10)
        for i in range(20):
            image = FullScreenImage(source=f"assets/image{i+1}.jpeg")
            grid.add_widget(image)
        self.add_widget(grid)


class ScreenManagerApp(App):
    current_signal_response = None
    previous_signal_response = '1'
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Add the screens to the screen manager
        screen2 = ScreenTwo(name='screen2')
        sm.add_widget(screen2)

        screen1 = ScreenOne(name='screen1')
        sm.add_widget(screen1)

        """address and port of the oranges pi which host the gpio"""
        HOST = '192.168.1.107'  # The server's hostname or IP address
        PORT = 8000        # The port used by the server
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.connect((HOST, PORT))
        
        sm.switch_to(screen2)

        def reset_timer():
            Clock.unschedule(load_screen_two)  # Remove any existing scheduled calls
            Clock.schedule_once(load_screen_two, 10)

        def load_screen_one():
            if sm.current_screen == screen2:
                sm.switch_to(screen1)
        
        def load_screen_two(dt):
            if sm.current_screen == screen1:
                sm.switch_to(screen2)

        # Schedule the screen switch every second
        def switch_screen(dt):
                data = socket_instance.recv(1024)
                self.current_signal_response = data.decode('utf-8').strip()

                if self.current_signal_response=='0' and self.previous_signal_response == '1':
                    load_screen_one()
                    Clock.schedule_once(load_screen_two,10)
                if self.current_signal_response=='0' and self.previous_signal_response == '0':
                    reset_timer()
                self.previous_signal_response = self.current_signal_response

        Clock.schedule_interval(switch_screen, 1)

        return sm

if __name__ == '__main__':
    ScreenManagerApp().run()

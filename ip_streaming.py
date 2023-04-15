import cv2
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock

class IPStreamApp(App):
    def build(self):
        self.capture = None
        self.img = Image()
        self.start_button = Button(text='Start Stream', on_press=self.start_stream)
        self.stop_button = Button(text='Stop Stream', on_press=self.stop_stream, disabled=True)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.start_button)
        layout.add_widget(self.stop_button)
        layout.add_widget(self.img)
        return layout

    def start_stream(self, *args):
        self.capture = cv2.VideoCapture('your_IP_camera_url')
        self.start_button.disabled = True
        self.stop_button.disabled = False
        Clock.schedule_interval(self.update_frame, 1/30.)

    def stop_stream(self, *args):
        self.capture.release()
        self.start_button.disabled = False
        self.stop_button.disabled = True

    def update_frame(self, *args):
        ret, frame = self.capture.read()
        if ret:
            self.img.texture = self.process_frame(frame)

    def process_frame(self, frame):
        # any processing of the frame goes here
        return frame.tostring()

if __name__ == '__main__':
    IPStreamApp().run()

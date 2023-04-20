from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock

class SimpleCarousel(Carousel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_images()
        self.current_page_index = 0
        Clock.schedule_interval(self.load_next_page, 3)

    def load_images(self):
        for i in range(1, 21, 5):
            page = GridLayout(cols=5)
            for j in range(i, i+5):
                img = Image(source=f"assets/image{j}.jpeg")
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

class CarouselApp(App):
    def build(self):
        return SimpleCarousel()

if __name__ == '__main__':
    CarouselApp().run()

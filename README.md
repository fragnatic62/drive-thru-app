This document provides an overview and explanation of the code in the `main.py` file.

## Description

The code is a Kivy application that displays camera streams and a carousel of images. It uses OpenCV (`cv2`) to capture frames from an RTSP camera stream and displays them using Kivy's `Image` widget. The application also includes a carousel that cycles through a set of images at regular intervals.

## Prerequisites

Before running the code, ensure that the following dependencies are installed:

- Python 3.10
- Kivy
- OpenCV (`cv2`)

## Usage

To run the application, execute the following command:

```shell
python main.py
```

The application will display the camera stream and the carousel of images. It uses RTSP URLs to connect to the camera stream. The URL for the camera stream is specified in the `channel_two` variable. Adjust the URL according to your camera's configuration.

## File Structure

The file structure of the code is as follows:

- `main.py`: The main Python file that contains the Kivy application.
- `main.kv`: The Kivy language file that defines the layout and visual components of the application.
- `assets/`: A folder that contains the images used in the carousel. The images are named `image1.jpeg`, `image2.jpeg`, and so on.

## Components

The code consists of the following components:

- `FullScreenImage`: A custom widget that extends the Kivy `Image` widget. It displays an image in fullscreen and adds a white border around it.

- `Camera`: A custom widget that displays the camera stream. It uses OpenCV to capture frames from the camera and updates the `Image` widget with the new frames.

- `CustomerCamera`: A custom widget that contains the camera widget. It sets up the camera capture object and defines the layout for displaying the camera.

- `AdsCarousel`: A custom widget that displays a carousel of images. It loads images from the `assets/` folder and cycles through them at regular intervals.

- `ScreenOne`: A screen that contains the camera display.

- `ScreenTwo`: A screen that displays a menu when there is no active customer available. It contains a grid layout of images.

- `ScreenManagerApp`: The main application class that builds the screen manager and sets up the socket connection for switching screens based on external signals.

## Screen Switching

The application uses a socket connection to switch between screens based on external signals. It connects to a server (specified by the `HOST` and `PORT` variables) and receives signals indicating when to switch screens. When a signal of value `0` is received, it switches to `ScreenOne` (camera display). After a certain interval (10 seconds), it switches back to `ScreenTwo` (menu).

## Authors

This code was written by [Your Name] and is based on a template provided by [Author Name].

## License

This project is licensed under the [License Name] license.

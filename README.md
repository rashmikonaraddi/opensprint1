Naruto Shadow Clone Jutsu - Computer Vision Project

## Overview

This project demonstrates a Naruto-inspired "Shadow Clone Jutsu" effect using Python, OpenCV, and MediaPipe.
The system detects a hand sign using the webcam and then creates multiple visual clones of the user on the screen along with a sound effect.

## Technologies Used

* Python 3.11
* OpenCV
* MediaPipe
* Pygame
* NumPy

## Features

* Real-time webcam capture
* Hand landmark detection using MediaPipe
* Shadow Clone visual effect
* Naruto sound effect trigger
* Interactive computer vision demo

## Project Structure

ai-lie-detector/
│
├── naruto_jutsu.py
├── shadow_clone_jutsu.mp3
└── README.txt

## Installation

1. Create a virtual environment
   python -m venv venv

2. Activate the environment
   Windows:
   venv\Scripts\activate

3. Install required libraries
   pip install opencv-python mediapipe pygame numpy protobuf==3.20.3

## Running the Project

Run the Python script:

python naruto_jutsu.py

Your webcam will open and detect hand gestures.

## How it Works

1. The webcam captures live video.
2. MediaPipe detects hand landmarks.
3. When a hand sign is detected:

   * "Shadow Clone Jutsu" text appears
   * Multiple clones of the user appear
   * Naruto sound effect plays.

## Controls

Press "Q" to exit the program.

## Possible Improvements

* Real Naruto hand seal recognition
* Chakra glow effects
* Smoke animation when clones appear
* More realistic clone placement
* Gesture recognition for other jutsu (Rasengan, Fireball)

## Author

Developed as a creative computer vision project inspired by the anime Naruto.

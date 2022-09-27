import os
import time

import cv2
from palleon import encode_image_as_jpeg
from palleon.input_plugin import InputPlugin

# custom defined environment variables
FPS = float(os.environ["palleon_fps"])


class CamInputPlugin(InputPlugin):
    def __init__(self):
        super().__init__()

    def update_thread(self):
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()

            # do the encoding without the lock to save "lock-time"
            data = encode_image_as_jpeg(frame)
            self.update_image(data)

            # wait to read the next frame
            time.sleep(1 / FPS)

    def settings_hook(self, key, value, value_type):
        print(key, value, value_type)


if __name__ == "__main__":
    CamInputPlugin().run()

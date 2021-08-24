import cv2 as cv
import numpy as np

cap = cv.VideoCapture("data/videos/Cars - 1900.mp4")
if not cap.isOpened():
    print("Cannot open video")
    exit()


class Window():

    def __init__(self, window_name):
        self.frame = None
        self.window_name = window_name
        self.x = None
        self.y = None

    def change_frame(self, frame):
        self.frame = frame

    def draw_circle(self, event, x, y, flag, param):
        if event == cv.EVENT_LBUTTONUP:
            # print("Event!")
            self.x = x
            self.y = y

    def show(self):
        self.frame = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        cv.circle(self.frame, (self.x, self.y), 20, (200, 100, 100), -1)
        cv.imshow(self.window_name, self.frame)



cap_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
cap_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
num_of_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
print(f"{cap_width} x {cap_height}")
print(f"{num_of_frames} frames")
i=0

window_obj = Window('video')

cv.namedWindow('video')
cv.setMouseCallback('video', window_obj.draw_circle)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame")
        break

    window_obj.change_frame(frame)

    window_obj.show()


    if cv.waitKey(30) == ord('q'):
        break
    # print(i)
    i += 1

cap.release()
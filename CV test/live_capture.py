import cv2 as cv
import pkg_resources

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
cap_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print(f"{cap_width} x {cap_height}")

# path = pkg_resources.resource_filename('cv2', 'haarcascade_frontalface_default.xml')
# cv.CascadeClassifier().load('data/haarcascade_frontalface_default.xml')
# print(path)
classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        print("Some problems accessing the camera")
        break

    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(frame, 1.3, 8)
    # print(r)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 200, 0), 3)
    cv.imshow("camera", frame)


    if cv.waitKey(10) == ord('q'):
        break

cap.release()
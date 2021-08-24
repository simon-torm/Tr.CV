import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
cap_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print(f"{cap_width} x {cap_height}")


while True:
    ret, frame = cap.read()
    if not ret:
        print("Some problems accessing the camera")
        break

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("camera", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
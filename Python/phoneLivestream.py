import cv2

capture = cv2.VideoCapture("https://192.168.1.3:4747/video") #This is just a dummy url. CHANGE IT later.

while True:
    _, frame = capture.read()

    # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mirror = cv2.flip(frame, 1) # 0 for vertical flip, 1 for horizontal, and -1 for both.

    cv2.imshow("livestream", mirror)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
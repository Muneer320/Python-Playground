import cv2

vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ret, frame = vid.read()
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    if len(data) > 0:
        print(f"\nData: {data}\n\n")
        break
        
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
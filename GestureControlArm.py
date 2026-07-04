import cvzone
import cv2
import serial


ser = serial.Serial('COM5', 9600, timeout=1)  # Replace with correct COM port
print(ser.name)  # Check if the port opens successfully
ser.write(b'Test\n')  # Send test data to the Arduino
ser.close()

cap = cv2.VideoCapture(1)


detector = cvzone.HandDetector(maxHands=1,detectionCon=1)
mySerial = cvzone.SerialObject("COM5",9600,1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers=detector.fingersUp()
        mySerial.sendData(fingers)
    cv2.imshow("image",img)
    cv2.waitKey(1)

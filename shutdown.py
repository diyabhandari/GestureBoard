import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import time

def set_shut():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\shutdown.ps1"])

def shut_system():
    detector = HandDetector(detectionCon=0.6, maxHands=1)
    cap = cv2.VideoCapture(0)
    gesture_up_time = 0
    function_delay = 4  # Time in seconds to wait before performing the function, here locking
    while True:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        hands, image = detector.findHands(image, flipType=False)

        if hands:
            lmList1 = hands[0]['lmList']
            fingers = detector.fingersUp(hands[0])
            if fingers[0] == 1 and fingers[1] == 1 and fingers[3] == 0 and fingers[4] == 1 and fingers[2] == 1: #flick type pose, with ring finger instead
                if gesture_up_time ==0:
                    gesture_up_time = time.time() #amount of time the gesture is up
                elif time.time() - gesture_up_time >= function_delay:
                    set_shut()
            else:
                gesture_up_time = 0  #reset  if the gesture is not maintained
        else:
            gesture_up_time =0  #reset  if no hands are detected

        cv2.imshow("GestureBoard", image)
        key = cv2.waitKey(100)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

shut_system()

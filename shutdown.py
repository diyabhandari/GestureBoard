import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import time

def set_shut():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\shutdown.ps1"])

def shut_system(image,shut_gesture_up,hands,detector): 
    function_delay = 4  # Time in seconds to wait before performing the function, here locking
    while True:
        if hands:
            lmList1 = hands[0]['lmList']
            fingers = detector.fingersUp(hands[0])
            if fingers[0] == 1 and fingers[1] == 1 and fingers[3] == 0 and fingers[4] == 1 and fingers[2] == 1: #flick type pose, with ring finger instead
                if shut_gesture_up ==0:
                    shut_gesture_up = time.time() #amount of time the gesture is up
                elif time.time() - shut_gesture_up >= function_delay:
                    set_shut()
            else:
                shut_gesture_up = 0  #reset  if the gesture is not maintained
        else:
            shut_gesture_up =0  #reset  if no hands are detected
        return image, shut_gesture_up

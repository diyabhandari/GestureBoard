import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import time

def set_restart():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"./scripts/restart.ps1"])

def restart_system(image,restart_gesture_up,hands,detector):
    function_delay = 4 # Time in seconds to wait before performing the function, here locking
    while True:
        if hands:
            lmList1 = hands[0]['lmList']
            fingers = detector.fingersUp(hands[0])
            if fingers[0] == 1 and fingers[1] == 1 and fingers[3] == 0 and fingers[4] == 1 and fingers[2] == 0: #flick with both middle and ring down
                if restart_gesture_up ==0:
                    restart_gesture_up = time.time() #amount of time the gesture is up
                elif time.time() - restart_gesture_up >= function_delay:
                    set_restart()
            else:
                restart_gesture_up = 0  #reset  if the gesture is not maintained
        else:
            restart_gesture_up =0  #reset  if no hands are detected
        return image, restart_gesture_up

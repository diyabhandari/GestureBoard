import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import time

def set_vol_up():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\volume_increase.ps1"])

def set_vol_down():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\volume_decrease.ps1"])

def volume_control(image, vol_gesture_up, hands, detector):
    function_delay=1.25 #the larger this number the longer it takes to get to desired volume
    if hands:
        fingers = detector.fingersUp(hands[0])
        current_time = time.time()
        
        if fingers == [0, 0, 0, 0, 0]:
            if vol_gesture_up == 0:
                vol_gesture_up = current_time
            elif current_time - vol_gesture_up >= function_delay:  # gesture should be up for 1.25 second to be recognized
                set_vol_up()
                vol_gesture_up = 0  # Reset after performing the action
        elif fingers == [1, 0, 0, 0, 0]:
            if vol_gesture_up == 0:
                vol_gesture_up = current_time
            elif current_time - vol_gesture_up >= function_delay: 
                set_vol_down()
                vol_gesture_up = 0  # Reset after performing the action
        else:
            vol_gesture_up = 0  # Reset if the gesture is not held
    return image, vol_gesture_up

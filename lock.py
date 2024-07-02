import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import time

def set_lock():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\lock.ps1"])

def lock_system(image, lock_gesture_up, hands, detector):
    function_delay=2
    if hands:
        fingers = detector.fingersUp(hands[0])
        if fingers == [1, 1, 0, 1, 1]:  # Specific gesture for locking system
            if lock_gesture_up == 0:
                lock_gesture_up = time.time()  # Start timing the gesture
            elif time.time() - lock_gesture_up >= function_delay:
                set_lock()
        else:
            lock_gesture_up = 0  # Reset if the gesture is not maintained
    else:
        lock_gesture_up = 0  # Reset if no hands are detected
    return image, lock_gesture_up

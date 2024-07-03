import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
from datetime import datetime
import time

def screenshot_func(image, ss_time, hands, detector):
    function_delay =5
    if hands:
        fingers = detector.fingersUp(hands[0])
        lmList = hands[0]['lmList']
        # Screenshot gesture
        if fingers == [1, 1, 1, 1, 0]:  # first 3 fingers up
            current_time = time.time()
            if current_time - ss_time >= function_delay: #there should be atleast 5 seconds between 2 screenshots
                print(f"Current time: {current_time}, Last screenshot time: {ss_time}")
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"image_{timestamp}.png"  # formatted string
                im1 = pyautogui.screenshot(filename)
                print(f"Screenshot taken: {filename}")
                ss_time = current_time
    return image, ss_time

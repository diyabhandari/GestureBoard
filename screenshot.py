import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
from datetime import datetime
import time

def screenshot_func():
    detector = HandDetector(detectionCon=0.6, maxHands=1)
    cap = cv2.VideoCapture(0)
    ss_delay=0
    ss_delay_duration=2
    while True:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        hands, image = detector.findHands(image, flipType=False)
        if hands:
            fingers = detector.fingersUp(hands[0])
            lmList = hands[0]['lmList']
            # Screenshot gesture
            if fingers == [1, 1, 1, 1, 0]:  # first 4 fingers up
                current_time = time.time()
                if current_time - ss_delay >= ss_delay_duration:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"image_{timestamp}.png" #formatted string
                    im1 = pyautogui.screenshot(filename)
                    print(f"Screenshot taken: {filename}")
                    ss_delay = current_time
        cv2.imshow("GestureBoard", image)
        key = cv2.waitKey(100)
        if key == 27:  # ESC key to exit
            break
    cap.release()
    cv2.destroyAllWindows()

screenshot_func()

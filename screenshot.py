import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

def screenshot_func():
    gesture_up_time = 0
    gesture_down_time = 0
    function_delay = 1
    brightness = 50
    detector = HandDetector(detectionCon=0.6, maxHands=1)
    cap = cv2.VideoCapture(0)
    while True:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        hands, image = detector.findHands(image, flipType=False)
        if hands:
            fingers = detector.fingersUp(hands[0])
            lmList = hands[0]['lmList']
            # Screenshot gesture
            ##file name must be passed for the screenshot to be saved, otherwise the function will simply return an image object
            if fingers == [1, 1, 1, 1, 1]:  # All fingers up
                pyautogui.screenshot("image1.png")
                print("Screenshot taken")
        cv2.imshow("GestureBoard", image)
        key = cv2.waitKey(100)
        if key == 27:  # ESC key to exit
            break
    cap.release()
    cv2.destroyAllWindows()
screenshot_func()

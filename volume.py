import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import time

def set_vol_up():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\volume_increase.ps1"])

def set_vol_down():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\volume_decrease.ps1"])

def volume_control():
    gesture_up_time = 0
    gesture_down_time = 0
    function_delay = 1
    detector = HandDetector(detectionCon=0.6, maxHands=1)
    cap = cv2.VideoCapture(0)

    while True:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        hands, image = detector.findHands(image, flipType=False)
        
        if hands:
            fingers = detector.fingersUp(hands[0])
            
            if fingers == [0, 0, 0, 0, 0]:  #sideways thumbs up
                if gesture_up_time == 0:
                    gesture_up_time = time.time()
                elif time.time() - gesture_up_time >= function_delay:
                    set_vol_up()
                    gesture_up_time = 0  #reset after performing the action
            else:
                gesture_up_time = 0  #reset if the gesture is not held

            if fingers == [1, 0, 0, 0, 0]:  #all fingers down
                if gesture_down_time == 0:
                    gesture_down_time = time.time()
                elif time.time() - gesture_down_time >= function_delay:
                    set_vol_down()
                    gesture_down_time = 0  #reset after performing the action
            else:
                gesture_down_time = 0  #reset if the gesture is not held

        cv2.imshow("GestureBoard", image)
        key = cv2.waitKey(100)
        if key == 27:  # ESC key to exit
            break

    cap.release()
    cv2.destroyAllWindows()

volume_control()

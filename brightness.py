import cv2
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc
from math import hypot
from numpy import interp
import time

def brightness_control(image, brightness_gesture_up, hands, detector):
    function_delay = 3
    if hands:
        lmList1 = hands[0]['lmList']
        fingers = detector.fingersUp(hands[0])
        thumb_x, thumb_y = lmList1[4][0], lmList1[4][1]
        ind_x, ind_y = lmList1[8][0], lmList1[8][1]
        
        if fingers == [0, 1, 0, 0, 0]:
            if brightness_gesture_up == 0:
                brightness_gesture_up = time.time()
            elif time.time() - brightness_gesture_up >= function_delay:
                cv2.line(image, (thumb_x, thumb_y), (ind_x, ind_y), (255, 0, 0), 3)  # 3 -> thickness
                length = hypot(ind_x - thumb_x, ind_y - thumb_y)  # distance from origin to coordinate
                bright = interp(length, [15, 160], [0, 100])  # interpolation
                # 15-160 is min-max distance between fingers
                sbc.set_brightness(int(bright))
        else:
            brightness_gesture_up = 0
    else:
        brightness_gesture_up = 0

    return image, brightness_gesture_up



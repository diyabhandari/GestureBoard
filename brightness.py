import cv2
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc
from math import hypot
from numpy import interp
import time

def brightness_control():
    gesture_up_time = 0
    function_delay = 4
    detector = HandDetector(detectionCon=0.6, maxHands=1)
    cap = cv2.VideoCapture(0)

    while True:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        hands, image = detector.findHands(image, flipType=False)
        
        if hands:
            lmList1 = hands[0]['lmList']
            fingers = detector.fingersUp(hands[0])
            thumb_x,thumb_y = lmList1[4][0],lmList1[4][1] 
            ind_x,ind_y = lmList1[8][0],lmList1[8][1]  
            if fingers == [0,1,0,0,0]:
              if gesture_up_time ==0:
                gesture_up_time = time.time()
              elif time.time() - gesture_up_time >= function_delay:
                cv2.line(image,(thumb_x,thumb_y),(ind_x,ind_y),(255,0,0),3) #3 -> thickness
                length = hypot(ind_x-thumb_x,ind_y-thumb_y) #distance from origin to coordinate
                bright = interp(length,[15,160],[0,100]) #interpolation
                #15-160 is min-max distance between fingers
                sbc.set_brightness(int(bright)) 
            else:
               gesture_up_time=0
        else:
           gesture_up_time=0

        cv2.imshow("GestureBoard", image)
        key = cv2.waitKey(100)
        if key == 27:  # ESC key to exit
            break

    cap.release()
    cv2.destroyAllWindows()

brightness_control()

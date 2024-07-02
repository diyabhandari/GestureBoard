import cv2
import time
from virtual_mouse import virtual_mouse
from volume import volume_control
from brightness import brightness_control
from screenshot import screenshot_func
from lock import lock_system
from shutdown import shut_system
from restart import restart_system
from cvzone.HandTrackingModule import HandDetector

def main():
    cap = cv2.VideoCapture(0)
    cap_w = 640
    cap_h = 480
    cap.set(3, cap_w)  # 3 -> width
    cap.set(4, cap_h)  # 4 -> height

    detector = HandDetector(detectionCon=0.9, maxHands=1)  # Create a single instance of HandDetector

    #Delay times for each gesture
    l_click_time = 0  # the time at which left click is done
    r_click_time =0
    vol_gesture_up = 0  # the time for which volume gesture is up
    brightness_gesture_up =0
    ss_time=0
    lock_gesture_up=0
    shut_gesture_up=0
    restart_gesture_up=0

    while True:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        hands, image = detector.findHands(image, flipType=False)  #single detector needed for all functions

        #Functions
        image, l_click_time = virtual_mouse(image, l_click_time, r_click_time, hands, detector)
        image, vol_gesture_up = volume_control(image, vol_gesture_up, hands, detector)
        image, brightness_gesture_up = brightness_control(image, brightness_gesture_up, hands, detector)
        image, ss_time = screenshot_func(image, ss_time, hands, detector)
        image, lock_gesture_up= lock_system(image,lock_gesture_up,hands,detector)
        image, shut_gesture_up = shut_system(image,shut_gesture_up,hands,detector)
        image, restart_gesture_up = restart_system(image,restart_gesture_up,hands,detector)

        cv2.imshow("GestureBoard", image)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

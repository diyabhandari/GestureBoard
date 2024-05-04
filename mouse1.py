import cv2
import mediapipe as m
import pyautogui as p
import time
indexx=0
thumby=0
indexy=0
thumbx=0
hands= m.solutions.hands.Hands()
drawing_utils=m.solutions.drawing_utils
cap=cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame=cv2.flip(frame,1)
    frame_height, frame_width,_ = frame.shape
    sw,sh=p.size()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=hands.process(rgb_frame)
    hand=output.multi_hand_landmarks
    if hand:
        for h in hand:
            drawing_utils.draw_landmarks(frame, h)
            landmarks= h.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                if id==8:
                    cv2.circle(img=frame, center=(x,y),radius=35, color=(255,255,255))
                    indexx=int(sw/frame_width*x)
                    indexy=int(sh/frame_height*y)
                    p.moveTo(indexx,indexy)
                if id==4:
                    cv2.circle(img=frame, center=(x,y),radius=35, color=(255,255,255))
                    thumbx=int(sw/frame_width*x)
                    thumby=int(sh/frame_height*y)  
                if abs(indexy-thumby) <  25:
                     p.click()
                     p.sleep(1)
    time.sleep(0)
                



    cv2.imshow("virtual_mouse_demo1",frame)
    cv2.waitKey(1)
 

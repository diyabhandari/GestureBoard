import cv2
import time
from cvzone.HandTrackingModule import HandDetector # pip install cvzone (see github repo)
import mouse # pip install mouse
from numpy import interp
from win32api import GetSystemMetrics

def virtual_mouse(image, l_click_time,r_click_time, hands, detector):
  frameR = 100  # to solve jittering near the edges of the display window, we'll reduce its size by this much
  cv2.rectangle(image, (frameR, frameR), (image.shape[1] - frameR, image.shape[0] - frameR), (255, 0, 255), 2)
  if hands:
      lmList1 = hands[0]['lmList']
      ind_x, ind_y = lmList1[8][0], lmList1[8][1]
      mid_x, mid_y = lmList1[12][0], lmList1[12][1]
      ring_x,ring_y = lmList1[16][0],lmList1[16][1]
      cv2.circle(image, (ind_x, ind_y), 5, (0, 255, 255), 2)
      fingers = detector.fingersUp(hands[0])
      #drag
      if fingers == [1, 1, 0, 0, 0]:
          conv_x = int(interp(ind_x, (frameR, image.shape[1] - frameR), (0, GetSystemMetrics(0))))
          conv_y = int(interp(ind_y, (frameR, image.shape[0] - frameR), (0, GetSystemMetrics(1))))
          mouse.move(conv_x, conv_y)
      #left click
      if fingers == [1, 1, 1, 0, 0]:
          if abs(ind_x - mid_x) < 50 and time.time() - l_click_time > 1:  # there should be at least 1 second between 2 clicks
              mouse.click(button="left")
              l_click_time = time.time()
      #right click   
      if fingers == [1, 0, 1, 1, 1]:
          if abs(mid_x-ring_x)<40 and time.time()-r_click_time >1:
              mouse.click(button="right")
              r_click_time = time.time()
              
  return image, l_click_time


import cv2
import threading
import time
from cvzone.HandTrackingModule import HandDetector #pip install cvzone (see github repo)
import mouse #pip install mouse
from numpy import interp
from win32api import GetSystemMetrics
#turn off frame

def virtual_mouse():
  detector = HandDetector(detectionCon=0.9,maxHands=1) ##detection confidence
  cap = cv2.VideoCapture(0)
  cap_w = 640
  cap_h = 480
  cap.set(3,cap_w) #3-> width 4->height of video capture object
  cap.set(4,cap_h)
  frameR = 100 #to solve jittering near the edges of the display window, we'll reduce its size by this much
  l_delay =0 #1 when left click, turns back to 0 when set time after click is elapsed
  #this will solve multiple clicks, as there was no time put after each click it kept detecting a single click as many
  def l_click_delay():
    global l_delay
    global l_click_thread #brought inside the scope of this function by declaring as global
    time.sleep(1)
    l_delay=0 #set to 0 after 1 sec, means we can left click again after 1 sec
    l_click_thread = threading.Thread(target=l_click_delay)
    
  l_click_thread = threading.Thread(target=l_click_delay)


  while True:
    success,image = cap.read()
    image = cv2.flip(image,1)
    ##extract all information regarding our hands. right or left hand ? processed image
    hands, image = detector.findHands(image,flipType=False) #we alr flipped with cv2
    cv2.rectangle(image,(frameR,frameR),(cap_w-frameR,cap_h-frameR),(255,0,255),2) ##visualize region in which mouse gesture is detected

    ##we will use the INDEX_FINGER_TIP, 8, for the mouse
    #if hand is present in frame 
    if hands:
      lmList1 = hands[0]['lmList'] #store all 21 landmarks of the first hand detected in a list
      ind_x,ind_y = lmList1[8][0],lmList1[8][1] #8 - > index finger, 0 and 1 give coordinates
      mid_x,mid_y = lmList1[12][0],lmList1[12][1]
      #encircle tip to highlight it
      cv2.circle(image,(ind_x,ind_y),5,(0,255,255),2)
      fingers = detector.fingersUp(hands[0])
      #print(fingers)
      #we want only the index finger to be up for the mouse to activated 
      #because we flipped the livestream, it examines the left hand as it would the right, when thumb is open itll detect it as closed
      #indexing of fingers array starts from thumb

      #drag
      if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0:
        #didnt specify for 3,4 cuz you cant have 2 closed but those oepn
        #conv coordinates of tip of index finger wrt screen size of the device
        conv_x = int(interp(ind_x,(frameR,cap_w-frameR),(0,GetSystemMetrics(0))))
        conv_y = int(interp(ind_y,(frameR,cap_h-frameR),(0,GetSystemMetrics(1))))
        ##pass new coordinates 
        mouse.move(conv_x,conv_y)

      #click when index and middle finger are close
      if fingers[1]==1 and fingers[2] == 1 and fingers[0] ==1:
        if abs(ind_x-mid_x)<25:
          if l_delay==0:
            mouse.click(button="left")
            l_delay=1
            l_click_thread.start()
    cv2.imshow("mouse4",image)
    key = cv2.waitKey(100)
    if key ==27:
      break

  cap.release()
  cv2.destroyAllWindows()
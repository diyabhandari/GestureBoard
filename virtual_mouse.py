import cv2
import time
from cvzone.HandTrackingModule import HandDetector # pip install cvzone (see github repo)
import mouse # pip install mouse
from numpy import interp
from win32api import GetSystemMetrics

def virtual_mouse():
  # Initialize hand detector and video capture
  detector = HandDetector(detectionCon=0.9, maxHands=1)
  cap = cv2.VideoCapture(0)
  cap_w = 640
  cap_h = 480
  cap.set(3, cap_w) # 3 -> width, 4 -> height of video capture object
  cap.set(4, cap_h)
  # Parameters to avoid jittering near the edges
  frameR = 100 
  # Variables for click delay
  l_click_delay_time = 0
  l_click_delay_duration = 1 # 1 second delay

  while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    
    # Extract hand information
    hands, image = detector.findHands(image, flipType=False) # We already flipped with cv2
    cv2.rectangle(image, (frameR, frameR), (cap_w - frameR, cap_h - frameR), (255, 0, 255), 2) # Visualize region in which mouse gesture is detected

    if hands:
      lmList1 = hands[0]['lmList'] # Store all 21 landmarks of the first hand detected in a list
      ind_x, ind_y = lmList1[8][0], lmList1[8][1] # 8 -> index finger, 0 and 1 give coordinates
      mid_x, mid_y = lmList1[12][0], lmList1[12][1]

      # Encircle tip to highlight it
      cv2.circle(image, (ind_x, ind_y), 5, (0, 255, 255), 2)
      fingers = detector.fingersUp(hands[0])
      #print(fingers)
      #we want only the index finger to be up for the mouse to activated 
      #because we flipped the livestream, it examines the left hand as it would the right, when thumb is open itll detect it as closed
      #indexing of fingers array starts from thumb

      # Drag: Only index and thumb fingers up
      if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0:
        # Convert coordinates of tip of index finger with respect to screen size of the device
        conv_x = int(interp(ind_x, (frameR, cap_w - frameR), (0, GetSystemMetrics(0))))
        conv_y = int(interp(ind_y, (frameR, cap_h - frameR), (0, GetSystemMetrics(1))))
        ##pass new coordinates 
        mouse.move(conv_x, conv_y)

      # Click: Index and middle finger are close
      if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1:
        if abs(ind_x - mid_x) < 50:
            current_time = time.time()
            if current_time - l_click_delay_time >= l_click_delay_duration: # there should be at least 1 second between two clicks
                mouse.click(button="left")
                l_click_delay_time = current_time 
      cv2.imshow("mouse4", image)
      key = cv2.waitKey(100)
      if key == 27: # ESC key to exit
          break
  cap.release()
  cv2.destroyAllWindows()

virtual_mouse()

import cv2
from cvzone.HandTrackingModule import HandDetector
##from numpy import interp
def volume_control():
  detector = HandDetector(detectionCon=0.9,maxHands=1) ##detection confidence
  cap = cv2.VideoCapture(0)
  while True:
    success,image = cap.read()
    image = cv2.flip(image,1)
    hands, image = detector.findHands(image,flipType=False) #we alr flipped with cv2
    if hands:
      lmList1 = hands[0]['lmList'] #store all 21 landmarks of the first hand detected in a list
      #thumbd up -> volume up, will turn up volume as long as that thumb is up, in increments of 1-2 ?
      #similar for thumbs down, but must learn how to detect thumbs up and down separately

      #store coordinates of thumb
      thumb_x = lmList1[4][0]
      thumb_y= lmList1[4][1]
      fingers = detector.fingersUp(hands[0]) # fingers that are up or down in the first hand that appears on cam
      if fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
        cv2.circle(image,(thumb_x,thumb_y),5,(0,255,255),2)

    
    cv2.imshow("mouse",image)
    key = cv2.waitKey(100)
    if key ==27:
      break

  cap.release()
  cv2.destroyAllWindows()

import cv2
from cvzone.HandTrackingModule import HandDetector #pip install cvzone (see github repo)
import mouse #pip install mouse

detector = HandDetector(detectionCon=0.9,maxHands=1) ##detection confidence

cap = cv2.VideoCapture(0)
while True:
  success,image = cap.read()
  image = cv2.flip(image,1)
  ##extract all information regarding our hands. right or left hand ? processed image
  hands, image = detector.findHands(image,flipType=False) #we alr flipped with cv2

  ##we will use the INDEX_FINGER_TIP, 8, for the mouse
  #if hand is present in frame 
  if hands:
    lmList1 = hands[0]['lmList'] #store all 21 landmarks of the first hand detected in a list
    ind_x,ind_y = lmList1[8][0],lmList1[8][1] #8 - > index finger, 0 and 1 give coordinates
    #encircle tip to highlight it
    cv2.circle(image,(ind_x,ind_y),5,(0,255,255),2)
  cv2.imshow("mouse4",image)
  key = cv2.waitKey(100)
  if key ==27:
    break

cap.release()
cv2.destroyAllWindows()
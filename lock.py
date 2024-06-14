import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
def set_lock():
  subprocess.run(["powershell","-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\lock.ps1"])
def lock_system():
  detector = HandDetector(detectionCon=0.6,maxHands=1) ##detection confidence, needs to be low for faster reponse here
  cap = cv2.VideoCapture(0)
  while True:
    success,image = cap.read()
    image = cv2.flip(image,1)
    hands, image = detector.findHands(image,flipType=False) #we alr flipped with cv2
    if hands:
      lmList1 = hands[0]['lmList'] #store all 21 landmarks of the first hand detected in a list
##################################################
      fingers = detector.fingersUp(hands[0]) # fingers that are up or down in the first hand that appears on cam
      mid_x = lmList1[12][0]
      thumb_x= lmList1[4][0]
      if fingers[0]==1 and fingers[1]==1 and fingers[3]==1 and fingers[4]==1 and fingers[2]==0: #kind of like a flick
        set_lock()
    cv2.imshow("GestureBoard",image)
    key = cv2.waitKey(100)
    if key ==27:
      break
  cap.release()
  cv2.destroyAllWindows()
lock_system()
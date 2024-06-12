import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
def set_vol_up():
  subprocess.run(["powershell","-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\volume_increase.ps1"])
def set_vol_down():
  subprocess.run(["powershell","-ExecutionPolicy", "Bypass", "-File", r"C:\Users\diyab\Desktop\GestureBoard\scripts\volume_decrease.ps1"])
def volume_control():
  detector = HandDetector(detectionCon=0.6,maxHands=1) ##detection confidence, needs to be low for faster reponse here
  cap = cv2.VideoCapture(0)
  while True:
    success,image = cap.read()
    image = cv2.flip(image,1)
    hands, image = detector.findHands(image,flipType=False) #we alr flipped with cv2
    if hands:
      lmList1 = hands[0]['lmList'] #store all 21 landmarks of the first hand detected in a list
      #thumbd up -> volume up, will turn up volume as long as that thumb is up, in increments of 1-2 ?
      #similar for thumbs down, but must learn how to detect thumbs up and down separately
##################################################################################
      #store coordinates of thumb
      thumb_x = lmList1[4][0]
      thumb_y= lmList1[4][1]
      fingers = detector.fingersUp(hands[0]) # fingers that are up or down in the first hand that appears on cam
      if fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
        set_vol_up()
        #print("volume up")
      if fingers[0]==1 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0: #thumb flipped, 1 -> its down
        set_vol_down()
        #print("volume down")  
    cv2.imshow("GestureBoard",image)
    key = cv2.waitKey(100)
    if key ==27:
      break

  cap.release()
  cv2.destroyAllWindows()
volume_control()
import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.9,maxHands=1) ##detection confidence

cap = cv2.VideoCapture(0)
while True:
  success,image = cap.read()
  image = cv2.flip(image,1)
  ##extract all information regarding our hands. right or left hand ? processed image
  hands, image = detector.findHands(image,flipType=False) #we alr flipped with cv2
  cv2.imshow("mouse4",image)
  key = cv2.waitKey(100)
  if key ==27:
    break

cap.release()
cv2.destroyAllWindows()
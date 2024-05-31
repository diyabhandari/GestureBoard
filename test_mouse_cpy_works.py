import cv2
import mediapipe as mp
import pyautogui
from google.protobuf.json_format import MessageToDict

pyautogui.FAILSAFE = False
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

class GestureController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Failed to open camera.")

    def start(self):
        with self.cap:
            while True:
                success, image = self.cap.read()
                if not success:
                    print("Failed to read frame.")
                    continue

                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                cv2.imshow('Gesture Controller', image)
                if cv2.waitKey(5) == 27:  # Press 'Esc' to exit
                    break

if __name__ == "__main__":
    try:
        gc = GestureController()
        gc.start()
    except Exception as e:
        print("An error occurred:", e)

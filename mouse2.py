import cv2
import mediapipe as mp
import pyautogui

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))



model_file = open(r"C:\Users\diyab\Downloads\hand_landmarker.task", "rb") #r converts to raw path
model_data = model_file.read()
model_file.close()
    
base_options = BaseOptions(model_asset_buffer=model_data)
options = HandLandmarkerOptions(base_options=base_options,  running_mode=VisionRunningMode.LIVE_STREAM, result_callback=print_result)
detector = HandLandmarker.create_from_options(options) #detector named as landmarker in the doc 
cam=cv2.VideoCapture(0)
while True:
    _,image = cam.read()
    #result = HandLandmarker.detect(image)
    cv2.imshow("virtual_mouse_demo2",image)
    key = cv2.waitKey(100)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
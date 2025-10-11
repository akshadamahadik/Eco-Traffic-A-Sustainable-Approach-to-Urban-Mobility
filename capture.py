import time
import cv2 
def capture(image):
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:
            try:
                check, frame = webcam.read()
                cv2.imwrite(filename="images/"+image, img=frame)
                time.sleep(2)
                webcam.release()
                cv2.waitKey()
                cv2.destroyAllWindows()
                break
        
            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break



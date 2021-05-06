import cv2

cap=cv2.VideoCapture("test.mp4")
#cap=cv2.VideoCapture(0) 


(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.') #Determino Version de OpenCV
#--------Determino fps y tamaño del video----------
if int(major_ver) < 3 :
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS) #revisar porque lo dijo en clase el tema de cv2.cv
    framesize=(cap.get(cv2.cv.CAP_PROP_FRAME_WIDTH),cap.get(cv2.cv.CAP_PROP_FRAME_HEIGHT))
    print("FPS: {0}, Framesize: {1}".format(fps,framesize))
else :
    fps=cap.get(cv2.CAP_PROP_FPS)
    framesize=(cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("FPS: {0}, Framesize: {1}".format(fps,framesize))
#-----------------------------------------
cap.release()


# https://www.javaer101.com/es/article/1026758.html
# https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
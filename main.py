import cv2
import pickle
import cvzone
import numpy as np
import time


width = 40
height = 40

def checkParkingSpace(imgPro): 
    parkingCount = 0
    for pos in posList:
        x,y = pos

        imgCrop = imgPro[y:y+height, x:x+width]
        # cv2.imshow(str(x*y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(count), (x,y+height-10), 1, 2, (255,255,255), (255,0,0))

        t = time.localtime()
        current_time = time.strftime("%H: %M: %S", t)
        if count < 230:
            color = (0,255,0)
            parkingCount += 1
            print("Car departure at " + current_time)
            
        else:
            color = (0,0,255)
            print("Car arrival at " + current_time)

        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height), color, 2)

    cvzone.putTextRect(img, str(parkingCount), (1100,100), 2, 2, (0,0,0), (205,255,100))


cap = cv2.VideoCapture('carPark.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES, 5250)

try:
    with open('CarParkPos','rb') as f:
        posList = pickle.load(f)

except:
    posList = []

while True:

    
    success, imgOG = cap.read()
    img = cv2.resize(imgOG,(1270,700))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 15)

    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    # cv2.imshow("Comparator", imgBlur)
    # cv2.imshow("Threshold", imgThreshold)
    cv2.waitKey(1)

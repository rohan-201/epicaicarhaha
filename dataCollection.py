import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

myDirectory = os.path.join(os.getcwd(), '')

while os.path.exists(os.path.join(myDirectory, f'IMG{str(countFolder)}')):
    countFolder += 1

newPath = myDirectory + "/IMG" + str(countFolder)
os.makedirs(newPath)

def saveData(img, steering):
    global imgList, steeringList
    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).replace(".", "")
    fileName = os.path.join(newPath, f"Image_{timestamp}.png")
    cv2.imwrite(fileName, img)
    imgList.append(fileName)
    steeringList.append(steering)

def savedLog():
    global imgList, steeringList
    rawData = {'Image': imgList, "Steering": steeringList}
    df = pd.DataFrame(rawData)
    df.to_csv(os.path.join(myDirectory, f'log_{str(countFolder)}.csv'), header=False, index=False)
    print("Log saved, total images: ", len(imgList))

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    for x in range(10):
        _, img = cap.read()
        saveData(img, 0.5)
        cv2.waitKey(1)
        cv2.imshow('Image', img)

    savedLog()



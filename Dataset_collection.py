import cv2
import numpy as np
import os
import time

cap =cv2.VideoCapture(0)
path='B/'
os.mkdir(path)
start=time.time()

# bgdModel =np.zeros((1,65),np.float64)
# fgdModel= np.zeros((1,65), np.float64)
# os.chmod(path,777)
waitime=0
while True:
    ret, img = cap.read()
    # img=np.zeros(img.shape[:2], np.uint8)

    # img=cv2.resize(img, (960, 540))
    # cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
    # cv2.setWindowProperty('frame1', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    img=cv2.rectangle(img,(200,100),(500,400),(0,0,255),2)
    p = cv2.waitKey(30) & 0xff# k = cv2.waitKey(30) & 0xff
        # if k == ord('q'):
        #     break
    if p == ord('a'):
        print("key A is pressed ")
        i=0

        while True:
            ret, img = cap.read()
            img = cv2.rectangle(img, (200, 100), (500, 400), (0, 0, 255), 2)
            crop=img[100:400,200:500]

            cv2.imshow('frame1', img)
            k = cv2.waitKey(30) & 0xff
            if k == ord('q'):
                break
            now=time.time()
            stop=now-start
            if(stop>.3):
                cv2.imwrite(os.path.join(path, '{}.jpg'.format(i)), crop)
                print("saving file {}".format(i))
                start=now
                i=i+1
            if (i >= 99):
                break

        break


    cv2.imshow('frame1', img)
    k = cv2.waitKey(30) & 0xff
    if k == ord('q'):
        break
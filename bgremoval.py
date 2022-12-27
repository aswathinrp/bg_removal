import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
imgBg = cv2.imread("images/one.jpg")

listimg =  os.listdir('images')
print(listimg)
imglist = []
for imgpath in listimg:
    img = cv2.imread(f'images/{imgpath}')
    imglist.append(img)
indeximg=0

    
while True:
    success,img=cap.read()
    imgout = segmentor.removeBG(img,imglist[indeximg],threshold=0.85)
    imageStacked = cvzone.stackImages([img,imgout],2,1)
    _,imageStacked = fpsReader.update(imageStacked)
    
    cv2.imshow('image',img)
    cv2.imshow('image out',imgout)
    key = cv2.waitKey(1)
    
    if key == ord('a'):
        indeximg -=1
    elif key == ord('d'):
        indeximg +=1
        
    elif key == ord('q'):
        break
        
        
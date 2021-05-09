import cv2
import numpy as np

img= cv2.imread('hand2.jpeg')
# cv2.rectangle(img, (100, 300), (500, 720), (0, 0, 255), 2)
# cv2.rectangle(img, (400, 50), (800, 475), (0, 0, 255), 2)
mask =np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect=(400,50,800,475)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2=np.where((mask==2) | (mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
cv2.imshow('frame1',img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()

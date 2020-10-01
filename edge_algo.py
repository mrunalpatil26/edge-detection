import cv2
import numpy as np
from matplotlib import pyplot as plt
from glob import glob

def edge_detection(mypath):
    for fn in glob(mypath + "\\*.jpg"):
        img = cv2.imread(fn)
        #resize = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mblur = cv2.medianBlur(gray, 5)
        gblur = cv2.GaussianBlur(gray,(5,5),0)
        edges = cv2.Canny(gblur,100,200)
        sobelx = cv2.Sobel(gblur,cv2.CV_64F,1,0,ksize=-1)  # x
        sobely = cv2.Sobel(gblur,cv2.CV_64F,0,1,ksize=-1)  # y
        kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        img_prewittx = cv2.filter2D(gblur, -1, kernelx)
        img_prewitty = cv2.filter2D(gblur, -1, kernely)
        
                
        plt.subplot(1,6,1),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        #plt.subplot(1,4,2),plt.imshow(gray,cmap = 'gray')
        #plt.title('gray Image'), plt.xticks([]), plt.yticks([])
        #plt.subplot(1,4,3),plt.imshow(gblur,cmap = 'gray')
        #plt.title('mblur Image'), plt.xticks([]), plt.yticks([])
        #plt.subplot(4,1,4),plt.imshow(mblur,cmap = 'gray')
        #plt.title('gblur Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,6,2),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,6,3),plt.imshow(sobelx,cmap = 'gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,6,4),plt.imshow(sobely,cmap = 'gray')
        plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,6,5),plt.imshow(sobely,cmap = 'gray')
        plt.title('prewitt x'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,6,6),plt.imshow(sobely,cmap = 'gray')
        plt.title('prewitt y'), plt.xticks([]), plt.yticks([])
        
        
        plt.show()

edge_detection("Pothole_dataset")

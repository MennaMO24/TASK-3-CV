import cv2
import numpy as np

image =cv2.imread("C:/Users/FreeComp/Downloads/Documents/folders/folders/folder1/1.jpg")
#image =cv2.imread("C:/Users/FreeComp/Downloads/Documents/folders/folders/folder2/1.jpg")
#image =cv2.imread("C:/Users/FreeComp/Downloads/Documents/folders/folders/folder3/1.jpg")
#image =cv2.imread("C:/Users/FreeComp/Downloads/Documents/folders/folders/folder4/1.jpg")
#image =cv2.imread("C:/Users/FreeComp/Downloads/Documents/folders/folders/folder5/1.jpg")
def avg_blur():
    blured=np.hstack([image,
                     cv2.blur(image,(3,3)),
                     cv2.blur(image,(5,5)),
                     cv2.blur(image,(7,7)),
                     cv2.blur(image,(13,13))])
    cv2.imshow("Avg_blured",blured)
    cv2.waitKey(0)

def guass_blur():
    g_blured=np.hstack([image,
                     cv2.GaussianBlur(image,(3,3),0),
                     cv2.GaussianBlur(image,(5,5),0),
                     cv2.GaussianBlur(image,(7,7),0),
                     cv2.GaussianBlur(image,(13,13),0)])
    cv2.imshow("Gaussian_Blur",g_blured)
    cv2.waitKey(0)

def median_blur():
    m_blured=np.hstack([image,
                     cv2.medianBlur(image,3),
                     cv2.medianBlur(image,5),
                     cv2.medianBlur(image,7),
                     cv2.medianBlur(image,13)])
    cv2.imshow("Median_Blur",m_blured)
    cv2.waitKey(0)

def bilateral():
    b_blured = np.hstack([image,
                     cv2.bilateralFilter(image, 5, 21, 21),
                     cv2.bilateralFilter(image, 7, 31, 31),
                     cv2.bilateralFilter(image, 9, 41, 41),
                     cv2.bilateralFilter(image, 12, 51, 51)])
    cv2.imshow("bilateral", b_blured)
    cv2.waitKey(0)


avg_blur()
guass_blur()
median_blur()
bilateral()
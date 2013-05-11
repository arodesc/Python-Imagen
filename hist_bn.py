import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('/home/arodesc/Imágenes/IMG_4649.JPG',0) #carga de imagen
#hist=np.zeros([180,256,3],'uint8')
hist=cv2.calcHist(img, [0], None,[256],[0,256])
plt.plot(hist)
plt.show()

        

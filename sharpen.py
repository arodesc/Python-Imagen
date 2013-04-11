import numpy as np
import cv2
from scipy import ndimage, signal

            #filtro de enfoque
            # -*- coding: utf-8 -*-

def gauss2d(k, std):            #gaussiana bidimensional
        rows=2*k+1
        cols=2*k+1
        gaussian1d=signal.gaussian(cols,std)  #gaussiana unidimensional
        kernel_gauss=np.ndarray((rows,cols),"float") #mascara/kernel
        for i in range(0,rows):
                for j in range(0,cols):
                        kernel_gauss[i,j]=gaussian1d[i]*gaussian1d[j]    
        kernel_gauss=kernel_gauss/kernel_gauss.sum() #normalizacion de la gaussiana
        return kernel_gauss

def conv2d(img, krnl):          #convolucion bidimensional
        rows=img.shape[0]-krnl.shape[0]+1
        cols=img.shape[1]-krnl.shape[1]+1
        output=np.ndarray((rows,cols), "float")
        kernel_reversed=np.rot90(np.rot90(kernel))
        for i in range(0, output.shape[0]):
                for j in range(0, output.shape[1]):
                        img_patch=img[i:i+len(krnl),j:j+len(krnl)]
                        y=max((kernel_reversed*img_patch).sum(),0)
                        z=min(y,255)
                        output[i,j]=z
        return output

def sharp(k,std):   #creación de la mascara de enfoque            
        rows=2*k+1
        cols=2*k+1
        kernel_g=gauss2d(k,std)
        kernel=np.zeros((rows,cols),"float")
        kernel[k,k]=2
        kernel=kernel-kernel_g
        return kernel

def apply_filter(image, kernel):                #rutina para aplicarle el filtro a la imagen
        if len(img.shape) == 2:                         #blanco y negro (1 canal y transparencia)
                img_filt = conv2d(img, kernel)
        else:                                           #color (3 canales y transparencia)
                img_filt = []
                for channel in range(img.shape[2]):
                    img_filt.append(conv2d(img[:,:,channel], kernel))
                img_filt = cv2.merge(img_filt)
        return img_filt


k=5        #radio de la gaussiana
std=3.0     #desviacion estandar de la gaussiana
img=cv2.imread('/media/arodesc/USB DISK/Fotos SSanta_2013/IMG_4643d.jpg')       #leer imagen
img=img.astype("float")
kernel=sharp(k,std)
img_filt=apply_filter(img, kernel)
cv2.imwrite('/media/arodesc/USB DISK/Fotos SSanta_2013/IMG_4643d_enf.jpg',img_filt) #escribir imagen

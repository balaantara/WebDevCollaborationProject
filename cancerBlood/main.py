import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random
import os
import cv2

from imutils import paths
from PIL import Image
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.layers import Dense, Dropout
from keras.layers import GlobalAveragePooling2D,BatchNormalization
from sklearn.model_selection import train_test_split

class bld():
    def __init__(self) -> None:
        pass

    def img_dir(self):
        dr = "./Blood_Cancer/"
        dir = os.listdir("./Blood_Cancer/")

        return dir

    def image_resize(self):
        dir = "./Blood_Cancer/"
        Img = self.img_dir()

        image = []
        for i in range(10):
            img = cv2.imread(f"{dir}{Img[i]}")
            # img = cv2.resize(img, (200,200))

            imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgBlur = cv2.GaussianBlur(imgGrey, (7,7), 0)

            data = np.asarray(imgBlur)
            print(repr(data[1]))

            # # image.append(img_to_array)
            # plt.imshow(imgBlur)
            # plt.show()

        return image
    def opn(self):
        dr = os.listdir("./Blood_Cancer/")

        img = []
        for i in range(5):
            img.append(dr[i])

        # print(img)

        new_img = []

        for i in range(len(img)):
            Img = cv2.imread(f"./Blood_Cancer/{img[i]}")
            # print(f"./Blood_Cancer/{img[i]}")
            new_img.append(Img)

            img_gray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
            # print(img_gray)

            ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
            # print(thresh)
            new_img.append(thresh)
            print(thresh)

            thresh = 255-thresh

            contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
                                     
            img_copy = Img.copy()
            cv2.drawContours(image=img_copy, contours=contours, contourIdx=-1, color=(255, 200, 200), thickness=1, lineType=cv2.LINE_AA)
            new_img.append(img_copy)

        # print(new_img)
        return new_img


    def show(self):
        data = self.opn()
        plt.figure(figsize=(20,20))
        for i, img in enumerate(data):
            
            plt.subplot(5,5,i+1)
            plt.grid(False)
            plt.imshow(img)

        plt.show()

        
if __name__ == "__main__":
    d = bld()
    d.img_dir()
    d.image_resize()
    d.opn()
    d.show()

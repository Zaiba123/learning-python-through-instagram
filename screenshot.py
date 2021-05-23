import numpy as np
import cv2
import pyautogui

#pyautogui takes pictures as python image library which you can manipulate
image = pyautogui.screenshot()

#This step allows us to convert the image from RGB to BGR which is how imread() reads it
#and can write it to the disk
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

#This step takes the BGR numpy array and writes to the disk
cv2.imwrite("screenshot.png", image)


#SCREENSHOT WORKED YAY
import ctypes
import os
from re import X
from django.urls import translate_url
import keyboard
import time
import win32api,win32gui
import mss
import PIL.ImageGrab
import PIL.Image
import winsound
import pyautogui
import threading
from interception import  *
from constants import *
from PIL import Image
import PIL
from pytesseract import *
import keyboard
import random
import win32api, win32con
import time
import mouse


#while True:

    # def dot2(): #gets and stores image as Dot2
    #     im2 = pyautogui.screenshot(region=(955, 535, 15, 15))
    #     im2.save(r"C:\Users\mnawe_000\Desktop\Idya\Dot2.png")
    #     img2 = "Dot2.png"

    # dot2()
    # dif = (os.stat('Dot.png').st_size)-(os.stat('Dot2.png').st_size)
    # print(dif)



# def c1():
#     print("1")
# def c2():
#     print("2")
# def c3():
#     print("3")
# def c4():
#     print("4")
# def c5():
#     print("hi")

# def gc():
#     g = "c"+str(random.randrange(1, 5))
#     t = str(g.replace(" ",""))
#     print()
#     l = globals()[t]()
#     return l

# for i in range(random.randint(0, 5)):
#     gc()


mouse.press()
mouse.release()
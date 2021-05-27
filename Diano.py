import pyautogui #pip install pyautogui
from PIL import Image,ImageGrab #pip install pillow
import time
pyautogui.FAILSAFE = True

def hit(key):
    pyautogui.press(key)
    
def isCollide(data):
    for i in range(240,290):
        for j in range(340,375):
            if data[i,j]<100:
                pyautogui.keyDown('down')
                time.sleep(0.3)
                pyautogui.keyUp('down')
                return
        
    
    for i in range(260,290):
        for j in range(345,440):
            if data[i,j]<100:
                pyautogui.press('up')
                return
    return
    
def isCollide2(data):
    for i in range(240,290):
        for j in range(340,375):
            if data[i,j]>1:
                pyautogui.keyDown('down')
                time.sleep(0.3)
                pyautogui.keyUp('down')
                return
    
    for i in range(260,290):
        for j in range(345,440):
            if data[i,j]>1:
                pyautogui.press('up')
                return            
                

if __name__=='__main__':
    print("Hey. Dino game about to start in 3 seconds")
    time.sleep(2)
    pyautogui.keyDown('down')
    time.sleep(0.2)
    pyautogui.keyUp('down')
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        
        c=data[100,100]
        if c>100:
            isCollide(data)
        else:
            isCollide2(data)   
        '''
        #Draw the rectangle for cactus
        for i in range(260,290):
            for j in range(378,440):
                data[i,j]=0
        
        #Draw the rectangle for checking black screen
        data[100,100]=254
        
        #Draw the area for bird
        for i in range(240,290):
            for j in range(340,375):
                data[i,j]=56
        
       
        image.show()
        
        break
        '''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as gui
from PIL import Image, ImageGrab 
import time 
import numpy as np
from io import BytesIO
import cv2
import matplotlib.pyplot as plt
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')


website='https://offline-dino-game.firebaseapp.com/'
path='/home/kevit/Downloads/chromedriver-linux64/chromedriver'
cService = webdriver.ChromeService(executable_path=path)
driver = webdriver.Chrome(service = cService,options=options)
driver.get(website)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "canvas.runner-canvas")))

canvas = driver.find_element(By.CSS_SELECTOR,'.runner-canvas')
main_body = driver.find_element(By.XPATH,"//body") 


def click(key):
    if key=='down':
        main_body.send_keys(Keys.ARROW_DOWN)
    if key=='up':
        main_body.send_keys(Keys.ARROW_UP)
        main_body.send_keys(Keys.ARROW_DOWN)
        
        

def isCollision(data):

    cactii=data[195:237,200:240]
    bird=data[120:165,160:205]
    cv2.imwrite('DinoGame/cactii.png', cactii) 
    cv2.imwrite('DinoGame/bird.png', bird)
    avg_cactii=np.mean(cactii)
    avg_bird=np.mean(bird)
    if avg_cactii<240:
        print(f'avg_cactii: {avg_cactii}')
        click("up")
        return  
      
    if avg_bird<240:
        print('avg_bird: {avg_bird}')
        click("down")
        return  
      
    return


def main():
    while True:
        main_body.screenshot("DinoGame/bg.png")
        data=cv2.imread("DinoGame/bg.png")
        data=cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        isCollision(data)
        time.sleep(0.05) 

        
if __name__=='__main__':
    time.sleep(1)
    click('up') 
    main()
















# def detect_obstacles():
#     # bbox (xmin, ymin, xmax, ymax)
#     # Get the values for the grab-box by trying
#     xmax = 335
#     width = 65
#     ymax = 620
#     height = 80
#     box = ImageGrab.grab(bbox=(xmax - width, ymax - height, xmax, ymax))
#     colors = [color[1] for color in box.getcolors()]
#     if (172, 172, 172, 255) in colors:
#         return True
#     else:
#         return False












# def getPixel(path,x, y):
#     px = Image.open(path)
#     img_array = np.array(px)
#     return img_array[x, y]

# top, left, width, height = 293, 0, 1920, 465
# screenDimensions = {
#     "top": top,
#     "left": left,
#     "width": width,
#     "height": height
# } 

# y_search, x_start, x_end = 350, 435, 450
# y_search2 = 275 # for the birds

# # ss = ImageGrab.grab(bbox=(left, top, width, height))
# main_body.screenshot("WebScraping/DinoGame/bg.png")
# bgColor=[255,255,255]
# # bgColor = getPixel("WebScraping/DinoGame/bg.png", 440, 30)
 

# main_body.send_keys(Keys.SPACE)
# while True:
#     canvas.screenshot("WebScraping/DinoGame/bg.png")
#     # sct_img = gui.screenshot(region=(left,top, width, height))
#     for i in reversed(range(x_start, x_end)):
#         # if i found a pixel in the search interval with a colour other than the bg colour, then it is an obstacle
#         if getPixel("WebScraping/DinoGame/bg.png",i,y_search) != bgColor\
#                 or getPixel("WebScraping/DinoGame/bg.png",i,y_search2) != bgColor:
#             main_body.send_keys(Keys.SPACE) # jump
#             time.sleep(0.01)
#         time.sleep(0.5)
        




# while True:
#     try:
#         #short jump
#         # ActionChains(driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

#         # long jump
#         ActionChains(driver).key_down(Keys.SPACE).pause(0.2).key_up(Keys.SPACE).perform()
#     except:
#         print("DOne")
#         break
# 






# while True:
#     # try:
#         screenshot = capture_screenshot()
#         if detect_cactus(screenshot):
#             main_body.send_keys(Keys.SPACE)  # Make the dino jump
#             time.sleep(0.1)
#         time.sleep(0.05)
    # except:
    #     print("Done")
    #     break
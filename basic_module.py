from match import matchAndClick, matchAndFlip
import time

def basicClickModules(img_dir, msg):
    flag = False
    while not flag:
        flag = matchAndClick(img_dir)
    
    print(msg + " Succeed.")
        
def basicFlipModules(img_dir, msg):
    flag = False
    while not flag:
        flag = matchAndFlip(img_dir)
    
    print(msg + " Succeed.")
    
START_INTERVAL = 3

def click(dir, msg,intv = START_INTERVAL):
    basicClickModules(dir, msg)
    time.sleep(intv)

def flip(dir, msg,intv = START_INTERVAL):
    basicFlipModules(dir, msg)
    time.sleep(intv)
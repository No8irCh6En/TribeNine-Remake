from match import matchAndClick, matchAndFlip, match_template
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
    
def basicEnsureModules(img_dir, msg):
    flag = False
    while not flag:
        flag, _ = match_template(img_dir)
    
    print(msg + " Found.")
    
START_INTERVAL = 3

def click(dir, msg,intv = START_INTERVAL):
    time.sleep(0.5)
    basicClickModules(dir, msg)
    time.sleep(intv)

def flip(dir, msg, intv = START_INTERVAL):
    basicFlipModules(dir, msg)
    time.sleep(intv)
    
def ensure(dir, msg, intv = START_INTERVAL):
    basicEnsureModules(dir, msg)
    time.sleep(intv)
import time
import os
import numpy as np
import pyautogui
import cv2
from capture import capture_screen
import capture
from match import match_template, matchAndClick, matchAndFlip

START_INTERVAL = 3

def is_start_menu():
    screen = capture_screen()
    menu_dir = "images/start/start-menu.png"
    return match_template(screen, menu_dir)

def click_start_setup():
    screen = capture_screen()
    START_SETUP_DIR = "images/start/start-setup.png"
    is_match, click_pos = match_template(screen, START_SETUP_DIR)
    if is_match:
        pyautogui.click(click_pos)
        print("点开设置")
        return True
    return False
    
def click_delete_accout():
    is_match = False
    while not is_match:
        screen = capture_screen()
        delete_account_dir = "images/start/start-delete.png"
        is_match, click_pos = match_template(screen, delete_account_dir)
        if is_match:
            pyautogui.click(click_pos)
            print("点击删除账号")
    
    time.sleep(START_INTERVAL)
    
    is_delete_ensure = False
    
    while not is_delete_ensure:
        screen = capture_screen()
        delete_ensure_dir = "images/start/delete-ensure.png"
        is_delete_ensure, click_pos = match_template(screen, delete_ensure_dir)
        if is_delete_ensure:
            pyautogui.click(click_pos)
            print("点击确认删除")
            
    time.sleep(START_INTERVAL)
    
    is_delete_ok = False
    
    while not is_delete_ok:
        screen = capture_screen()
        delete_ok_dir = "images/start/delete-ok.png"
        is_delete_ok, click_pos = match_template(screen,delete_ok_dir)
        if is_delete_ok:
            pyautogui.click(click_pos)
            print("删除账号成功")
    
    is_setup_closed = False
    while not is_setup_closed:
        screen = capture_screen()
        close_setup_dir = "images/start/close-setup.png"
        is_setup_closed, click_pos = match_template(screen, close_setup_dir)
        if is_setup_closed:
            pyautogui.click(click_pos)
            print("关闭设置")
    
    
    time.sleep(START_INTERVAL)
    
    return True  

def click_start_game():
    
    is_start_menu = False
    
    while not is_start_menu:  
        screen = capture_screen()
        start_menu_dir = "images/start/start-menu.png"
        is_start_menu, click_pos = match_template(screen, start_menu_dir)
        if is_start_menu:
            pyautogui.click(click_pos)
            print("点开开始游戏")
    
    time.sleep(START_INTERVAL)
    
    return 
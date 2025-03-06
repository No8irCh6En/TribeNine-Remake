import time
import os
import pyautogui
from capture import capture_screen
from match import match_template
from basic_module import click, flip

def is_in_game():
    return

def get_mail_reward():
    mail_dir = "images/in-game/mail.png"
    click(mail_dir, "open-mail")
    
    get_all_dir = "images/in-game/get-all.png"
    click(get_all_dir, "get-all-mail")
    
    ## TODO: click another time and press ESC
    
    ## END TODO, backto set-up page
    

def get_fes_reard():
    ## Assume already in set-up page
    fes_dir = "images/in-game/award-con.png"
    click(fes_dir, "award-page")
    
    award_dir = "images/in-game/award.png"
    click(award_dir, "get-fes-reward")
    
    return

def satis_or_not():
    return

def to_gacha():
    ## Assume already in gacha page
    gacha_page_dir = "images/in-game/gacha-page.png"
    click(gacha_page_dir, "gacha-page")
    
    to_gacha_dir = "images/in-game/to-gacha.png"
    click(to_gacha_dir, "to-gacha")

def gacha():
    return

def back_to_start():
    return
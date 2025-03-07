import time
import pyautogui
from match import match_template
from basic_module import click, flip, ensure

HIGH_RANK_CHARACTER = 0
GACHA_TIMES = 2

def is_in_game():
    in_game_dir = "images/in-game/init.png"
    ensure(in_game_dir, "in-game")

def get_mail_reward():
    
    setup_dir = "images/in-game/set-up.png"
    click(setup_dir, "to-set-up")
    
    mail_dir = "images/in-game/mail.png"
    click(mail_dir, "open-mail")
    
    get_all_dir = "images/in-game/get-all.png"
    click(get_all_dir, "get-all-mail")
    
    ## TODO: click another time and press ESC
    
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
    esc_dir = "images/in-game/esc.png"
    click(esc_dir, "esc")
    
    set_up_dir = "images/in-game/set-up.png"
    click(set_up_dir, "back-to-set-up")
        
    event_dir = "images/in-game/event.png"
    click(event_dir, "to-event")
    ## END TODO, backto set-up page
    

def get_fes_reard():
    ## Assume in event page
    
    fes_dir = "images/in-game/award-con.png"
    click(fes_dir, "award-page")
    
    award_dir = "images/in-game/award.png"
    click(award_dir, "get-fes-reward")

def satis_or_not():
    return (HIGH_RANK_CHARACTER >= 2)

def to_gacha():
    ## Assume already in gacha page
    gacha_page_dir = "images/in-game/gacha-page.png"
    click(gacha_page_dir, "gacha-page")
    pyautogui.click()
    
    to_gacha_dir = "images/in-game/to-gacha.png"
    click(to_gacha_dir, "to-gacha")
    pyautogui.click()


def gacha10times():
    
    global HIGH_RANK_CHARACTER, GACHA_TIMES
    
    gacha_dir = "images/in-game/10-times.png"
    click(gacha_dir, "10-times")
    # pyautogui.click()
    
    gacha_ensure_dir = "images/in-game/gacha-ensure.png"
    click(gacha_ensure_dir, "gacha-ensure")
    
    skip_gacha_dir = "images/in-game/skip-gacha.png"
    click(skip_gacha_dir, "skip-gacha")
    
    new_char_dir = "images/in-game/new-char.png"
    new_tension_dir = "images/in-game/new-tens.png"
    while(match_template(new_char_dir)[0] or match_template(new_tension_dir)[0]):
        pyautogui.click()
        print("click one time")
        time.sleep(0.5)
        
    
    close_gacha_dir = "images/in-game/close-gacha.png"
    click(close_gacha_dir, "close-gacha")
    # pyautogui.click()
    
    star_dir = "images/targets/3-star.png"
    result = match_template(star_dir)
    if result:
        HIGH_RANK_CHARACTER += 1
        

def gacha():
    for _ in range(GACHA_TIMES):
        gacha10times()
        
    ## TODO: back to init page (now in gacha page)
    
    
    ## END TODO

def back_to_start():
    time.sleep(10)
    get_new_dir = "images/in-game/get-new.png"
    while(not match_template(get_new_dir)):
        time.sleep(1)
    
    set_up_dir = "images/in-game/set-up.png"
    click(set_up_dir, "back-to-set-up")
    
    
    mail_dir = "images/in-game/mail.png"
    _, click_pos = match_template(mail_dir)
    pyautogui.click(click_pos)
    
    back_to_dir = "images/in-game/back-to.png"
    flip(back_to_dir)
import pyautogui
from capture import capture_screen
from match import match_template
from basic_module import click

def is_start_menu():
    screen = capture_screen()
    menu_dir = "images/start/start-menu.png"
    return match_template(screen, menu_dir)

def click_start_setup():
    start_setup_dir = "images/start/start-setup.png"
    click(start_setup_dir, "start-setup")
    
def click_delete_accout():
    delete_account_dir = "images/start/start-delete.png"
    click(delete_account_dir, "delete-account")
    
    delete_ensure_dir = "images/start/delete-ensure.png"
    click(delete_ensure_dir, "delete-ensure")

    
    delete_ok_dir = "images/start/delete-ok.png"
    click(delete_ok_dir, "delete-ok")
    
    close_setup_dir = "images/start/close-setup.png"
    click(close_setup_dir, "setup-closed")


def click_start_game():
    
    start_menu_dir = "images/start/start-menu.png"
    click(start_menu_dir, "start-menu")
    
    real_start_dir = "images/start/real-start.png"
    click(real_start_dir, "real-start")
    
    skip_ensure_dir = "images/start/skip-ensure.png"
    click(skip_ensure_dir, "skip-ensure")
    

from basic_module import click, ensure
import time

def is_start_menu():
    menu_dir = "images/start/start-menu.png"
    ensure(menu_dir, "start-menu")

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
    
    time.sleep(2)
    
    close_setup_dir = "images/start/close-setup.png"
    click(close_setup_dir, "setup-closed")


def click_start_game():
    
    start_menu_dir = "images/start/start-menu.png"
    click(start_menu_dir, "start-menu")
    
    skip_ensure_dir = "images/start/skip-ensure.png"
    click(skip_ensure_dir, "skip-ensure")
    
    real_start_dir = "images/start/real-start.png"
    click(real_start_dir, "real-start")
    

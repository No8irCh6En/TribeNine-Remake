from start_menu import is_start_menu, click_start_setup, click_delete_accout, click_start_game

from in_game import is_in_game, get_mail_reward, get_fes_reard, satis_or_not, to_gacha, gacha, back_to_start


def main():
    ## Assume from the start menu, already logged
    satisfy_need = False
    while not satisfy_need:
        is_start_menu()
        click_start_setup()
        click_delete_accout()
        click_start_game()
        is_in_game()
        get_mail_reward()
        ## You may add get_fes_reward() here if needed
        to_gacha()
        gacha()
        back_to_start()
        satisfy_need = satis_or_not()

if __name__ == "__main__":
    main()
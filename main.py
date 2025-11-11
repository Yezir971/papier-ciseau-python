from app.utils import *
# from data.text_data import speed_textfrom data.text_data import speed_text
from app.cheat_code import checked_password
from app.interface import interface_menu_game
def main():
    is_run = True
    while is_run:
        is_play_game = False
        difficult_menu = False
        menu_cheat_code = False
        interface_menu_game()
        first_choice = choice_player("Pret à relever le défi ?", "Jouer", "Jouer", "Code de triche", "quitter")
        if first_choice == "Jouer":
            difficult_menu = True
        elif first_choice == "Code de triche":
            menu_cheat_code = True
            while menu_cheat_code: 
                code = str(input(machine('Entre le code de triche (quitter pour revenir au menu principal) : ',speed_text["medium"], False)))
                if(code == "quitter"):
                    menu_cheat_code = False
                    break
                checked_password(code)
        elif first_choice == "quitter":
            is_run = False
            difficult_menu = False
        while difficult_menu:
            try: 
                choix = choice_player("Choisis une dificulté.", "easy", "easy", "medium", "hard", "verry hard", "Retour au menu pricipal")
                if(choix == "Retour au menu pricipal"):
                    difficult_menu = False
                is_play_game = True
                while is_play_game:
                    print(f"Difficulté -> {choix}")
                    play_game(choix)
                    break
            except ValueError:
                print('Vous avez entrer un mauvais choix')
                choix = choice_player("choisis une dificulté.", "easy", "easy", "medium", "hard", "verry hard")
            
    
    
    
if __name__ == "__main__":
    main()
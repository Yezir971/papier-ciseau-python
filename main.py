from app.utils import *
from data.const import speed_text, difficulty
def main():
    
 
    is_true = True
    is_play_game = False
    interface_menu_game()
    while is_true:
        try: 
            choix = choice_player_dificulty()
            if(choix == "quitter"):
                break
            choix = int(choix)
            if choix in range(1,len(difficulty)+1):
                is_play_game = True
            else:
                print(f"Choix invalide, veuillez entrer 1, 2, 3, 4 ou 'quitter' pour arreter de jouer.")
                choix = choice_player_dificulty()
            while is_play_game:
                print(f"Difficulté -> {choix}")
                play_game(choix)
                break
        except ValueError:
            print('Vous avez entrer un mauvais choix')
            choix = choice_player_dificulty()
            
    
    
    
if __name__ == "__main__":
    main()
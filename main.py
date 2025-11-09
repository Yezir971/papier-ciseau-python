from app.utils import *
from data.const import difficulty
def main():
    is_true = True
    is_play_game = False
    interface_menu_game()
    while is_true:
        try: 
            choix = choice_player("Choisis une dificulté.", "easy", "easy", "medium", "hard", "verry hard")
            if(choix == "quitter"):
                break
            type(choix)
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
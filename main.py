from app.utils import *
def main():
 
    is_true = True
    while is_true == True:
        try: 
            machine(interface_menu_game(), 0.002)
            
            choix = choice_player_dificulty()
            if(choix == "quitter"):
                print('quitter')
                return
            if(int(choix) == 1):
                print(f'difficulté -> {choix}')
                
            elif (int(choix) == 2):
                print(f'cdifficulté -> {choix}')
        except:
            print('Vous avez entrer un mauvais choix')
            exit()
        # else:
        #     is_true = False
        #     print('mauvais choix')
    # print(choix)
    
    
    
if __name__ == "__main__":
    main()
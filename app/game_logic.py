from app.interface import machine, template_ui_after_choice, choice_player
from data.text_data import speed_text
from colorama import Fore, Style

def match_game(answer:str ,answer_ia:str, nb_life_j1: int, nb_life_boot:int, difficulty:str )-> int:
    """Logical for all level, return the number of pv Ducker and player

    Args:
        answer (str): Answer of player
        answer_ia (str): Answer enter by Ducky, Ducky is not a cheater :)
        nb_life_j1 (int): PV of player 1
        nb_life_boot (int): PV of Ducky
        difficulty (str): Name of difficulty 

    Returns:
        nb_life_boot(int): number life of Ducky
        nb_life_j1(int): number life of player 1 
    """
    match answer:
        case 'pierre':
            if answer_ia == 'papier' :
                nb_life_j1 -= 1
                template_ui_after_choice(nb_life_j1, nb_life_boot,'Tu perd' , answer_ia)
            elif answer_ia == 'ciseau' :
                nb_life_boot -= 1
                template_ui_after_choice(nb_life_j1, nb_life_boot,'Tu gagne' , answer_ia)
            else:
                template_ui_after_choice(nb_life_j1, nb_life_boot,'égalité' , answer_ia)
        case 'papier':
            if answer_ia == 'ciseau' :
                nb_life_j1 -= 1
                template_ui_after_choice(nb_life_j1, nb_life_boot,'Tu perd' , answer_ia)
            elif answer_ia == 'pierre' :
                nb_life_boot -= 1
                template_ui_after_choice(nb_life_j1, nb_life_boot,'Tu gagne' , answer_ia)
            else:
                template_ui_after_choice(nb_life_j1, nb_life_boot,'égalité' , answer_ia)
        case 'ciseau':
            if answer_ia == 'pierre' :
                nb_life_j1 -= 1
                template_ui_after_choice(nb_life_j1, nb_life_boot,'Tu perd' , answer_ia)
            elif answer_ia == 'papier' :
                nb_life_boot -= 1
                template_ui_after_choice(nb_life_j1, nb_life_boot,'Tu gagne' , answer_ia)
            else:
                template_ui_after_choice(nb_life_j1, nb_life_boot,'égalité' , answer_ia)                
        case 'C\'est bon, j\'en ai marre je préfère abandonner':
            is_play_game = choice_player('Voulez vous rejouer ou retourner au menu principal.','Rejouer','Rejouer','Retour au menu')
            if( is_play_game =='Rejouer' ):
                # si on rejoue on reset le nombre de pv des joueurs 
                nb_life_boot = life[difficulty]["ia"]
                nb_life_j1 = life[difficulty]["player"]
                machine('Les points de vie des 2 joueurs ont été réinitialisé\n', speed_text['medium'])
                machine(f'Point de vie du joueur : {nb_life_j1}\n', speed_text['medium'])
                machine(f'Point de vie de Ducky : {nb_life_boot}\n', speed_text['medium'])
            elif(is_play_game == 'Retour au menu'):
                nb_life_boot = -1
                nb_life_j1 = -1
        case _:
            machine(Fore.RED+'Veuillez entrer pierre, papier ou ciseau\n', speed_text["medium"])
            print(Style.RESET_ALL)
    return nb_life_j1, nb_life_boot
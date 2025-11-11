import random
from data.trash_talk import *
from data.const import posibility, win_condition
from data.life_data import life
from data.text_data import speed_text
from colorama import Fore
from app.interface import machine, choice_player, erase_terminal
from app.game_logic import match_game
from app.cheat_code import reward_cheat_code, activated_cheat

   
def play_game(level: int):
    """Run game with the good difficulty 

    Args:
        level (int): name of difficulty 
    """
    match level:
        case "easy":
            game_lvl("easy")
        case "medium":
            game_lvl("medium")
        case "hard":
            game_lvl("hard")
        case "verry hard":
            game_lvl("verry_hard")

def game_lvl(difficulty: str)-> bool:
    """Main function for run or leave the game

    Args:
        difficulty (str): name of difficulty 

    Returns:
        bool: bolean for retry game or continue
    """
    erase_terminal()
    extra_life_player1,extra_life_player2, extra_life_player3, malus_life_duck = activated_cheat()

    machine(f'Niveau de difficulté {difficulty} Ducky prépare ses plumes:\n', speed_text["medium"])
    nb_life_boot = life[difficulty]["ia"] - malus_life_duck
    nb_life_j1 = life[difficulty]["player"] + extra_life_player1 + extra_life_player2 + extra_life_player3
    machine(f'Point{"s" if nb_life_j1>1 else ""} de vie du joueur : {nb_life_j1}\n', speed_text['medium'])
    machine(f'Point{"s" if nb_life_boot>1 else ""} de vie de Ducky : {nb_life_boot}\n', speed_text['medium'])
    while nb_life_boot > 0 and nb_life_j1 > 0:
        answer = choice_player('Choix du joueur','pierre\n','pierre', 'papier', 'ciseau', 'C\'est bon, j\'en ai marre je préfère abandonner')
        # si le jouerur est en mode très très difficile on prend exactement le contre de son coup pour le faire perdre :D
        answer_ia = random.choice(posibility) if difficulty != "verry_hard" else win_condition[posibility.index(answer)]
        nb_life_j1, nb_life_boot = match_game(answer,answer_ia,nb_life_j1, nb_life_boot, difficulty)
    if nb_life_boot == 0 :
        print('Le joueur à gagné\n')
        machine(reward_cheat_code(difficulty), speed_text['medium'])
    if nb_life_j1 == 0 :
        print("L\'IA à gagné\n")
        machine(random.choice(trash_talk[difficulty]), speed_text["medium"])
    if nb_life_j1 == -1 and nb_life_boot == -1: # Cas qui permet au joueur d'arreter le jeux et de retourner au menu principal
        erase_terminal()
        return False
    is_play_game = choice_player('Voulez vous rejouer ou retourner au menu principal.','Rejouer','Rejouer','Retour au choix du niveau')
    if is_play_game == "Rejouer":
        game_lvl(difficulty)
        erase_terminal()
        return True
    elif is_play_game == "Retour au choix du niveau":
        erase_terminal()
        return False
    else:
        machine(Fore.RED+'Veuillez entrer un choix possible', speed_text["medium"])
        

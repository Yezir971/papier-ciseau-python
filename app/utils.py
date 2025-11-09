import time
import random
from data.trash_talk import *
from data.const import posibility, win_condition
from data.const import speed_text, life
import os
from colorama import Fore, Back, Style
from InquirerPy import inquirer




def interface_menu_game():
    """return the graphical interface game
    """
    machine('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  \033[33m██████╗ ██╗   ██╗ ██████╗██╗  ██╗██╗   ██╗\033[33m    \033[31m██╗   ██╗███████╗\033[39m    ██╗   ██╗ ██████╗ ██╗   ██╗
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⡥⠶⢶⣿⣿⣿⣿⣷⣆⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿  \033[33m██╔══██╗██║   ██║██╔════╝██║ ██╔╝╚██╗ ██╔╝\033[33m    \033[31m██║   ██║██╔════╝\033[39m    ╚██╗ ██╔╝██╔═══██╗██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡿⢡⡞⠁⠀⠀⠤⠈⠿⠿⠿⠿⣿⠀⢻⣦⡈⠻⣿⣿⣿⣿⣿  \033[33m██║  ██║██║   ██║██║     █████╔╝  ╚████╔╝ \033[33m    \033[31m██║   ██║███████╗\033[39m     ╚████╔╝ ██║   ██║██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡇⠘⡁⠀⢀⣀⣀⣀⣈⣁⣐⡒⠢⢤⡈⠛⢿⡄⠻⣿⣿⣿⣿  \033[33m██║  ██║██║   ██║██║     ██╔═██╗   ╚██╔╝  \033[33m    \033[31m╚██╗ ██╔╝╚════██║\033[39m      ╚██╔╝  ██║   ██║██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠉⠐⠄⡈⢀⣿⣿⣿⣿  \033[33m██████╔╝╚██████╔╝╚██████╗██║  ██╗   ██║   \033[33m     \033[31m╚████╔╝ ███████║\033[39m       ██║   ╚██████╔╝╚██████╔╝
⣿⣿⣿⣿⣿⣿⣿⠇⢠⣿⣿⣿⣿⡿⢿⣿⣿⣿⠁⢈⣿⡄⠀⢀⣀⠸⣿⣿⣿⣿  \033[33m╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   \033[33m      \033[31m╚═══╝  ╚══════╝\033[39m       ╚═╝    ╚═════╝  ╚═════╝
⣿⣿⣿⣿⡿⠟⣡⣶⣶⣬⣭⣥⣴⠀⣾⣿⣿⣿⣶⣾⣿⣧⠀⣼⣿⣷⣌⡻⢿⣿
⣿⣿⠟⣋⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣷⠄⢻      <--|Voici Ducky un ass du papier feuille ciseau
⡏⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢂⣭⣿⣿⣿⣿⣿⠇⠘⠛⠛⢉⣉⣠⣴⣾         |Relève le défi en le battant à son propre jeu.
⣿⣷⣦⣬⣍⣉⣉⣛⣛⣉⠉⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣿        
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿\n''', speed_text['fast'])
    
    
def choice_player(message: str, default: str, *choices):
    """Return a graphical design for user choice 

    Args:
        message (str): Message for indicate instruction 
        default (str): Default choice
        *choices: Tuple for different choice

    Returns:
        _type_: Visual effect for make choice
    """
    return inquirer.select(
        message=message,    
        choices=choices,  
        pointer="👉",    
        amark="",   
        qmark="",         
        default=default,
        instruction='(Haut bas pour selectionner)'         
    ).execute()
    
def machine(texte: str, delay: float)-> str:
    """Visual effect for mechine read

    Args:
        texte (str): texte
        delai (float): delay between letter 
    Returns:
        texte(str): texte
    """
    for i in texte: 
        print(i, flush=True, end="")
        time.sleep(delay)
    return texte
    
    
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
    machine(f'Niveau de difficulté {difficulty} Ducky prépare ses plumes:\n', speed_text["medium"])
    nb_life_boot = life[difficulty]["ia"]
    nb_life_j1 = life[difficulty]["player"]
    machine(f'Point{"s" if nb_life_j1>1 else ""} de vie du joueur : {nb_life_j1}\n', speed_text['medium'])
    machine(f'Point{"s" if nb_life_boot>1 else ""} de vie de Ducky : {nb_life_boot}\n', speed_text['medium'])
    while nb_life_boot > 0 and nb_life_j1 > 0:
        answer = choice_player('Choix du joueur','pierre\n','pierre', 'papier', 'ciseau', 'C\'est bon, j\'en ai marre je préfère abandonner')
        # si le jouerur est en mode très très difficile on prend exactement le contre de son coup pour le faire perdre :D
        answer_ia = random.choice(posibility) if difficulty != "verry_hard" else win_condition[posibility.index(answer)]
        nb_life_j1, nb_life_boot = match_game(answer,answer_ia,nb_life_j1, nb_life_boot, difficulty)
    if nb_life_boot == 0 :
        print('Le joueur à gagné\n')
    if nb_life_j1 == 0 :
        print("L\'IA à gagné\n")
        machine(random.choice(trash_talk[difficulty]), speed_text["medium"])
    if nb_life_j1 == -1 and nb_life_boot == -1: # Cas qui permet au joueur d'arreter le jeux et de retourner au menu principal
        erase_terminal()
        interface_menu_game()
        return False
    is_play_game = choice_player('Voulez vous rejouer ou retourner au menu principal.','Rejouer','Rejouer','Retour au menu')
    if is_play_game == "Rejouer":
        game_lvl(difficulty)
        erase_terminal()
        return True
    elif is_play_game == "Retour au menu":
        erase_terminal()
        interface_menu_game()
        return False
    else:
        machine(Fore.RED+'Veuillez entrer un choix possible', speed_text["medium"])
        
def erase_terminal():
    """Efface le contenu du terminal."""
    # 'cls' pour Windows, 'clear' pour Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')    


def match_game(answer:str ,answer_ia:str, nb_life_j1: int, nb_life_boot:int, difficulty:str )-> int:
    """Logical for all level

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

def template_ui_after_choice(nb_life_j1: int, nb_life_boot: int, message: str, answer_ia: str):
    """Visual for result after shifumi move

    Args:
        nb_life_j1 (int): PV of player 1
        nb_life_boot (int): PV of Ducky
        message (str): Message if the player win or not :D
        answer_ia (str): Answer enter by Ducky, Ducky is not a cheater :)
    """
    color_texte_player = Fore.BLUE if nb_life_boot <= nb_life_j1 else Fore.RED
    color_texte_ducky = Fore.RED if nb_life_boot <= nb_life_j1 else Fore.BLUE
    machine(f'Ducky choisi : {answer_ia}\n', speed_text['medium'])
    machine(f'Résultat : {message}\n', speed_text['medium'])
    machine(color_texte_player+f'Il vous reste {nb_life_j1} point{"s" if nb_life_j1>1 else ""} de vie\n', speed_text["medium"])
    machine(color_texte_ducky+f'Il ne reste plus que {nb_life_boot} point{"s" if nb_life_boot>1 else ""} de vie à Ducky\n', speed_text["medium"])
    print(Style.RESET_ALL)
    
    
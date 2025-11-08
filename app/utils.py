import time
import random
from data.trash_talk import *
from data.const import posibility, win_condition
from data.const import speed_text, life
import os
from colorama import Fore, Back, Style



def interface_menu_game():
    """return the graphical interface game
    """
    machine('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    \033[33m██████╗ ██╗   ██╗ ██████╗██╗  ██╗██╗   ██╗\033[33m    \033[31m██╗   ██╗███████╗\033[39m    ██╗   ██╗ ██████╗ ██╗   ██╗     
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⡥⠶⢶⣿⣿⣿⣿⣷⣆⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿    \033[33m██╔══██╗██║   ██║██╔════╝██║ ██╔╝╚██╗ ██╔╝\033[33m    \033[31m██║   ██║██╔════╝\033[39m    ╚██╗ ██╔╝██╔═══██╗██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡿⢡⡞⠁⠀⠀⠤⠈⠿⠿⠿⠿⣿⠀⢻⣦⡈⠻⣿⣿⣿⣿⣿    \033[33m██║  ██║██║   ██║██║     █████╔╝  ╚████╔╝ \033[33m    \033[31m██║   ██║███████╗\033[39m     ╚████╔╝ ██║   ██║██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡇⠘⡁⠀⢀⣀⣀⣀⣈⣁⣐⡒⠢⢤⡈⠛⢿⡄⠻⣿⣿⣿⣿    \033[33m██║  ██║██║   ██║██║     ██╔═██╗   ╚██╔╝  \033[33m    \033[31m╚██╗ ██╔╝╚════██║\033[39m      ╚██╔╝  ██║   ██║██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠉⠐⠄⡈⢀⣿⣿⣿⣿    \033[33m██████╔╝╚██████╔╝╚██████╗██║  ██╗   ██║   \033[33m     \033[31m╚████╔╝ ███████║\033[39m       ██║   ╚██████╔╝╚██████╔╝
⣿⣿⣿⣿⣿⣿⣿⠇⢠⣿⣿⣿⣿⡿⢿⣿⣿⣿⠁⢈⣿⡄⠀⢀⣀⠸⣿⣿⣿⣿    \033[33m╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   \033[33m      \033[31m╚═══╝  ╚══════╝\033[39m       ╚═╝    ╚═════╝  ╚═════╝
⣿⣿⣿⣿⡿⠟⣡⣶⣶⣬⣭⣥⣴⠀⣾⣿⣿⣿⣶⣾⣿⣧⠀⣼⣿⣷⣌⡻⢿⣿
⣿⣿⠟⣋⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣷⠄⢻      <--|voici Ducky un ass du papier feuille ciseau
⡏⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢂⣭⣿⣿⣿⣿⣿⠇⠘⠛⠛⢉⣉⣠⣴⣾         |relève le défi en le battant à son propre jeu
⣿⣷⣦⣬⣍⣉⣉⣛⣛⣉⠉⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣿        
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿''', speed_text['fast'])
    
    
def choice_player_dificulty():
    machine(''' 
Choice your dificulty :
\033[32m1. easy\033[32m
\033[33m2. medium\033[33m
\033[35m3. hard\033[35m
\033[31m4. WTF?! The AI is cheating!\033[31m''', 0.02)
    return input('')
    
def machine(texte: str, delay: float):
    """Visual effect for mechine read

    Args:
        texte (str): texte
        delai (float): delay between letter 
    """
    for i in texte: 
        print(i, flush=True, end="")
        time.sleep(delay)
    print(Style.RESET_ALL)
    
def play_game(level: int):
    match level:
        case 1:
            print("level 1")
            game_lvl_1("easy")
        case 2:
            print("level 2")
            game_lvl_1("medium")
        case 3:
            print("level 3")
            game_lvl_1("hard")
        case 4:
            print("level the player gone lose")
            game_lvl_1("juste_die")

def game_lvl_1(difficulty: str):
    machine('Niveau de difficulté 1 l\'ia ne triche pas:', speed_text["medium"])
    nb_life_boot = life[difficulty]["ia"]
    nb_life_j1 = life[difficulty]["player"]
    while nb_life_boot > 0 and nb_life_j1 > 0:
        machine('pierre, papier, ciseau', speed_text["medium"])
        answer = input('')
        # si le jouerur est en mode très très difficile on prend exactement le contre de son coup pour le faire perdre :D
        answer_ia = random.choice(posibility) if difficulty != "juste_die" else win_condition[posibility.index(answer)]
        nb_life_j1, nb_life_boot = match_game(answer,answer_ia,nb_life_j1, nb_life_boot)
    if nb_life_boot == 0 :
        print('Le joueur à gagné\n')
    if nb_life_j1 == 0 :
        print("L\'IA à gagné\n")
        machine(random.choice(trash_talk[difficulty]), speed_text["medium"])
    machine('Voulez vous rejouer ou retourner au menu principale ?', speed_text["medium"])
    machine('1. Rejouer', speed_text["medium"])
    machine('2. Retour au menu', speed_text["medium"])
    is_play_game = int(input(''))
    if is_play_game == 1:
        game_lvl_1(difficulty)
        return True
    elif is_play_game == 2:
        interface_menu_game()
        return False
    else:
        machine(Fore.RED+'Veuillez entre un chois possible', speed_text["medium"])
        
def erase_terminal():
    """Efface le contenu du terminal."""
    # 'cls' pour Windows, 'clear' pour Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')    


def match_game(answer:str ,answer_ia:str, nb_life_j1: int, nb_life_boot:int ):
    match answer:
        case 'pierre':
            if answer_ia == 'papier' :
                nb_life_j1 -= 1
                machine(Fore.RED+'joueur perd une vie', speed_text["medium"])
            elif answer_ia == 'ciseau' :
                nb_life_boot -= 1
                machine(Fore.BLUE+'IA perd une vie', speed_text["medium"])
            else:
                machine('égalité', speed_text['medium'])
        case 'papier':
            if answer_ia == 'ciseau' :
                nb_life_j1 -= 1
                machine(Fore.RED+'joueur perd une vie', speed_text["medium"])
            elif answer_ia == 'pierre' :
                nb_life_boot -= 1
                machine(Fore.BLUE+'IA perd une vie', speed_text["medium"])
            else:
                machine('égalité', speed_text['medium'])

        case 'ciseau':
            if answer_ia == 'pierre' :
                nb_life_j1 -= 1
                machine(Fore.RED+'joueur perd une vie', speed_text["medium"])
            elif answer_ia == 'papier' :
                nb_life_boot -= 1
                machine(Fore.BLUE+'IA perd une vie', speed_text["medium"])
            else:
                machine('égalité', speed_text['medium'])
        case _:
            machine(Fore.RED+'Veuillez entre pierre, papier, ciseau', speed_text["fast"])
    return nb_life_j1, nb_life_boot
import time
import random
from data.trash_talk import *
from data.const import posibility, win_condition
from data.const import speed_text, life
import os



def interface_menu_game():
    """return the graphical interface game
    """
    machine('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    ██████╗ ██╗   ██╗ ██████╗██╗  ██╗██╗   ██╗    ██╗   ██╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗     
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⡥⠶⢶⣿⣿⣿⣿⣷⣆⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿    ██╔══██╗██║   ██║██╔════╝██║ ██╔╝╚██╗ ██╔╝    ██║   ██║██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡿⢡⡞⠁⠀⠀⠤⠈⠿⠿⠿⠿⣿⠀⢻⣦⡈⠻⣿⣿⣿⣿⣿    ██║  ██║██║   ██║██║     █████╔╝  ╚████╔╝     ██║   ██║███████╗     ╚████╔╝ ██║   ██║██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡇⠘⡁⠀⢀⣀⣀⣀⣈⣁⣐⡒⠢⢤⡈⠛⢿⡄⠻⣿⣿⣿⣿    ██║  ██║██║   ██║██║     ██╔═██╗   ╚██╔╝      ╚██╗ ██╔╝╚════██║      ╚██╔╝  ██║   ██║██║   ██║
⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠉⠐⠄⡈⢀⣿⣿⣿⣿    ██████╔╝╚██████╔╝╚██████╗██║  ██╗   ██║        ╚████╔╝ ███████║       ██║   ╚██████╔╝╚██████╔╝
⣿⣿⣿⣿⣿⣿⣿⠇⢠⣿⣿⣿⣿⡿⢿⣿⣿⣿⠁⢈⣿⡄⠀⢀⣀⠸⣿⣿⣿⣿    ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝         ╚═══╝  ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝
⣿⣿⣿⣿⡿⠟⣡⣶⣶⣬⣭⣥⣴⠀⣾⣿⣿⣿⣶⣾⣿⣧⠀⣼⣿⣷⣌⡻⢿⣿
⣿⣿⠟⣋⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣷⠄⢻      <--|voici SexyDuck un ass du papier feuille ciseau
⡏⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢂⣭⣿⣿⣿⣿⣿⠇⠘⠛⠛⢉⣉⣠⣴⣾         |relève le défi en le battant à son propre jeu
⣿⣷⣦⣬⣍⣉⣉⣛⣛⣉⠉⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣿        
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿''', speed_text['fast'])
    
    
def choice_player_dificulty():
    machine('''
Choice your dificulty :
1. Easy
2. Medium
3. hard
4. WTF?! The AI is cheating!\n''', 0.02)
    
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
    machine('Niveau de difficulté 1 l\'ia ne triche pas: \n', speed_text["medium"])
    nb_life_boot = life[difficulty]["ia"]
    nb_life_j1 = life[difficulty]["player"]
    while nb_life_boot > 0 and nb_life_j1 > 0:
        machine('pierre, papier, ciseau\n', speed_text["medium"])
        answer = input('')
        # si le jouerur est en mode très très difficile on prend exactement le contre de son coup pour le faire perdre :D
        answer_ia = random.choice(posibility) if difficulty != "juste_die" else win_condition[posibility.index(answer)]
        nb_life_j1, nb_life_boot = match_game(answer,answer_ia,nb_life_j1, nb_life_boot)
    if nb_life_boot == 0 :
        print('Le joueur à gagné\n')
    if nb_life_j1 == 0 :
        print("L\'IA à gagné\n")
        machine(random.choice(trash_talk[difficulty]), speed_text["medium"])
    machine('Voulez vous rejouer ou retourner au menu principale ?\n', speed_text["medium"])
    machine('1. Rejouer\n', speed_text["medium"])
    machine('2. Retour au menu\n', speed_text["medium"])
    is_play_game = int(input(''))
    if is_play_game == 1:
        game_lvl_1(difficulty)
        return True
    elif is_play_game == 2:
        interface_menu_game()
        return False
    else:
        machine('Veuillez entre un chois possible', speed_text["medium"])
        
def erase_terminal():
    """Efface le contenu du terminal."""
    # 'cls' pour Windows, 'clear' pour Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')    


def match_game(answer:str ,answer_ia:str, nb_life_j1: int, nb_life_boot:int ):
    match answer:
        case 'pierre':
            if answer_ia == 'papier' :
                nb_life_j1 -= 1
                machine('joueur perd une vie\n', speed_text["medium"])
            elif answer_ia == 'ciseau' :
                nb_life_boot -= 1
                machine('IA perd une vie\n', speed_text["medium"])
            else:
                print('égalité')
        case 'papier':
            if answer_ia == 'ciseau' :
                nb_life_j1 -= 1
                machine('joueur perd une vie\n', speed_text["medium"])
            elif answer_ia == 'pierre' :
                nb_life_boot -= 1
                machine('IA perd une vie\n', speed_text["medium"])
            else:
                print('égalité')
        case 'ciseau':
            if answer_ia == 'pierre' :
                nb_life_j1 -= 1
                machine('joueur perd une vie\n', speed_text["medium"])
            elif answer_ia == 'papier' :
                nb_life_boot -= 1
                machine('IA perd une vie\n', speed_text["medium"])
            else:
                print('égalité')
        case _:
            print('Veuillez entre pierre, papier, ciseau')
    return nb_life_j1, nb_life_boot
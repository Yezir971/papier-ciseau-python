import time
from colorama import Fore, Style
from InquirerPy import inquirer
import os
from data.text_data import speed_text

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
⣿⣿⠟⣋⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣷⠄⢻      <--|Voici Ducky un as du papier feuille ciseau
⡏⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢂⣭⣿⣿⣿⣿⣿⠇⠘⠛⠛⢉⣉⣠⣴⣾         |Relève le défi en le battant à son propre jeu.
⣿⣷⣦⣬⣍⣉⣉⣛⣛⣉⠉⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣿        
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿\n''', speed_text['fast'])
    
def machine(texte: str, delay: float, return_text=True)-> str:
    """Visual effect for mechine read

    Args:
        texte (str): texte
        delai (float): delay between letter 
        return_text (bolean): Bolean for return texte or not
    Returns:
        texte(str): texte
    """
    for i in texte: 
        print(i, flush=True, end="")
        time.sleep(delay)
    if return_text:
        return return_text 
    else:
        return ""
    
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
        instruction='(Haut bas puis enter pour sélectionner)'         
    ).execute()
    
def erase_terminal():
    """Efface le contenu du terminal."""
    # 'cls' pour Windows, 'clear' pour Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')    
    
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
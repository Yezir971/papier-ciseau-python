from colorama import Fore, Style

from app.interface import machine
from data.text_data import speed_text
from data.cheat_code_data import cheat_code_data


def checked_password(code: str):
    """Check if the password are valid and show a message

    Args:
        code (str): Password string
    """
    for key, info in cheat_code_data.items():
        if info["code"] == code:
            # si le cheat est déjà activer on retourne un message d'erreur 
            if info["is_activate"]:
                machine(Fore.RED+'Le cheat est déjà activé\n', speed_text['medium'])
            else :
                info["is_activate"] = True
                # on affiche la description du cheat que l'on a activé
                machine(Fore.CYAN+info["description"], speed_text['medium'])
                machine(Fore.GREEN+'Le cheat est bien activé\n',speed_text["medium"] )
            print(Style.RESET_ALL)
            return
    machine(Fore.RED+'Mot de passe incorect\n',speed_text["medium"] )
    print(Style.RESET_ALL)
    return
    

def reward_cheat_code(difficulty: str):
    """Displays the success message with the cheat code for the level based on the difficulty.

    Args:
        difficulty (str): Difficulty game

    Returns:
        string: Message with cheat code
    """
    for key, info in cheat_code_data.items():
        if key == difficulty:
            return f"Félicitations 🥳🥳! tu as gagné un cheat code, il te sera utile dans les niveaux suivants. code : \x1b[34m{cheat_code_data[difficulty]['code']}\n"
        
def activated_cheat()-> tuple:
    """Function Checked if password are activated and return all stat linked by cheat code

    Returns:
        tuple: Stat cheat code
    """
    extra_life_player1 = 0
    extra_life_player2 = 0
    extra_life_player3 = 0
    malus_life_duck = 0

    for key, info in cheat_code_data.items():
        if info["is_activate"]:
            match key:
                case "easy":
                    extra_life_player1 =1
                case "medium":
                    extra_life_player2 =2
                case "hard":
                    malus_life_duck = 1
                case "verry_hard":
                    extra_life_player3 = 999

    return extra_life_player1, extra_life_player2 , extra_life_player3, malus_life_duck
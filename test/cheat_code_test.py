import pytest
from app.cheat_code import checked_password, activated_cheat, reward_cheat_code


def test_checked_password(capsys):
    # Cas où l'utilisateur entre un mauvais mot de passe 
    checked_password("james")
    captured = capsys.readouterr()
    assert "Mot de passe incorect" in captured.out
    # Cas où l'utilisateur entre un bon mot de passe
    checked_password("MaitreYoda")
    captured = capsys.readouterr()
    assert "\033[36mTu gagne une vie en plus\n\033[32mLe cheat est bien activé\n" in captured.out
    # Cas où l'utilisateur entre encore une fois le meme mot de passe 
    checked_password("MaitreYoda")
    captured = capsys.readouterr()
    assert "\033[31mLe cheat est déjà activé\n" in captured.out

def test_activated_cheat():
    checked_password("MaitreYoda")
    assert activated_cheat() == (1,0,0,0) 
    checked_password("MaitreYoda")
    assert activated_cheat() == (1,0,0,0) 
    checked_password("GuessWho'sBack")
    assert activated_cheat() == (1,2,0,0) 
    checked_password("CandyShop")
    assert activated_cheat() == (1,2, 0,1) 
    checked_password("CaliforniaLove")
    assert activated_cheat() == (1,2,999, 1) 

def test_reward_cheat_code():
    assert reward_cheat_code("easy") == f"Félicitations 🥳🥳! tu as gagné un cheat code, il te sera utile dans les niveaux suivants. code : \x1b[34mMaitreYoda\n"
    assert reward_cheat_code("medium") == f"Félicitations 🥳🥳! tu as gagné un cheat code, il te sera utile dans les niveaux suivants. code : \x1b[34mGuessWho'sBack\n"
    assert reward_cheat_code("hard") == f"Félicitations 🥳🥳! tu as gagné un cheat code, il te sera utile dans les niveaux suivants. code : \x1b[34mCandyShop\n"
    assert reward_cheat_code("verry_hard") == f"Félicitations 🥳🥳! tu as gagné un cheat code, il te sera utile dans les niveaux suivants. code : \x1b[34mCaliforniaLove\n"
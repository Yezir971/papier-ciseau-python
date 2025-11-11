import pytest
from app.utils import match_game, template_ui_after_choice

def test_match_game():
    assert match_game("pierre", "papier", 5, 3, 'easy') == (4, 3)  
    assert match_game("pierre", "ciseau", 5, 3, 'easy') == (5, 2)  
    assert match_game("pierre", "pierre", 5, 3, 'easy') == (5, 3)  

    assert match_game("papier", "pierre", 5, 3, 'easy') == (5, 2)
    assert match_game("papier", "ciseau", 5, 3, 'easy') == (4, 3)
    assert match_game("papier", "papier", 5, 3, 'easy') == (5, 3)

    assert match_game("ciseau", "papier", 5, 3, 'easy') == (5, 2)
    assert match_game("ciseau", "pierre", 5, 3, 'easy') == (4, 3)
    assert match_game("ciseau", "ciseau", 5, 3, 'easy') == (5, 3)
    
       

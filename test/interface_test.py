import pytest
from app.interface import template_ui_after_choice

@pytest.mark.parametrize("nb_life_j1,nb_life_boot,message,answer_ia" , [(5, 1, 'You die', "Pierre"),(3, 2, 'You win', "Papier"),(2, 5, 'Draw', "Ciseau"),(1, 0, 'You survive', "Pierre")])
def test_template_ui_after_choice(capsys, nb_life_j1,nb_life_boot,message,answer_ia ):
    template_ui_after_choice(nb_life_j1,nb_life_boot,message,answer_ia) 
    captured = capsys.readouterr()
    assert captured.out == (f"""Ducky choisi : {answer_ia}\nRésultat : {message}\n{"\x1b[34m" if nb_life_boot <= nb_life_j1 else "\x1b[31m" }Il vous reste {nb_life_j1} point{"s" if nb_life_j1 > 1 else ""} de vie\n{"\x1b[31m" if nb_life_boot <= nb_life_j1 else "\x1b[34m" }Il ne reste plus que {nb_life_boot} point{"s" if nb_life_boot>1 else "" } de vie à Ducky\n\x1b[0m\n""")

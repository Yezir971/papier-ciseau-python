speed_text = {
    "slow":0.2,
    "medium":0.02,
    "fast":0.002
}
life = {
    "verry_hard":{"player":10, "ia":1 },
    "easy":{"player": 6, "ia":5 },
    "medium":{"player":5, "ia":5},
    "hard":{"player": 3, "ia":6 },
}
difficulty = ("easy", "medium", "hard", "verry_hard")

posibility = ('pierre', 'papier', 'ciseau')
win_condition = ('papier', 'ciseau', 'pierre')


cheat_code_data= {
    "easy": {"code":"MaitreYoda", "is_activate" :False, "description":"Tu gagne une vie en plus\n"}, 
    "medium": {"code":"GuessWho'sBack", "is_activate" :False, "description":"Tu gagne deux vie en plus\n"}, 
    "hard": {"code":"CandyShop", "is_activate" :False, "description":"Fait perdre une vie à ducky\n"}, 
    "verry_hard": {"code":"CaliforniaLove", "is_activate" :False, "description":"Donne 999 vies au joueurs\n"}
}

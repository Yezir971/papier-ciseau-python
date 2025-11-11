# Ducky vs You

**Ducky vs You** est un petit jeu en Python.

---

## Mise en contexte

Voici **Ducky**, un canard taquin qui n’a pas sa langue dans son bec !  
Ducky est un as du pierre-feuille-ciseaux et te défie de le battre.  
Si tu parviens à vaincre Ducky dans l’un de ses niveaux, tu débloqueras un **mot de passe secret** qui t’accordera des **avantages non négligeables** dans tes prochains duels 💪  

Et si tu réussis à le battre dans **tous les niveaux de difficulté**… à toi la gloire et la fierté d’avoir vaincu un canard au shifumi ! 😂🦆🤨

---

## Architecture du projet

```
├── README.md
├── app/                        # Dossier principal contenant la logique métier et les modules du jeu
│   ├── __init__.py
│   ├── cheat_code.py           # Gestion et activation des codes de triche
│   ├── game_logic.py           # Logique principale du jeu
│   ├── interface.py            # Affichage et interactions avec le joueur
│   └── utils.py                # Manager : appelle les fonctions au bon moment
├── data/                       # Dossier contenant les constantes et variables du projet
│   ├── __init__.py
│   ├── cheat_code_data.py
│   ├── const.py
│   ├── life_data.py
│   ├── text_data.py
│   └── trash_talk.py
├── main.py                     # Point d’entrée : appelle principalement utils
├── requirements.txt            # Dépendances nécessaires au projet
└── test/                       # Dossier des tests
    ├── __init__.py
    ├── cheat_code_test.py      # Tests des fonctions de cheat code
    ├── game_logic_test.py      # Tests de la logique du jeu
    └── interface_test.py       # Tests des fonctions d’affichage
```

---

## Installation

### Cloner le projet
```bash
git clone https://github.com/Yezir971/papier-ciseau-python
cd papier-ciseau-python
```

### Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## Lancer le projet

> ⚠️ L’utilisation de **nodemon** n’est pas possible, car le projet utilise des bibliothèques nécessitant un véritable environnement de développement Python ⚠️.

### Lancer le jeu
```bash
python3 main.py
```
ou
```bash
python main.py
```

---

## 🧪 Lancer les tests

```bash
pytest -vv
```

> Les tests peuvent mettre un certain temps à s’exécuter :  
> c’est normal, certaines fonctions utilisent la fonction `machine()`  
> qui affiche le texte **caractère par caractère** avec un délai.  

Pour voir l’exécution en temps réel :
```bash
pytest -vv -s
```

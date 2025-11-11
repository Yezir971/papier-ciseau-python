import os

def tree(path=".", prefix=""):
    entries = sorted(os.listdir(path))
    for i, entry in enumerate(entries):
        full = os.path.join(path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(full):
            ext = "    " if i == len(entries) - 1 else "│   "
            tree(full, prefix + ext)

with open("structure.md", "w", encoding="utf-8", newline="\n") as f:
    import sys
    old_stdout = sys.stdout
    sys.stdout = f
    print("# 📁 Structure du projet\n")
    tree(".")
    sys.stdout = old_stdout

print("✅ Fichier structure.md généré en UTF-8")

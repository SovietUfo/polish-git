import sys
import subprocess

translation = {
    "popełnij": "commit",
    "konfiguruj": "config",
    "inicjalizuj": "init",
    "klonuj": "clone",
    "dodaj": "add",
    "wypchnij": "push",
    "pilot": "remote",
    "sprawdź": "checkout",
    "gałąź": "branch",
    "ciągnij": "pull",
    "łącz": "merge",
    "różnica": "diff",
    "etykieta": "tag",
    "kłoda": "log",
    "zrestartuj": "reset",
    "chowaj": "stash",
    "usuń": "rm"
}

args = sys.argv[1:]

first = args[0]


if first in translation.keys():
    command = " ".join(str(x) for x in args).replace(first, translation[first])
    subprocess.run(["git", *command.split()])
    
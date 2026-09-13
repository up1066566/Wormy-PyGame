import json
from pathlib import Path

with open("config_basic.json", 'r') as file:
    data = json.load(file)

settings = data["settings"]
colors = data["colors"]

FPS_EASY = settings["FPS_EASY"]
FPS_MEDIUM = settings["FPS_MEDIUM"]
FPS_HARD = settings["FPS_HARD"]
FPS_EXPERT = settings["FPS_EXPERT"]
FPS = settings["FPS"]

WINDOWWIDTH = settings["WINDOWWIDTH"]
WINDOWHEIGHT = settings["WINDOWHEIGHT"]
CELLSIZE = settings["CELLSIZE"]
EXTRABORDER = settings["EXTRABORDER"]

WHITE = colors["WHITE"]
BLACK = colors["BLACK"]
RED = colors["RED"]
GREEN = colors["GREEN"]
DARKGREEN = colors["DARKGREEN"]
DARKGRAY = colors["DARKGRAY"]
BGCOLOR = colors["BGCOLOR"]

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a mulltiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a mulltiple of cell size."

BOARDWIDTH = WINDOWWIDTH//CELLSIZE
BOARDHEIGHT = WINDOWHEIGHT//CELLSIZE
# print('constants is ok')


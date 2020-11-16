import json
from PySimpleGUIQt import DEFAULT_PROGRESS_BAR_COLOR

file = open("config.json", 'r')
config = json.load(file)
config["tema"] = {'BACKGROUND': '#A8C1B4',
               'TEXT': 'black',
               'INPUT': '#DDE0DE',
               'SCROLL': '#E3E3E3',
               'TEXT_INPUT': 'black',
               'BUTTON': ('white', '#6D9F85'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0}
print(config)
with open("config.json", 'w') as f:
    json.dump(config, f, indent = 4)

HEXCODE_TO_COLOUR = {"AQUA": "#00ffff",
                     "BEIGE": "#f5f5dc",
                     "BLACK": "#000000",
                     "BOLE": "#79443b",
                     "BRASS": "#b5a642",
                     "BROWN": "#a52a2a",
                     "CANARY": "#ffff99",
                     "CELESTE": "#b2ffff",
                     "CHARCOAL": "#36454f",
                     "CHESTNUT": "#954535"}

colour_name = input("Enter colour: ").upper()
while colour_name != "":
    try:
        colour = HEXCODE_TO_COLOUR[colour_name]
        print(colour)
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter colour: ").upper()

name_to_code = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff", "amarantha": "#e52b50",
                "amber": "#ffbf00", "amethyst": "#9966cc", "aqua": "#00ffff", "armygreen": "#4b5320", "aureolin": "#fdee00",
                "brilliantrose": "#ff55a3"}


colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name} is {name_to_code[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()

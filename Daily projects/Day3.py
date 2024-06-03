import sys

print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

direction = input("Welcome to Treasure Island. \nYour mission is to find the treasure. \nYou're at a crossroad. Where do you want to go? Type \"left\" or \"right\": ")

if direction.lower() == "left":
    action = input("Do you want to swim or wait? ")
else:
    sys.exit("You fell into a hole. \nGame Over.")

if action.lower() == "wait":
    door = input("Which door do you want to enter: Red, Blue, or Yellow? ")
else:
    sys.exit("You were attacked by a trout.\nGame Over.")

if door.lower() == "red":
    sys.exit("You were burned by fire.\nGame Over.")
elif door.lower() == "blue":
    sys.exit("You were eaten by beasts.\nGame Over.")
elif door.lower() == "yellow":
    sys.exit("Congratulations! You Win!")
else:
    sys.exit("Game Over")

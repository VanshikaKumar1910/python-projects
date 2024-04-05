import time

def intro():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(2)
    print("You find yourself standing in front of a mysterious cave.")
    time.sleep(2)
    print("Legend has it that a treasure is hidden deep inside the cave.")
    time.sleep(2)
    print("Do you dare to enter the cave and seek the treasure?")
    time.sleep(2)

def choose_cave():
    print("Which cave do you want to enter? (left or right)")
    cave = input()
    if cave.lower() == "left":
        print("You enter the left cave...")
        time.sleep(2)
    elif cave.lower() == "right":
        print("You enter the right cave...")
        time.sleep(2)
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        choose_cave()

def explore_cave():
    print("As you venture deeper into the cave, you see two paths.")
    time.sleep(2)
    print("One path is dark and narrow, while the other is well-lit.")
    time.sleep(2)
    print("Which path do you choose? (dark or lit)")
    path = input()
    if path.lower() == "dark":
        print("You take the dark path...")
        time.sleep(2)
    elif path.lower() == "lit":
        print("You take the well-lit path...")
        time.sleep(2)
    else:
        print("Invalid choice. Please enter 'dark' or 'lit'.")
        explore_cave()

def main():
    intro()
    choose_cave()
    explore_cave()
    print("You continue deeper into the cave...")
    time.sleep(2)
    print("Suddenly, you hear a loud noise...")
    time.sleep(2)
    print("GAME OVER")

if __name__ == "__main__":
    main()

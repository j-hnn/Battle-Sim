from os import system
import battle

print("Welcome to My Text-Based Battle Simulator")

while True: 
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input(">> ")
    if choice == "1":
        battle.start()
    elif choice == "2":
        print("loadgame")
    elif choice == "3":
        print("goodbye")
        exit(0)
    else:
        system("cls")

from random import randint

class Actor:
    def __init__(self):
        self.hp = 10 # health
        self.hpmax = self.hp # max hp 
        self.ap = 2  # action points
        self.atk1 = 2 # first attack
        self.atk2 = 8 # second attack
        self.atk1ap = 1 # ap for attack 1
        self.atk2ap = 3 # ap for attack 2

player = Actor()
enemy = Actor()

def attack():
    is_blocked = False

    print(f"Player: HP - {player.hp}, AP - {player.ap}")
    print(f"Enemy: HP - {enemy.hp}")

    print(f"1. Weak Attack - (AP - {player.atk1ap}, DMG <= {player.atk1})")
    print(f"1. Strong Attack - (AP - {player.atk2ap}, DMG <= {player.atk2})")
    print(f"3. Block - (AP - 0, Sucess Rate - 80%)")
    print(f"4. Wait (AP + 1)")
    action = input(">> ")

    if action == "1":
        print(f"You did {player.atk1} damage.")
        enemy.hp -= player.atk1
        player.ap -= player.atk1ap
    elif action == "2":
        damage = randint(player.atk2/2, player.atk2)
        print(f"You did {damage} damge.")
        enemy.hp -= damage
        player.ap -= player.atk2ap
    elif action == "3":
        chance = randint(1, 100)
        if chance <= 80:
            print("You blocked enemy's attack")
            is_blocked = True
        else:
            print("Attack failed")
            is_blocked = False
    return is_blocked
        
def enemy_attack(is_blocked):
    if not is_blocked and enemy.hp > 0:
        print(f"The enemy did {enemy.atk1} damage")
        player.hp -= enemy.atk1

def start():
    print("This is the battle system")
    
    while enemy.hp > 0 or player.hp > 0:
        blocked = attack()
        enemy_attack(blocked)
    if enemy.hp <= 0:
        print("The enemy has died")
        print(f"Player HP - {player.hp}")
    elif player.hp <= 0:
        print("The player has died")
    input("Press ENTER to exit to main menu")
import random

def fight(player_hp, enemy_hp, run_prob):
    print("A foe approaches!")
    next_turn = ""
    run_number = -1
    while (enemy_hp > 0) and (player_hp > 0):
        next_turn = "void"
        while not((next_turn == "fight") or (next_turn == "heal") or (next_turn == "run")):
            print("Your HP: " + str(player_hp))
            print ("Enemy HP: "  + str(enemy_hp))
            print("Actions: FIGHT  HEAL  RUN")
            next_turn = input("What will you do: ").lower()
        if (next_turn == "fight"):
            enemy_hp -= random.randint(5,10)
        elif (next_turn == "heal"):
            player_hp += random.randint(4,9)
        else:
            run_number = random.randint(1, 100)
            if (run_number < run_prob):
                print("You got away!")
                return None
            print("Couldn't get away!")
        if enemy_hp <= 0:
            print("You won!")
            return None
        input("The enemy attacks!")
        player_hp -= random.randint(3,8)
        next_turn = "void"
    print("You lost.")


name = input("Please enter your name: ")
age = int(input("How old are you: "))
if (age < 50) or (age > 55):
    print("Hello, " + name + "!")
else:
    input("I am going to beat you to death.")
    input("With hammers.")
    fight(25,30, 10)
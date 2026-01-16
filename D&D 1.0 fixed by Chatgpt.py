print("D&D 1.0")
print("Dragon Lord appears!\n")

enemy_health = 10000
player_health = 105
mana = 100

while True:
    print("\nYour Stats:")
    print("HP:", player_health)
    print("Mana:", mana)

    action = input("\nType 'fireball', 'icearrow', or 'quit': ").lower()

    if action == "fireball":
        if mana >= 15:
            mana -= 15
            print("You begin casting Fire Ball...")
            roll = input("Roll 10+ needed. Type 'roll': ").lower()

            if roll == "roll":
                print("Hero: FIRE BALL!")
                enemy_health -= 5
                print("Dragon Lord: You DARE strike me?!")
            else:
                print("You failed the roll.")
                print("Dragon Lord obliterates you.")
                player_health = 0

        else:
            print("Not enough mana!")

    elif action == "icearrow":
        if mana >= 10:
            mana -= 10
            print("You begin casting Ice Arrow...")
            roll = input("Roll 15+ needed. Type 'roll': ").lower()

            if roll == "roll":
                print("Hero: ICE ARROW!")
                enemy_health -= 25
                print("Dragon Lord is weak to Ice!")
            else:
                print("You failed the roll.")
                print("Dragon Lord ends you.")
                player_health = 0

        else:
            print("Not enough mana!")

    elif action == "quit":
        print("You flee from the Dragon Lord.")
        break

    else:
        print("You hesitate...")
        print("Dragon Lord vaporizes you.")
        player_health = 0

    if player_health <= 0:
        print("\nYOU DIED.")
        break

    if enemy_health <= 0:
        print("\nTHE DRAGON LORD IS SLAIN.")
        break
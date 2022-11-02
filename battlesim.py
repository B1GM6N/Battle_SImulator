################################
#     Summative Dictionary     #
#        Peyton Germann        #
################################
#Imports random and time
import random
import time
# list for saying yes
yes = ("yes", "Yes", "Y", "y")
# dictionary for health
health = {"goblin":30,"grimreaper":90,"johncena":70,"pikachu":40,"badger":50,"god":99,"lebron":60,"kanye":10,"peytong":20,"solidsnake":80}
# dictiornary for damage
damage = {"goblin":50,"grimreaper":90,"johncena":50,"pikachu":60,"badger":30,"god":99,"lebron":20,"kanye":10,"peytong":30,"solidsnake":70}
# dictionary for attack name
attacknm = {"goblin":"stabby stabby","grimreaper":"life steal","johncena":"punch","pikachu":"Thunder","badger":"claw","god":"let there be light","lebron":"ballin","kanye":"Can we get much HIGHEEEEEEEEEER","peytong":"low kick","solidsnake":"C4"}
# list for enemy names
monsters = ["goblin", "grimreaper", "johncena", "pikachu", "badger", "god", "lebron", "kanye", "peytong", "solidsnake"]
# dictionary for speed
speed = {"goblin":80,"grimreaper":50,"johncena":30,"pikachu":90,"badger":70,"god":99,"lebron":50,"kanye":20,"peytong":70,"solidsnake":60}
# makes the program wait
def time(n):
    from time import sleep
    sleep(n)
# gets a random number from 0 100
def randomnum():
    r = random.randint(0,100)
    return r
# gets a random enemy
def randomenemy():
    r = random.choice(monsters)
    return r

# gets character stats and moveset
def moveset(m):
    print("It is time to make your moveset.")
    print("What is your main attack?")
    attack = input(">")
    print(f"Lets see how much damage {attack} does.")
    dmg = randomnum()
    # gets your attack name and amount of damage
    time(2)
    print(f"{attack} does {dmg}dmg")
    time(1)
    if int(dmg) > 50:
        print("Thats alot of damage.")
    elif int(dmg) < 50:
        print("Could be better.")
    # Gets health stat
    print("Now that you have your main attack its time to see how much health you have.")
    hth = randomnum()
    time(2)
    print(f"You have {hth}hp.")
    if int(hth) < 30:
        print("Lets hope your a glass cannon and not just glass.")
    time(2)
    print("Lets see how fast you are.")
    # gets speed stat
    spd = randomnum()
    if int(spd) > 50:
        print("You are pretty fast.")
    elif int(spd) < 50:
        print("You are slow. L")
    time(1)
    # adds all information to their lists and dictionaries
    health[m] = hth
    damage[m] = dmg
    attacknm[m] = attack
    monsters.append(m)
    speed[m] = spd
    time(2)
def battle(n):
    # runs moveset function
    moveset(n)
    enemy = randomenemy()
    print("You get one heal per match of 20 health.")
    print("You get one mystery potion")
    time(2)
    print(f"Hey siri play pokemon battle music.")
    time(2)
    print(f"{n} enters the ring with {enemy}!")
    print("Its time to battle!")
    # saves all stats so we can change them and use them
    playerhp = health[n]
    playerat = attacknm[n]
    playerdm = damage[n]
    playersp = speed[n]
    enemyhp = health[enemy]
    enemyat = attacknm[enemy]
    enemydm = damage[enemy]
    enemysp = speed[enemy]
    time(2)
    # makes loop so that while they both are alive the battle continues
    while playerhp > 0 and enemyhp > 0:
        # for if the player is faster than the enemy
        if playersp > enemysp:
            # makes unbreakable
            while True:
                # asks for what you want to do
                print("What would you like to do?")
                print("1 - Attack 2 - Heal 3 - Drink mystery potion")
                option = input(">")
                # player attacks
                if option == "1":
                    print(f"{n} uses {playerat} which does {playerdm}")
                    time(1)
                    # lowers the enemys health using attack damage
                    enemyhp = enemyhp - playerdm
                    # says amount of health left or breaks loop because enemy dead
                    if enemyhp > 0:
                        print(f"{enemy} has {enemyhp} left")
                        time(2)
                    elif enemyhp < 0:
                        break
                    # enemy attacks and changes player health stat
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    # if player is alive says hp if not breaksk loop
                    if playerhp > 0:
                        print(f"{n} has {playerhp} left")
                    elif playerhp < 0:
                        break
                    break
                # heals
                if option == "2":
                    print(f"{n} healed 20hp.")
                    # increases health
                    playerhp = playerhp + 20
                    print(f"{n} has {playerhp}hp.")
                    time(2)
                    # enemy attacks same as before
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    if playerhp > 0:
                        print(f"{n} has {playerhp} left")
                    elif playerhp < 0:
                        break
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    if playerhp > 0:
                        print(f"{n} has {playerhp} left")
                    elif playerhp < 0:
                        break
                # mystery potion???
                elif option == "3":
                    # have a chance to get full health or to lose hp
                    rando = randomnum()
                    print("You take a sip of the mystery potion.")
                    if rando > 90:
                        print("You now have 100hp!")
                        playerhp = 100
                    elif rando < 90:
                        print("You lost 10hp.")
                        playerhp = playerhp - 10
                    time(2)
                    # enemy attacks
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    if playerhp > 0:
                        print(f"{n} has {playerhp}hp left.")
                    elif playerhp < 0:
                        break
                    break
                # for if you type a wrong input
                elif option == "4":
                    print("Not a valid input.")
        # same as everything before this except enemy attacks first because of speed
        elif enemysp > playersp:
            print(f"{enemy} attacks using {enemyat}.")
            playerhp = playerhp - enemydm
            if playerhp > 0:
                print(f"{n} has {playerhp}hp left")
            elif playerhp < 0:
                break
            while True:
                print("What would you like to do?")
                print("1 - Attack 2 - Heal 3 - Drink mystery potion")
                option = input(">")
                if option == "1":
                    print(f"{n} uses {playerat} which does {playerdm}")
                    time(1)
                    enemyhp = enemyhp - playerdm
                    if enemyhp > 0:
                        print(f"{enemy} has {enemyhp} left")
                        time(2)
                    elif enemyhp < 0:
                        break
                    break
                if option == "2":
                    print(f"{n} healed 20hp.")
                    playerhp = playerhp + 20
                    print(f"{n} has {playerhp}hp.")
                    time(2)
                    break
                if option == "3":
                    rando = randomnum()
                    print("You take a sip of the mystery potion.")
                    if rando > 90:
                        print("You now have 100hp!")
                        playerhp = 100
                    elif rando < 90:
                        print("You lost 10hp.")
                        playerhp = playerhp - 10
                    time(2)
                    break
                elif option == "4":
                    print("Not a valid input.")
                
    if playerhp < 0:
        # if the player loses it saves enemys currents stats to dictionaries
        print(f"It looks like {n} is unable to continue.")
        health[enemy] = enemyhp
        damage[enemy] = enemydm
        attacknm[enemy] = enemyat
        speed[enemy] = enemysp
    elif enemyhp < 0:
        # if enemy is dead it saves the players current stats to dictionaries
        print(f"It looks like {enemy} is unable to continue.")
        health[n] = playerhp
        damage[n] = playerdm
        attacknm[n] = playerat
        speed[n] = playersp
    time(2)
    print("Data from this battle is saved")
    print("so if you play again you have a chance to run into the winner.")
    
def intro():
    # asks for name and starts the simulator
    print("This is a python battle simulator! where you can battle it out with famous characters and creatures.")
    name = input("Who is fighting in the arena today?\n")
    cap = randomnum()
    if int(cap) > 50:
        print(f"Interesting, good luck {name}.")
    elif int(cap) < 50:
        print(f"Lets hope you get an easy opponent {name}. :)")
    battle(name)

while True:
    intro()
    # asks if you want to run program again
    yes_no = input("Want to enter the ring again?")
    if yes_no in yes:
        print("Awesome!")
    elif yes_no not in yes:
        print("Bye.")
        break
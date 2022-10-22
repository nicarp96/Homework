import random as rd

max_pers_hp = 100
pers_hp = 100
pers_armor = 200
pers_attack = 20
pers_healing = 15
enemy_hp = 200
enemy_armor = 100
enemy_attack = 0

def enemy_damage_dealt():
    global max_pers_hp, pers_hp, pers_armor, enemy_attack
    enemy_attack = rd.randint(0, 40)
    print("Enemy deals: ",enemy_attack,"\n")
    if pers_armor-enemy_attack>0:
        pers_armor -= enemy_attack

    elif per12s_armor-enemy_attack<0:
        pers_hp = pers_hp-(-1*(pers_armor-enemy_attack))
        pers_armor=0

    else:
        print("You lost")
def attackTheEnemy():
    global enemy_hp, enemy_armor, pers_attack
    if enemy_armor-pers_attack>0:
        enemy_armor -= pers_attack
    elif enemy_armor-pers_attack<0:
        enemy_hp = enemy_hp-(-1*(enemy_armor-pers_attack))
        enemy_armor=0
    else:
        print("You won!")
def playerHeal():
    global max_pers_hp, pers_hp, pers_healing
    if pers_hp+pers_healing<max_pers_hp:
        pers_hp+=pers_healing
    else:
        pers_hp=max_pers_hp
while enemy_hp!=0:
    print("You have ",pers_hp," HP", " and ", pers_armor, " Armor")
    print("Enemy has ",enemy_hp," HP", " and ", enemy_armor, " Armor")
    print("1.Attack\n2.Heal\n")
    choise = input("\nChose ur action [1-2] -> ")
    if choise==1:
        attackTheEnemy()
        enemy_damage_dealt()

    else:
        playerHeal()
        enemy_damage_dealt()

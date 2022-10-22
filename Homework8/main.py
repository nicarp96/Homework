fighters = []
heal_power = 10
class characters():
     def _init__ (self Name, Hp, Armor, Power):
        self.Name = Name
        self.Hp = Hp
        self.Armor= Armor
        self.Power = Power
 class qame (characters):
     def heal(self):
         global heal_power
         self.Hp += heal_power
        print(self.Name+ 'have ', self.Hp, 'Hp left')
     def attack (self, Power):
         if self.Hp - Power > 0:
             self.Hp -= Power
             print(self. Name + ' have ', self.Hp, 'Hp left')
             return True
         else:
            print(self.Name, 'is dead')
             return False
nr =2
for i in range(nr):
    name = input('Name: ')
    Hp = int(input ( 'Hp: ') )
    Armor = int(input('Armor: '))
    Power = int(input('Power: '))
    fighters.append (game (name, Hp, Armor, Power))
alive = True
player1  =  fighters[0]
player2 = fighters[1]
cur_player = player1
next_player = player2
while alive :
print ('Turn to choose for ', cur_player . Name)
print('Enter 1 for attack )
print ('Enter 2 for heal')
try:
move = int (input ()
except:
print ('Wrong data')
continue
move == 1:
alive = next.player. attack(cur_player. Power)
elif move == 2:
cur_player. heal ()
else:
continue
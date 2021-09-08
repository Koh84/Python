"""
class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self):
        print(self.atkl)


enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()
"""

'''
    Program: Magical Calculator
    Author: kelvin K
    Copyright: 2021
'''


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("Hp is", self.hp)


# Create first enemy object
enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

# Create second enemy object
enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()
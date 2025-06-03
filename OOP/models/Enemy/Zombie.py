import random

from .Enemy import Enemy

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage, defense = 0):
        super().__init__('Zombie', health_points, attack_damage,defense)
    def talk(self):
        print('*Complaining...*')
    def  spread_disease(self): #unique zombie only method
        print('The Zombie is try to spread infection')

    def special_attack(self):
        did_special_attack_work = random.random()< 0.5
        if did_special_attack_work:
            curr_hp = self.get_health()
            self.set_health(curr_hp+2);
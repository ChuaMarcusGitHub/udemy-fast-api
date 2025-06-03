import random
from .Enemy import Enemy


class Ogre(Enemy):

    def __init__(self, hp, attack_damage, defense=1):
        super().__init__(name='Ogre', hp=hp, atk=attack_damage, defense=defense)

    def talk(self):
        print('Ogre is throwing hands all around.')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.7
        if (did_special_attack_work):
            curr_att = self.get_attack()
            self.set_attack(curr_att + 2)

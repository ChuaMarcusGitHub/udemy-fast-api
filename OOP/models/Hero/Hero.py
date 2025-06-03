from typing import Optional
from models.Weapons import Weapon

class Hero:
    def __init__(self, health, attack_damage):
        self.__health = health
        self._attack_damage = attack_damage
        self._is_weapon_equipped = False
        self._weapon: Optional[Weapon] = None

    def attack(self):
        print(f"Hero attacks for {self._attack_damage} damage!")

    def equip_weapon(self):
        if self._weapon is not None and not self._is_weapon_equipped:
            self._attack_damage += self._weapon._attack
            self._is_weapon_equipped = True
    def break_weapon(self):
        if self._weapon and self._is_weapon_equipped:
            self._attack_damage -= self._weapon._attack
            self._weapon = None
            self._is_weapon_equipped = False


    def get_health(self):
        return self.__health
    def set_health(self, new_hp):
        self.__health = new_hp
    def get_attack(self):
        return self._attack_damage
    def set_attack(self, new_attack):
        if self._is_weapon_equipped:
            self._attack_damage(new_attack + self._weapon._attack)
        else:
            self._attack_damage(new_attack)
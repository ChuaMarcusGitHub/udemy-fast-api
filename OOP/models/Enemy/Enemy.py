class Enemy:
    __type_of_enemy: str
    __health_points: int
    __attack_damage: int
    __defense: int

    # Constructor
    def __init__(self, name: str, hp: int, atk=10, defense = 0):
        self.__type_of_enemy = name
        self.__health_points = hp
        self.__attack_damage = atk
        self.__defense = defense

    def scanned(self):
        print(f"Scanned Enemy....\nName:{self.__type_of_enemy}\nHP:{self.__health_points}\nAttack:{self.__attack_damage}\n")

    # Class Methods
    def talk(self):
        print(f"I am {self.__type_of_enemy}, prepare to die.")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.__attack_damage} damage!")

    ## Get-Setters

    # Type of Enemy
    def get_type_of_enemy(self):
        return self.__type_of_enemy

    # HP
    def get_health(self):
        return self.__health_points
    def set_health(self, new_hp):
        self.__health_points = new_hp

    # Atk
    def get_attack(self):
        return self.__attack_damage
    def set_attack(self, new_attack):
        self.__attack_damage = new_attack

    def special_attack(self):
        print(f"{self.__type_of_enemy} has no special attack")



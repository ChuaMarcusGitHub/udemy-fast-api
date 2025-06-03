from models import Zombie, Ogre, Enemy, Hero

ogre = Ogre(20, 3)
zombie = Zombie(10, 1)
# Hero
hero = Hero(30, 4)


def hero_battle(h1: Hero, e1: Enemy):
    while h1.get_health() > 0 and e1.get_health() > 0:
        e1.special_attack()
        e1.attack()
        hero_hp = h1.get_health() - e1.get_attack()
        h1.set_health(hero_hp)

        h1.attack()
        enemy_hp = e1.get_health() - h1.get_attack()
        e1.set_health(enemy_hp)

    winner = 'Hero' if h1.get_health() > 0 else e1.get_type_of_enemy()
    print(f'Congratulations! {winner} new king of fighters!')

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.get_health() > 0 and e2.get_health() > 0:
        print('-------------')
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()} - HP: {e1.get_health()}")
        print(f"{e2.get_type_of_enemy()} - HP: {e2.get_health()}")
        e1_health = e1.get_health()
        e2_health = e2.get_health()
        e1.attack()
        e2.set_health(e2_health - e1.get_attack())
        e2.attack()
        e1.set_health(e1_health - e2.get_attack())

    winner = e1.get_type_of_enemy if e1.get_health() > 0 else e2.get_type_of_enemy()
    print(f'Congratulations! {winner} new king of fighters!')

# battle(zombie, ogre)
hero_battle(hero, zombie)


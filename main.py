from monster import Monster
from class_to_csv import to_file


def create_custom_monster() -> Monster :
    monster_name    = input("\nWhat name do you want it to have?\n")
    monster_health  = input("\nWhat is the health of the creature?\n")
    monster_ac      = input("\nWhat is the ac of the creature?\n")
    monster_damage  = input("\nWhat is the damage of the creature?\n")
    monster_speed   = input("\nWhat is the speed of the creature?\n")
    
    return Monster(monster_name, monster_health, monster_ac, monster_damage, monster_speed)
    

monster_type = input("""
1 - Random Monster
2 - Custom Monster
                     """)

if(int(monster_type) == 1):
    print("Random Monster")
    m = Monster()
    to_file(object=m)
else:
    print("Custom Monster")
    to_file(object = create_custom_monster())



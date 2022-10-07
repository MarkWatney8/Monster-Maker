from monster import Monster
from class_to_csv import to_file

m = Monster()
def create_custom_monster() -> Monster :
    monster_name    = input("\nWhat name do you want it to have?\n")
    monster_health  = int(input("\nWhat is the health of the creature?\n"))
    monster_ac      = int(input("\nWhat is the ac of the creature?\n"))

    while monster_ac < 10:
        monster_ac  = int(input("\nHas to be 10+ for ac\n"))
    
    monster_damage  = int(input("\nWhat is the damage of the creature?\n"))
    monster_speed   = int(input("\nWhat is the speed of the creature?\n"))
    
    return Monster(monster_name, monster_health, monster_ac, monster_damage, monster_speed)
    

monster_type = input("""
1 - Random Monster
2 - Custom Monster
                     """)

if(int(monster_type) == 1):
    print("Random Monster")
    m = Monster()
    to_file(object=m)
    print(m)
else:
    print("Custom Monster")
    m = create_custom_monster()
    to_file(object = m)
    print(m)



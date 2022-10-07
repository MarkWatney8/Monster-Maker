from monster import Monster
from class_to_csv import to_file


m = Monster()
def create_custom_monster():
    monster_name    = input("\nWhat name do you want it to have?\n")
    if monster_name != "":
        m.name = monster_name

    monster_health  = input("\nWhat is the health of the creature?\n")
    if monster_health != "":
        m.health = monster_health

    monster_ac      = input("\nWhat is the ac of the creature?\n")
    if monster_ac != "":
        
        while int(monster_ac) < 10:
            monster_ac  = input("\nHas to be 10+ for ac\n")
        m.ac = monster_ac
    
    monster_damage  = input("\nWhat is the damage of the creature?\n")
    if monster_damage != "":
        m.damage = monster_damage

    monster_speed   = input("\nWhat is the speed of the creature?\n")
    if monster_speed != "":
        m.speed = monster_speed
    

monster_type = input("""
1 - Random Monster
2 - Custom Monster
\n""")

if(int(monster_type) == 1):
    print("Random Monster")
    to_file(object=m)
    print(m)
else:
    print("Custom Monster")
    create_custom_monster()
    to_file(object = m)
    print(m)

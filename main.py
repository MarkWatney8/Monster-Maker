import monster
import class_to_csv


test = input("This is a test input. ")

print(test)


monster_type = input("""
1 - Random Monster
2 - Custom Monster""")

if(int(monster_type) == 1):
    print("Random Monster")
else:
    print("Custom Monster")

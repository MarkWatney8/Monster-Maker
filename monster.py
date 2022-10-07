import random


class Monster:


    def __init__(self, name="Gourge", health=random.randrange(1, 81), ac=random.randrange(10, 25), damage=random.randrange(2, 20, 2), speed=random.randrange(10, 50, 10)):
        self.name = name
        self.health = health
        self.ac = ac
        self.damage = damage
        self.speed = speed

    
    def generate_random_health(self):
        health = random.randrange(1, 81)
        self.health = health


    def generate_random_ac(self):
        ac = random.randrange(10, 25)
        self.ac = ac


    def generate_random_damage(self):
        damage = random.randrange(2, 20, 2)
        self.damage = damage


    def generate_random_speed(self):
        speed = random.randrange(10, 50, 10)
        self.speed = speed





from random import randrange


class Monster:

    def __init__(   
                    self,
                    name   = "Gourge", 
                    health = randrange(1, 81),
                    ac     = randrange(10, 25),
                    damage = randrange(2, 20, 2),
                    speed  = randrange(10, 50, 10)
                ):
        
        self.name   = name
        self.health = health
        self.ac     = ac
        self.damage = damage
        self.speed  = speed


    def __str__(self):
        return f"""
    Name: {self.name}
    Health: {self.health}
    AC: {self.ac}
    Damage: {self.damage}
    Speed: {self.speed} ft.
        """

    
    def generate_random_health(self):
        self.health = randrange(1, 81)


    def generate_random_ac(self):
        self.ac = randrange(10, 25)


    def generate_random_damage(self):
        self.damage = randrange(2, 20, 2)


    def generate_random_speed(self):
        self.speed = randrange(10, 50, 10)


m = Monster()
print(m)
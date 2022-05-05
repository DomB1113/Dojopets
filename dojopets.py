


class Pet:
    energy = 50
    health = 100
    def __init__(self, name, type, tricks,noises):
        self.name = name 
        self.type = type 
        self.tricks = tricks
        self.noises = noises
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.energy)
        print(self.health)
    def play(self):
        self.health += 5
        print(self.energy)
        print(self.health)
    def noise(self):
        print(self.noises)

class Petfriends(Pet):
    friendshiplvl = 0
    def __init__(self, name, type, tricks, noises,friend, lvl):
        super().__init__(name, type, tricks, noises)
        self.friendshiplvl = lvl
        self.friend = [friend]
    def sleep(self):
        self.friendshiplvl +=5
        self.energy +=35
        return super().sleep()
    def eat(self):
        self.energy += 5
        self.health += 10
        self.friendshiplvl +=5
        return super().eat()
    def play(self):
        self.health += 5
        self.friendshiplvl += 10
        return super().play()
    def noise(self):
        self.health -= 5
        self.energy += 5
        self.friendshiplvl += 2
        return super().noise()
    def fight(self):
        self.energy -= 10
        self.health -=10
        self.friendshiplvl -=5
        return self



zukos_tricks = ['speak','sit', 'stay', 'paw']
scott = Pet("scott","bird","sit","churp")
zuko = Pet("zuko","golden doodle",zukos_tricks,"bark")
moanas_friends = [zuko,scott]
moana = Petfriends("moana","pitbull","stay","bark",moanas_friends,5)

#(self, first_name, last_name, treats, pet_food, pet):

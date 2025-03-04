class Animal:
    def make_sound(self):
        pass  


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo! Moo!"


def play_sound(animal):
    print(animal.make_sound())


dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog) 
play_sound(cat)  
play_sound(cow)
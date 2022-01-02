class Animal:
    def __init__(self, legs, weight, size):
        self.legs = legs
        self.weight = weight
        self.size = size
    
    def make_sound(self):
        print("Make appropriate sound, that animal does")

class Dog(Animal):
    def __init__(self, legs, weight, size):
        super().__init__(legs, weight, size) # inheriting all attributes that are listed

    def make_sound(self):
        super().make_sound() # inheriting functionality from base make sound method
        print("Dog does HUF-HUF")

class Cat(Animal):
    def __init__(self, legs, weight, size):
        super().__init__(legs, weight, size)

    def make_sound(self):
        print("Dog does MEOW-MEOW")




basic_animal = Animal(4,50,"medium")
dog = Dog(4, 15, "big")
cat = Cat(4, 5, "small")

print(f"Size of main animal is {basic_animal.size}, size of dog is {dog.size}, size of cat is {cat.size}")
print(dog.make_sound())
print(cat.make_sound())
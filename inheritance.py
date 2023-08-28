# Day 21 Learning to complete the snake game

#Inheritance

class Animal:

    def __init__(self):
        self.is_alive = True

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):         # required to inherit from Animal

    def __init__(self):
        super().__init__()    # super refers to superclass Animal, gets access to superclass attributes and methods

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()       # does everything Animal breathe does
        print("doing it underwater")  # does this in addition to Animal breathe

# you can change an attribute in the subclass but rewriting the attribute with its value
# Example: self.is_alive = False in the Fish init
class Dog:
    name=None
    legs=None
    isCute=None
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def Hello(self):
        print("Woof……Woof!")
        print("My name is "+self.name+".")
        print("I am a "+self.gender+".")
        print("I want to play with you.")
class SpottedDog(Dog):
    isLarge=NotImplemented
    def Character(self):
        print("I am a spotted dog.")
        if self.isLarge==True:
            print("I am a large dog.")
dog3=SpottedDog("Lucky","Girl")
dog3.isLarge=True
dog3.Hello()
dog3.Character()
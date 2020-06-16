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
    isLarge=None
    def __init__(self,name,gender,spots):
        super().__init__(name,gender)
        self.spots=spots
    def Character(self):
        print("I am a spotted dog.")
        if self.isLarge==True:
            print("I am a large dog.")
        print("I have "+str(self.spots)+" spots in my body.")
dog4=SpottedDog("Kitte","Girl",23)
dog4.isLarge=True
dog4.Character()
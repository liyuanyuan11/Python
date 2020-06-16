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
dog1=Dog("Alice","Girl")
dog2=Dog("Danny","Boy")
dog1.Hello()
dog2.Hello()
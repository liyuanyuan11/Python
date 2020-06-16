class Dog:
    name=None
    legs=None
    age=None
    gender=None
    isCute=None
    def SayHello(self):
        print("Woof……Woof!")
        print("My name is "+self.name+".")
        print("I am a "+self.gender+".")
        print("I want to play with you.")
dog1=Dog()
dog1.name="Wang Wang"
dog1.gender="Boy"
dog1.SayHello()
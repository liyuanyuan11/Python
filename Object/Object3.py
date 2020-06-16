class Dog:
    name=None
    legs=None
    age=None
    gender=None
    isCute=None
dog1=Dog()
dog1.name="Wang Wang"
dog1.legs=4
dog1.age=2
dog1.gender="Boy"
dog1.isCute=True
print("The dog name is "+dog1.name+".")
print("The dog is a "+dog1.gender+".")
print("It is "+str(dog1.age)+" years old.")
if dog1.isCute==True:
    print("It is cute.")
else:
    print("It is not cute.")
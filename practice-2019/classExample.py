class human:
    #properties/attributes method(function)
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender=gender
    
    #method
    def laugh(self):
        print(f"{self.name}",end="")
        for i in range(5):
            print(":-)",end="")
        print()
    
    def cry(self):
        print(":-(")

# build an object
I = human("yilian",33)
Mary = human("Mary",10)
He = human("Mike",20)
I.laugh()
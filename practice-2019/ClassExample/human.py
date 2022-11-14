#define a human class
class human:
    #initializer
    def __init__(self,name,age):
        self.name=name  #property/attribute--name
        self.age = age  #property/attribute -- age
    
    def laugh(self):
        print(f'{self.name}',end="")
        print(":-)")
    
#build a human object 
I = human("yilian",30)
he = human("mike",45)
    
#use a human object 
I.laugh()

class student(human):
    def __init__(self, name, age,school):
        super().__init__(name, age)
        self.school = school 
    
    def study(self):
        print(f'{self.name} study at {self.school}')

#build a student object 
she = student("mary",18,"usca")
she.study()
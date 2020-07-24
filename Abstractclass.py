from  abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,value):
        self.name = value

    @abstractmethod
    def get_gender(self):
        pass

class Male(Person):
    def get_gender(self):
        return "male"
class Female(Person):
    def get_gender(self):
        print("Females..")

#p1=Person("Hello")  #It shows an error related with Abstract Class.
m1=Male("yash")
print(m1.get_gender())
f1=Female("Riya")
f1.get_gender()
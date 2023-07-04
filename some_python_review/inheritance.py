
class Parent:
    def method1(self):
        print('Parent class method called')

class Child(Parent):
    def __init__(self):
        print('Child class object created')
    
    def method2(self):
        print("Child class method called")


obj = Child() #creating object of child class

obj.method1() # from parent class
obj.method2() # from child class

# we dont need a constructor in the parent class because we just need the object of child class

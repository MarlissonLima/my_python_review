#composite class has a(has-a relation) component class

class A: # component
    def __init__(self):
        print('Component class object created')
    
    def method1(self):
        print('Component class method1() method executed')

class B: # composite
    def __init__(self):
        #creating object of component class(A)
        self.obj1 = A()
        print('Composite class object also created')

    def method2(self):
        print('Composite class method2() method executed')
        
        #calling method1() method of component class(A)
        self.obj1.method1()



#creating object of composite class(B)
obj2 = B()

#calling method2() method of composite class
obj2.method2()
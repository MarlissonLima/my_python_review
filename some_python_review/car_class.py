
class Car():
    def __init__(self,make,model,year,gas_tank):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #default value for atribute
        self.gas_tank = gas_tank

    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it")
    
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rool back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        if self.gas_tank==True:
            print("The gas tank is filled")
        else:
            print("The gas tank is not filled")

    

class EletricCar(Car):
    def __init__(self, make, model, year,gas_tank):
        #intialize attributes of the base class(parent)
        #then initialize attributes specific to an eletric car(derivate class (child))
        super().__init__(make, model, year,gas_tank)
        self.battery_size = 70
        


    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)}-kWh battery")

    def fill_gas_tank(self): #overriding methods from parent class
       print("This car doesn't need a gas tank!!!")


if __name__=='__main__':

    #new car
    my_new_car = Car('audi','a4',2016,True)
    print(my_new_car.get_descriptive_name())
    my_new_car.update_odometer(23)
    my_new_car.read_odometer()
    my_new_car.fill_gas_tank()


    print("\n\n")

    #used car
    my_used_car = Car('subaru','outback',2013,False)
    print(my_used_car.get_descriptive_name())
    my_used_car.update_odometer(23500)
    my_used_car.read_odometer()
    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()
    my_used_car.fill_gas_tank()

    print("\n\n")

    #inheritance
    my_tesla = EletricCar('tesla','model s',2016,False)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    my_tesla.fill_gas_tank()


    


    
#defining the base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
#creating the subclasses
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print( "Flying ")  

# creating instances and using polymorphism
vehicles = [Car(), Plane()]
for vehicle in vehicles:
    print(vehicle.move())

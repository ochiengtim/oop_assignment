#Base Class
class Vehicle:
    def move(self):
        print("This vehicle moves in a general way.")

#Car Class
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

#Plane Class
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")

#Boat Class
class Boat(Vehicle):
    def move(self):
        print("Sailing across water")

#Bike Class
class Bike(Vehicle):
    def move(self):
        print("Pedaling on a path")

#Polymorphism Demo
def test_polymorphism():
    garage = [Car(), Plane(), Boat(), Bike()]
    for vehicle in garage:
        vehicle.move()

#Run Test
if __name__ == "__main__":
    test_polymorphism()

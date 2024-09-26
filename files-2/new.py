import math

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

class Car:
    def __init__(self, name, location, cost) -> None:
        self.name = name
        self.location = location
        self.cost = cost
    def __str__(self) -> str:
        return f'[{self.name}, {self.location}, {self.cost}]'
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y

class Passenger:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
    def __str__(self) -> str:
        return f'[{self.name}, {self.location}]'
    def move_to(self, new_x, new_y):
      self.location.x = new_x
      self.location.y = new_y

class RideSharingApp:
  def __init__(self) -> None:
    self.cars = []
    self.passengers = []

  def add_car(self, car):
    self.cars.append(car)
    
  def add_passenger(self, passenger):
    self.passengers.append(passenger)

  def remove_car(self, car):
    self.cars.remove(car)
  def remove_passenger(self, passenger):
    self.passengers.remove(passenger)

  def find_cheapest_car(self):
    car_name = self.cars[0]
    cheapest = car_name.cost
    for car in self.cars:
      if car.cost < cheapest:
        car_name = car
        cheapest = car.cost
    return f'Cheapest car available: {car_name}, Cost per mile: {cheapest}'

  def find_nearest_car(self, passenger):
    best_car = self.cars[0]
    distance = 0
    passenger_x = passenger.location.x
    passenger_y = passenger.location.y

    for car in self.cars:
      car_x = car.location.x
      car_y = car.location.y
      dist = math.sqrt((car_x - passenger_x) ** 2 + (car_y - passenger_y) ** 2)

      if dist < distance:
        best_car = car
        distance = dist

      return f'Nearest Car for {passenger}: {best_car}. Distance: {distance}'


#For the remaining code (after this line), no modification is required
print('---------------------Object creation------------------')
print()
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)
print()

print()
location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)
print()

print()
mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)
print()

print('-----------------------Scenario 1---------------------')
print()
mobileApp.find_cheapest_car()
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)
print()

print('-----------------------Scenario 2---------------------')
print()
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)
print()

print()
mobileApp.find_cheapest_car()
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)
print()

print('-----------------------Scenario 3---------------------')
print()
car3= Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)
mobileApp.find_cheapest_car()
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)
print()


#!/usr/bin/python3

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance
        print(f"The {self.color} car drove {distance} miles. Total mileage: {self.mileage}")


car1 = Car("red", 10000)
car2 = Car("blue", 5000)

car1.drive(100)   # affects only car1
car2.drive(50)    # affects only car2


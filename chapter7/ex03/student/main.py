# Write your Wheel class here

import math

class Wheel:
    def __init__(self, radius):
        self.radius = radius

    def wheel_area(self):
        area = math.pi * self.radius * self.radius
        return area

    def wheel_perimeter(self):
        circumference = 2 * math.pi * self.radius
        return circumference

    def swap_radius(self, new_radius):
        self.radius = new_radius
        return new_radius

# Use this to test your code
if __name__ == "__main__":
    wheel = Wheel(7)
    morewheels = True
    while morewheels:
        radius = float(input("Radius of wheel: "))
        wheel.swap_radius(radius)
        print("Surface area of wheel:", wheel.wheel_area())
        print("Perimeter of wheel:", wheel.wheel_perimeter())
        yn = input('More wheels? Y/N ')
        morewheels = yn == 'y' or yn == 'Y'

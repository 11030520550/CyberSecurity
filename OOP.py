
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity is: {capacity}"

    def far(self, capacity):
        return f"The far capacity is: {capacity * 100}"


class Bus(Vehicle):

   def seating_capacity(self, capacity = 50):
       return f"T he seating capacity is: {capacity}"

   def far(self, capacity = 50):
       return super().far(capacity + 50)

bus_1 = Bus(100,30000)
print(bus_1.max_speed, bus_1.mileage)

#4. Define a class attribute (for the parent class) ”color” with a default value white. I.e., Every Vehicle should be white.
print(bus_1.color)
print(bus_1.seating_capacity())
print(bus_1.seating_capacity(4))
print(bus_1.far())










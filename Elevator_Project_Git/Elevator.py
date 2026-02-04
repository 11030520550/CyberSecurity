
class User:
    def __init__(self, name, start_floor, destination_floor):
        self.name = name
        self.start_floor = start_floor
        self.destination_floor = destination_floor


class Elevator:
     def __init__(self,num_floors):
         self.num_floors = num_floors
         self.current_floor = 1
         self.direction = 1
         self.destinations = []
         self.waiting_users = []
         self.passengers = []

     def add_user(self,user):
         self.waiting_users.append(user)
         self.destinations.add(user.start_floor)

     def run(self):
         while self.current_floor:
             if not self.waiting_users > :











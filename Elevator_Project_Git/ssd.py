import threading
import time

class User:
    def __init__(self, name, start_floor, destination_floor):
        self.name = name
        self.start_floor = start_floor
        self.destination_floor = destination_floor
        self.in_elevator = False

class Elevator(threading.Thread):
    def __init__(self, num_floors):
        super().__init__()
        self.num_floors = num_floors
        self.current_floor = 0
        self.direction = 1  # 1=up, -1=down
        self.passengers = []
        self.waiting_users = []
        self.destinations = set()
        self.running = True

    def add_user(self, user):
        self.waiting_users.append(user)
        self.destinations.add(user.start_floor)

    def run(self):
        while self.running:
            if not self.destinations:
                time.sleep(2)
                continue

            # קביעת כיוון לפי היעד הקרוב
            if self.direction == 1:
                next_floors = sorted([f for f in self.destinations if f >= self.current_floor])
                if not next_floors:
                    self.direction = -1
                    continue
            else:
                next_floors = sorted([f for f in self.destinations if f <= self.current_floor], reverse=True)
                if not next_floors:
                    self.direction = 1
                    continue

            next_floor = next_floors[0]

            # תנועה קומה-קומה
            while self.current_floor != next_floor:
                self.current_floor += 1 if self.current_floor < next_floor else -1
                print(f"מעלית בתנועה {'↑' if self.direction==1 else '↓'} - קומה: {self.current_floor} [🔴]")
                time.sleep(1)

            # עצירה
            print(f"מעלית עצרה בקומה {self.current_floor} [🟢]")
            self.handle_floor()
            time.sleep(1)

    def handle_floor(self):
        # משתמשים שמחכים כאן נכנסים
        for user in self.waiting_users[:]:
            if user.start_floor == self.current_floor:
                print(f"{user.name} נכנס למעלית, יעדו: {user.destination_floor}")
                self.passengers.append(user)
                self.waiting_users.remove(user)
                self.destinations.add(user.destination_floor)

        # משתמשים שיוצאים מהמעלית
        for passenger in self.passengers[:]:
            if passenger.destination_floor == self.current_floor:
                print(f"{passenger.name} יצא מהמעלית")
                self.passengers.remove(passenger)

        # הסרת הקומה מהרשימה אם אין אף אחד שצריך כאן
        if self.current_floor in self.destinations:
            self.destinations.remove(self.current_floor)

def main():
    elevator = Elevator(num_floors=10)
    elevator.start()

    # דוגמה של כמה משתמשים
    user1 = User("משתמש1", start_floor=0, destination_floor=7)
    user2 = User("משתמש2", start_floor=3, destination_floor=9)
    user3 = User("משתמש3", start_floor=2, destination_floor=1)

    elevator.add_user(user1)
    elevator.add_user(user2)
    elevator.add_user(user3)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("עצירת המעלית...")
        elevator.running = False
        elevator.join()

if __name__ == "__main__":
    main()

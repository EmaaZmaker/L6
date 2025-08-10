class Bus:
    def __init__(self, seat_capacity):
        self.seat_capacity = seat_capacity

class Fare:
    def __init__(self, bus: Bus):
        base_price_per_seat = 1
        base_price = bus.seat_capacity * base_price_per_seat
        self.price = base_price + (0.10 * base_price)  
ob1 = Bus(50)
ob2 = Fare(ob1)
print(f"The seats in the bus are {ob1.seat_capacity} and the price is {ob2.price}")

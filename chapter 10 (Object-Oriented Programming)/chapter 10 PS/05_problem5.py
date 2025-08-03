# from random import randint

# class Train:
#     def __init__(self, train_no):
#         self.train_no = train_no

#         self.book("rampur", "shyampur")

#     def book(self, source, destination):
#         print(f"Ticket booked in train number {self.train_no}, from {source} to {destination}")

#     def get_status(self):
#         print(f"Train no: {self.train_no}, running on time")

#     def get_fare(self, source, destination):
#         fare = randint(200, 1000)
#         print(f"Ticket fare in train number {self.train_no}, form {source} to {destination} is ₹{fare}")
#         return fare

# t = Train(110086)
# t.book("Rampur", "Shyampur")
# t.get_status()
# t.get_fare("Rampur", "Shyampur")





from random import randint

class Train:
    def __init__(self, train_number, source, destination):
        self.train_number = train_number
        self.source = source 
        self.destination = destination

        self.get_info()
            
    def get_info(self):
        seat_available = randint(0, 1)
        if seat_available:
            seat_number = randint(40, 100)
            print(f"Seat is available, the number is {seat_number}")

            self.get_booked(seat_number)

        else:
            print("No seat is available, sorry for your inconveinence.")

    def get_booked(self, seat_number):
        print(f"Ticket is successfully booked in tain number {self.train_number} from {self.source} to {self.destination}, with seat number {seat_number}")

        self.get_fare()

    def get_fare(self):
        print(f"Fare is {randint(200, 1000)}")

ticket_booking_query = Train(110086, "Delhi", "Shilong")
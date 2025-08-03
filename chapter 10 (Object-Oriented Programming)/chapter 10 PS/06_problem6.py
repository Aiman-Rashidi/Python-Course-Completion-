from random import randint

class Train:
    # def __init__(self, train_no):
    #     self.train_no = train_no
    def __init__(aiman, train_no):
        aiman.train_no = train_no

    # def book(self, source, destination):
    #     print(f"Ticket booked in train number {self.train_no}, from {source} to {destination}")
    def book(harry, source, destination):
        print(f"Ticket booked in train number {harry.train_no}, from {source} to {destination}")

    def get_status(self):
        print(f"Train no: {self.train_no}, running on time")

    def get_fare(self, source, destination):
        fare = randint(200, 1000)
        print(f"Ticket fare in train number {self.train_no}, form {source} to {destination} is ₹{fare}")
        return fare

t = Train(110086)
t.book("Rampur", "Shyampur")
t.get_status()
t.get_fare("Rampur", "Shyampur")
class Vehicle:
    def __init__(self, vehicle_id, year, make, list_price):
        self.vehicle_id = vehicle_id
        self.year = year
        self.make = make
        self.list_price = list_price

        #year = input("Enter the Year: ")
        #make = input("Enter the Make: ")



def actual_price(year, list_price):
        if (year >= 2017):
            actual_price = 0.95 * list_price
            return actual_price
        elif (year >= 2013 and year < 2017):
            actual_price = 0.9 * list_price
            return actual_price
        elif (year >= 2010 and year < 2013):
            actual_price = 0.85 * list_price
            return actual_price
        elif (year < 2010):
            actual_price = 0.8 * list_price
            return actual_price






from collections import deque

class DeliveryDrivers(object):
    def __init__(self, carventory=None):
        self.carventory = carventory if carventory is not None else deque(maxlen=10)

    def __str__(self):
        if not self.carventory:
            return "There is no available car registered."
        car_str = "\n".join([
            "Driver: {0:<20} Type: {1:<15} Capacity: {2:<8} Load: {3:<5}".format(
                driver_details[0], driver_details[1], driver_details[2], driver_details[3]
            ) for driver_details in self.carventory
        ])
        return car_str

    def add_driver(self, name, car_type, capacity, load):
        if capacity < 0 or load < 0:
            return "Error: Capacity and load must be non-negative."
        self.carventory.append((name, car_type, capacity, load))
        return f"Driver {name} added with {car_type}, capacity: {capacity}, current load: {load}."

    def find_driver_for_load(self, req_load):
        for i, driver in enumerate(self.carventory):
            name, car_type, capacity, load = driver
            if load + req_load <= capacity:
                return i, driver
        return None, None

    def check_load(self, req_load):
        if req_load < 0:
            return "Error: Requested load must be non-negative."
        if not self.carventory:
            return "No drivers available."
        
        i, driver = self.find_driver_for_load(req_load)
        if driver:
            name, car_type, capacity, load = driver
            return f"Driver {name} can take {req_load} units with {car_type}. Capacity: {capacity}, Current Load: {load}."
        else:
            return f"No driver can take the load of {req_load} units."

    def add_load(self, req_load):
        if req_load < 0:
            return "Error: Requested load must be non-negative."
        if not self.carventory:
            return "No drivers available."

        i, driver = self.find_driver_for_load(req_load)
        if driver:
            name, car_type, capacity, load = driver
            self.carventory[i] = (name, car_type, capacity, load + req_load)
            return f"Driver {name} now has a load of {load + req_load} units."
        else:
            return f"No driver can take the load of {req_load} units."

def main():
    # Initialize DeliveryDrivers instance
    prodcar = DeliveryDrivers()
    print(prodcar.add_driver("Iris", "Toyota Prius", 7, 0))
    print(prodcar.add_driver("James", "Transporter", 100, 0))
    print(prodcar.add_driver("Cameron", "Buick", 12, 0))
    print(prodcar.add_driver("Annie", "Ford", 100, 0))
    print(prodcar)

    # Check if any driver can take a load and add the load if possible
    print(prodcar.check_load(70))
    print(prodcar.add_load(60))
    print(prodcar.add_load(7))
    print(prodcar.add_load(20))
    print(prodcar.add_load(22))
    print(prodcar.add_load(12))
    print(prodcar.add_load(10))
    print(prodcar.add_load(20))
    print(prodcar.add_load(40))
    print(prodcar.add_load(40))
    print(prodcar.add_load(40))

    print(prodcar)
    return

if __name__ == "__main__":
    main()

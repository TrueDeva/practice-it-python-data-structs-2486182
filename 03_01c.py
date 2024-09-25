from collections import deque

class DeliveryDrivers:
    def __init__(self, carventory=None):
        self.carventory = carventory if carventory is not None else deque(maxlen=10)
        self.unassigned_loads = []

    def __str__(self):
        return "\n".join([f"Driver: {name:<20} Type: {car_type:<15} Capacity: {capacity:<8} Load: {load:<5}"
                          for name, car_type, capacity, load in self.carventory]) or "There is no available car registered."

    def _log_message(self, message, color_code):
        return f"{color_code}{message}\033[0m"

    def add_driver(self, name, car_type, capacity, load):
        if capacity < 0 or load < 0:
            return self._log_message("Error: Capacity and load must be non-negative.", "\033[91m")
        self.carventory.append((name, car_type, capacity, load))
        return self._log_message(f"Driver {name} added with {car_type}, capacity: {capacity}, current load: {load}.", "\033[92m")

    def _find_best_driver(self, req_load):
        best_driver = min(
            ((i, driver) for i, driver in enumerate(self.carventory)
             if driver[3] + req_load <= driver[2]),
            default=(None, None),
            key=lambda item: item[1][2] - (item[1][3] + req_load)
        )
        return best_driver

    def add_load(self, req_load):
        if req_load < 0:
            return self._log_message("Error: Requested load must be non-negative.", "\033[91m")
        if not self.carventory:
            return self._log_message("No drivers available.", "\033[91m")

        i, driver = self._find_best_driver(req_load)
        if driver:
            name, car_type, capacity, load = driver
            self.carventory[i] = (name, car_type, capacity, load + req_load)
            selection_type = "\033[96mOptimized" if capacity - (load + req_load) < capacity - load else "\033[93mStandard"
            return self._log_message(f"{selection_type} Selection: Driver {name} now has a load of {load + req_load} units.", selection_type)
        else:
            self.unassigned_loads.append(req_load)
            return self._log_message(f"No driver can take the load of {req_load} units. Added to unassigned loads.", "\033[91m")

    def redistribute_loads(self):
        logs = []
        for i, (name, car_type, capacity, load) in enumerate(self.carventory):
            if load == 0:
                continue
            for j, (other_name, other_car_type, other_capacity, other_load) in enumerate(self.carventory):
                if i != j and other_load + load <= other_capacity:
                    self.carventory[i] = (name, car_type, capacity, 0)
                    self.carventory[j] = (other_name, other_car_type, other_capacity, other_load + load)
                    logs.append(self._log_message(f"Moved {load} units from {name} to {other_name}.", "\033[94m"))
                    break
        return "\n".join(logs) if logs else self._log_message("No redistribution necessary.", "\033[93m")

    def retry_unassigned_loads(self):
        logs = []
        for req_load in list(self.unassigned_loads):
            result = self.add_load(req_load)
            logs.append(result)
            if "now has a load of" in result:
                self.unassigned_loads.remove(req_load)
        return "\n".join(logs) if logs else self._log_message("All unassigned loads have been added successfully.", "\033[92m")

def main():
    prodcar = DeliveryDrivers()
    drivers = [("Iris", "Toyota Prius", 7, 3), ("James", "Transporter", 100, 50), ("Cameron", "Buick", 12, 8),
               ("Annie", "Ford", 100, 20), ("Blake", "Tesla Model X", 5, 1), ("Olivia", "Sprinter Van", 30, 5),
               ("Mason", "Mini Cooper", 4, 2), ("Sophia", "Jeep Wrangler", 15, 10), ("Liam", "Honda CR-V", 25, 18),
               ("Emma", "Chevy Suburban", 20, 0)]
    
    for driver in drivers:
        print(prodcar.add_driver(*driver))
    
    print(prodcar)

    loads = [3, 50, 4, 2, 15, 6, 25, 10, 7, 30, 8, 20, 12, 1, 5]
    for load in loads:
        print(prodcar.add_load(load))

    print(prodcar)
    print("\nRedistributing loads...")
    print(prodcar.redistribute_loads())
    print(prodcar)
    print("\nRetrying unassigned loads...")
    print(prodcar.retry_unassigned_loads())
    print(prodcar)

if __name__ == "__main__":
    main()

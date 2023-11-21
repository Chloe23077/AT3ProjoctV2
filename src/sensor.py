import random
from car_park import CarPark
from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self,
                 id,
                 is_active,
                 carpark):
        self.id = id
        self.is_active = is_active
        self.carpark = carpark

    def __str__(self):
        return f"sensor's {self.id} and status: {self.is_active}"

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 990), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_carpark(plate)

    @abstractmethod
    def update_carpark(self, plate):
        pass


class EntrySensor(Sensor):
    def update_carpark(self, plate):
        self.carpark.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def update_carpark(self, plate):
        self.carpark.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.carpark.plates)

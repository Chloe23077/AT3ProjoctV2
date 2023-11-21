from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 current_vehicle_count=0,
                 sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Carpark at {self.location}, with {self.capacity} bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

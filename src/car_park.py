from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 current_vehicle_count=0,
                 sensors=None,
                 displays=None,
                 plates=None,  # new
                 ):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []  # (not to change the default value)
        # uses the first value if not None, otherwise uses the second value
        self.displays = displays or []
        self.plates = plates or []  # new

    def __str__(self):
        return f"Carpark at {self.location}, with {self.capacity} bays."
        # R return f"Welcome to {self.location} car park"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

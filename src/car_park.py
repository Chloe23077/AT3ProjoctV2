from pathlib import Path
from datetime import datetime
from sensor import Sensor
from display import Display
import json


class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 current_vehicle_count=0,
                 sensors=None,
                 displays=None,
                 plates=None,
                 log_file=Path("log.txt"),
                 config_file="config.json"
                 ):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []  # (not to change the default value)
        # uses the first value if not None, otherwise uses the second value
        self.displays = displays or []
        self.plates = plates or []  # new
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = Path(config_file)

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
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)


    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")


    def write_config(self):
        with open("config.json", "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)


    @staticmethod
    def from_config(config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return CarPark(config["location"], config["capacity"], log_file=config["log_file"])

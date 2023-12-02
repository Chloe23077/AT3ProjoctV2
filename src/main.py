from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():
    car_park = CarPark(location="moondalup", capacity=100, log_file="moondalup.txt")
    entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
    exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)
    display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

    for _ in range(10):
        entry_sensor.detect_vehicle()

    for _ in range(2):
        exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()

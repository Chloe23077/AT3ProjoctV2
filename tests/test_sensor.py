import unittest
from sensor import EntrySensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.sensor = EntrySensor(id=1, car_park=self.car_park, is_active=False)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.car_park, self.car_park)
        self.assertEqual(self.sensor.is_active, False)

    def test_detect_vehicle(self):
        self.sensor.detect_vehicle()
        self.assertEqual(self.car_park.current_vehicle_count, 1)


if __name__ == "__main__":
    unittest.main()

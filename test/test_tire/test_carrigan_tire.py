import unittest

from tire.carrigan_tire import CarriganTire

# Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.
class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        sensors=[0.9,0.1,0.1]
        tire=CarriganTire(sensors)

        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensors = [0.8, 0.1]
        tire = CarriganTire(sensors)

        self.assertFalse(tire.needs_service())

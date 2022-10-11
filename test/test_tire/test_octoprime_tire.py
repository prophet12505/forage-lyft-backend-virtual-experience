import unittest

from tire.octoprime_tire import OctoprimeTire


# Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.
class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.9, 0.1, 0.5,0.5,0.5,0.5]
        tire = OctoprimeTire(sensors)

        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensors = [0.9, 0.1, 0.5, 0.5, 0.4, 0.5]
        tire = OctoprimeTire(sensors)

        self.assertFalse(tire.needs_service())

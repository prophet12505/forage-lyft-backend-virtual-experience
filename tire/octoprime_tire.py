from tire.tire import Tire


# Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.

class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        sum_sensor=0
        for sensor in self.sensors:
            sum_sensor+=sensor
            if(sum_sensor>=3):
                return True

        return False
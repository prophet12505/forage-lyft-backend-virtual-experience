from tire.tire import Tire

# Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.

class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        for sensor in self.sensors:
            if sensor>=0.9:
                return True

        return False
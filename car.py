from serviceable import Serviceable
from abc import ABC, abstractmethod

class Car(Serviceable):
    def __init__(self,engine,battery):
        super().__init__()
        self.engine=engine
        self.battery=battery


    def needs_service(self):
        if(self.engine.needs_service() or self.battery.needs_service()):
            return True
        else:
            return False

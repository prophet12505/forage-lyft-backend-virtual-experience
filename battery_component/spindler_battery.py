
from abc import ABC


from battery import Battery
from datetime import datetime

class Spindler_Battery(Battery, ABC):
    def __init__(self,  last_service_date,current_date,):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(date=self.current_date.date + 2)
        if service_threshold_date < datetime.today().date() :
            return True #need service
        else:
            return False
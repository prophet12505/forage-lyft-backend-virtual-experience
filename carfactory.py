from engine_component.capulet_engine import CapuletEngine
from engine_component.sternman_engine import SternmanEngine
from engine_component.willoughby_engine import WilloughbyEngine

from battery_component.spindler_battery import Spindler_Battery
from battery_component.nubbin_battery import Nubbin_Battery

from car import Car


class CarFactory:
    def __init__(self):
        pass

    def create_calliope(self,current_date, last_service_date,current_mileage, last_service_mileage):
        engine=CapuletEngine(last_service_mileage,current_mileage)
        battery=Spindler_Battery(last_service_date,current_date)
        return Car(engine,battery)

    def create_glissade(self,current_date, last_service_date,current_mileage, last_service_mileage):
        engine=WilloughbyEngine(last_service_mileage,current_mileage)
        battery=Spindler_Battery(last_service_date,current_date)
        return Car(engine,battery)

    def create_palindrome(self,current_date, last_service_date,warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler_Battery(last_service_date,current_date)
        return Car(engine, battery)

    def create_rorschach(self,current_date, last_service_date,current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = Nubbin_Battery(last_service_date,current_date)
        return Car(engine, battery)

    def create_thovex(self,current_date, last_service_date,current_mileage, last_service_mileage):
        engine =CapuletEngine(last_service_mileage,current_mileage)
        battery = Nubbin_Battery(last_service_date,current_date)
        return Car(engine, battery)

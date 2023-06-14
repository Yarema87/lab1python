from lab1python.models.saw import Saw
from lab1python.models.excections import AlreadyIsException


class ElectricSaw(Saw):
    """
    Class which describes a model of electric saw
    """
    instance = None

    def __init__(self, worktime=8, brand="T-800", power=1100, battery_charge=70,
                 types_of_supply=("battery", "electricity"), is_working=False):
        """
        :param worktime: :param worktime: how much time (in hours) can this electric saw work
        :param brand: example electric saw's brand
        :param power: power of this example electric saw in watts
        :param battery_charge: charge of this electric saw in percent
        :param is_working: is this electric saw working now
        default parameters are describing some spherical electric in vacuum
        """
        super().__init__(brand, power, worktime, types_of_supply, is_working)
        self.battery_charge = battery_charge

    def __str__(self):
        return (f"Brand: {self.brand}, power: {self.power}, worktime: {self.worktime}, battery charge: "
                f"{self.battery_charge}, types of supply: {self.types_of_supply},  is working: {self.is_working}")

    def cut_wood(self, length):
        """
        check, if electric saw with some charge of battery can cut wood with some length
        """
        return True if self.battery_charge > length * 2 else False

    @staticmethod
    def get_instance():
        ElectricSaw.instance = ElectricSaw()
        return ElectricSaw.instance

    def get_remaining_working_time(self):
        return self.battery_charge * 1.2

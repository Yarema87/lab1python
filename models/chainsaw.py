from lab1python.models.saw import Saw


class Chainsaw(Saw):
    """
    Class which describes a model of chainsaw
    """
    instance = None

    def __init__(self, worktime=8, brand="T-800", power=1100,  types_of_supply=("fuel", "electricity"),
                 fuel_tank_capacity=3.7, fuel_level=3.3, is_working=False):
        """
        :param worktime: how much time (in hours) can this chainsaw work
        :param brand: brand of chainsaw
        :param power: power of this chainsaw in watts
        :param fuel_tank_capacity: capacity of this chainsaw's fuel tank in liters
        :param fuel_level: amount of fuel in this chainsaw's fuel tank in liters
        :param is_working: is this chainsaw working now
        default parameters are describing some spherical chainsaw in vacuum
        """
        super().__init__(brand, power, worktime, types_of_supply, is_working)
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_level = fuel_level

    def __str__(self):
        return (f"Brand: {self.brand}, power: {self.power}, worktime: {self.worktime},  "
                f"fuel tank capacity: {self.fuel_tank_capacity}"
                f", fuel level: {self.fuel_level}, "
                f"types of supply: {self.types_of_supply}, is working: {self.is_working}")

    def start(self):
        """
        make chainsaw working
        """
        self.is_working = True

    def stop(self):
        """
        make chainsaw not working
        """
        self.is_working = False

    def cut_wood(self, length):
        """
        check, if chainsaw with some amount of fuel in tank can cut wood with some length
        """
        return True if self.fuel_level > length * 0.3 else False

    @staticmethod
    def get_instance():
        Chainsaw.instance = Chainsaw()
        return Chainsaw.instance

    def get_remaining_working_time(self):
        return self.fuel_level * 2.4

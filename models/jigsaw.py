from lab1python.models.saw import Saw
from lab1python.models.excections import AlreadyIsException


class Jigsaw(Saw):
    """
    Class which describes a model of jigsaw
    """
    instance = None

    def __init__(self, worktime=8, brand="T-800", power=1100, length=0.4,
                 width=0.02, types_of_supply=("battery", "electricity"), is_working=False):
        """
        :param worktime: how much time (in hours) can this jigsaw work
        :param brand: brand of jigsaw
        :param power: power of this jigsaw in watts
        :param width: width of jigsaw's canvas
        :param length: length of jigsaw's canvas
        :param is_working: is this jigsaw working now
        default parameters are describing some spherical jigsaw in vacuum
        """
        super().__init__(brand, power, worktime, types_of_supply, is_working)
        self.length = length
        self.width = width

    def __str__(self):
        return (f"Brand: {self.brand}, power: {self.power}, worktime: {self.worktime}, length: "
                f"{self.length}, width: {self.width}, "
                f"types of supply: {self.types_of_supply} is working: {self.is_working}")

    @staticmethod
    def get_instance():
        Jigsaw.instance = Jigsaw()
        return Jigsaw.instance

    def get_remaining_working_time(self):
        return 8

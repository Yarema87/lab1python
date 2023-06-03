from lab1python.models.saw import Saw


class CircularSaw(Saw):
    """
    Class which describes a model of circular saw
    """
    instance = None

    def __init__(self, worktime=8, brand="T-800", power=1100, radius=1.1,
                 width=0.02, types_of_supply=("battery", "electricity"), is_working=False):
        """
        :param worktime: how much time (in hours) can this circular saw work
        :param brand: brand of circular saw
        :param power: power of this circular saw in watts
        :param width: width of saw's disc
        :param radius: radius of saw's disc
        :param is_working: is this circular saw working now
        default parameters are describing some spherical circular saw in vacuum
        """
        super().__init__(brand, power, worktime, types_of_supply, is_working )
        self.radius = radius
        self.width = width

    def __str__(self):
        return (f"Brand: {self.brand}, power: {self.power}, worktime: {self.worktime}, radius: "
                f"{self.radius}, width: {self.width}, "
                f"types of supply: {self.types_of_supply}, is working: {self.is_working}")

    def start(self):
        """
        make circular saw working
        """
        self.is_working = True

    def stop(self):
        """
        make circular saw not working
        """
        self.is_working = False

    @staticmethod
    def get_instance():
        CircularSaw.instance = CircularSaw()
        return CircularSaw.instance

    def get_remaining_working_time(self):
        return 8

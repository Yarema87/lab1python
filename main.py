class Chainsaw:
    """
    Class exact to the one from java first lab
    """
    instance = None

    def __init__(self, brand="T-800", power=1100, fuel_tank_capacity=3.7, fuel_level=3.3, is_working=False):
        self.__brand = brand
        self.__power = power
        self.__fuel_tank_capacity = fuel_tank_capacity
        self.__fuel_level = fuel_level
        self.__is_working = is_working

    def __str__(self):
        return (f"Brand: {self.__brand}, power: {self.__power}, fuel tank capacity: "
                f"{self.__fuel_tank_capacity}, fuel level: {self.__fuel_level}, is working: {self.__is_working}")

    def start(self):
        self.__is_working = True

    def stop(self):
        self.__is_working = False

    def cut_wood(self, length):
        return True if self.__fuel_tank_capacity > length * 0.3 else False

    @staticmethod
    def get_instance():
        Chainsaw.instance = Chainsaw()
        return Chainsaw.instance


chainsaw1 = Chainsaw("T-1000", 900, 3.2, 3.0, True)
chainsaw2 = Chainsaw()
chainsaw_list = [chainsaw1, chainsaw2, Chainsaw.get_instance()]
for i in chainsaw_list:
    print(i)

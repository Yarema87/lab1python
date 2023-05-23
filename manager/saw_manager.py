from lab1python.models.electric_saw import ElectricSaw
from lab1python.models.chainsaw import Chainsaw
from lab1python.models.circular_saw import CircularSaw
from lab1python.models.jigsaw import Jigsaw

chainsaw1 = Chainsaw()
electric_saw1 = ElectricSaw()
circular_saw1 = CircularSaw()
jigsaw1 = Jigsaw()
chainsaw2 = Chainsaw(6.5, "T-1000", 1000, 4.1, 3.2,)
electric_saw2 = ElectricSaw(7.1, "R2-D2", 1700, 80, True)
circular_saw2 = CircularSaw(6.6, "C3-PO", 1500, 1.05, 0.03, True)
jigsaw2 = Jigsaw(8, "HALO-10000", 550, 0.45, 0.03)
list_of_saws = [chainsaw1, electric_saw1, circular_saw1, jigsaw1, chainsaw2, electric_saw2, circular_saw2, jigsaw2]


def print_saws():
    for i in list_of_saws:
        print(i)


def add_saw(saw):
    list_of_saws.append(saw)


def find_all_working():
    list_of_working_saws = []
    for i in list_of_saws:
        if i.is_working is True:
            list_of_working_saws.append(i)
    return list_of_working_saws


def find_saws_more_powerful_than(power):
    list_of_powerful_saws = []
    for i in list_of_saws:
        if i.power > power:
            list_of_powerful_saws.append(i)
    return list_of_powerful_saws


if __name__ == '__main__':
    for j in find_all_working():
        print(j)

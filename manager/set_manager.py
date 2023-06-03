import saw_manager
from lab1python.models.saw import Saw


def iterate_tuple_elements(obj):
    if isinstance(obj, Saw):
        for element in obj.types_of_supply:
            print(element)
    else:
        print("Invalid object. Please provide an instance of Saw.")


def len_tuple_elements():
    for i in saw_manager.create_saws():
        print(i.types_of_supply[0].__len__())
        print(i.types_of_supply[1].__len__())


def getitem_tuple_elements():
    for i in saw_manager.create_saws():
        for j in range(2):
            print(i.__getitem__(i.types_of_supply[j]))

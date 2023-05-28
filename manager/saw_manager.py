from lab1python.models.electric_saw import ElectricSaw
from lab1python.models.chainsaw import Chainsaw
from lab1python.models.circular_saw import CircularSaw
from lab1python.models.jigsaw import Jigsaw
import set_manager


def create_saws():
    chainsaw1 = Chainsaw()
    electric_saw1 = ElectricSaw()
    circular_saw1 = CircularSaw()
    jigsaw1 = Jigsaw()
    chainsaw2 = Chainsaw(6.5, "T-1000", 1100, ("fuel", "electricity"), 4.1, 3.3, True)
    electric_saw2 = ElectricSaw(7.1, "R2-D2", 1700, 80, ("battery", "electricity"), True)
    circular_saw2 = CircularSaw(6.6, "C3-PO", 1500, 1.05, 0.03, ("battery", "electricity"))
    jigsaw2 = Jigsaw(8, "HALO-10000", 550, 0.45, 0.03)
    list_of_saws = [chainsaw1, electric_saw1, circular_saw1, jigsaw1, chainsaw2,
                    electric_saw2, circular_saw2, jigsaw2]
    return list_of_saws


def numb_of_args(func):
    """
    decorator, which prints number of function arguments before it's execution
    """
    def inner(*args):
        number_of_args = len(args)
        print(f"number of args = {number_of_args}")
        return func(*args)
    return inner


def numb_of_calls(func):
    """
    decorator which counts how many times was function called, and throws exception before the third time
    """
    counter = 0

    def inner(*args):
        nonlocal counter
        counter += 1
        if counter >= 3:
            raise Exception("Too many calls")
        return func(*args)
    return inner


@numb_of_calls
def convert_saws_to_str():
    """
    :return: list of saws in string format
    """
    string_saws = []
    for i in create_saws():
        string_saws.append(str(i))
    return string_saws


@numb_of_calls
def print_saws():
    """
    printing all created saws
    """
    for i in create_saws():
        print(i)


@numb_of_args
def add_saw(saw):
    """
    add a saw to list
    """
    create_saws().append(saw)


@numb_of_args
def find_saws_more_powerful_than(power):
    """
    :return: all saws, which power is more than param
    """
    list_of_powerful_saws = []
    for i in create_saws():
        if i.power > power:
            list_of_powerful_saws.append(i)
    return list_of_powerful_saws


@numb_of_calls
def find_all_working():
    """
    :return: all saws, which are working now
    """
    list_of_working_saws = []
    for i in create_saws():
        if i.is_working is True:
            list_of_working_saws.append(i)
    return list_of_working_saws


@numb_of_calls
def print_len():
    """
    :return:
    """
    for i in create_saws():
        print(len(i.brand))


@numb_of_calls
def print_getitem():
    for i in create_saws():
        return i.__getitem__(i)


@numb_of_calls
def print_iter():
    iter_saws = iter(create_saws())
    for _ in create_saws():
        return next(iter_saws)


@numb_of_calls
def comprehension():
    len_list = [i.brand.__len__() for i in create_saws()]
    return len_list


@numb_of_calls
def enumerating():
    for i in enumerate(convert_saws_to_str()):
        return i


@numb_of_calls
def zipping():
    zipped_list = zip(convert_saws_to_str(), comprehension())
    return list(zipped_list)


@numb_of_calls
def dictionary():
    for i in create_saws():
        dict_saw = i.__dict__
        return dict_saw


@numb_of_calls
def all_or_any():
    counter = 0
    for i in create_saws():
        if i.power > 900:
            counter += 1
    if counter == create_saws().__len__():
        k = True
    else:
        k = False
    if counter > 0:
        m = True
    else:
        m = False
    dictionary_checker = {"all": k, "any": m}
    return dictionary_checker


if __name__ == '__main__':
    print(all_or_any())

from lab1python.models.electric_saw import ElectricSaw
from lab1python.models.chainsaw import Chainsaw
from lab1python.models.circular_saw import CircularSaw
from lab1python.models.jigsaw import Jigsaw
from lab1python.models.saw import Saw
from lab1python.models.excections import AlreadyIsException
import set_manager


def number_of_calls(func):
    """
    decorator which counts how many times was function called, and throws exception after the third time
    """
    counter = 0

    def inner(*args):
        nonlocal counter
        counter += 1
        if counter > 3:
            raise Exception("Too many calls")
        return func(*args)

    return inner


def number_of_args(func):
    """
    decorator, which prints number of function arguments before it's execution
    """
    def inner(*args):
        numb_of_args = len(args)
        print(f"numb of args = {numb_of_args}")
        return func(*args)
    return inner


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


class SawManager:

    @number_of_calls
    def convert_saws_to_str(self):
        """
        :return: list of saws in string format
        """
        string_saws = []
        for i in create_saws():
            string_saws.append(str(i))
        return string_saws

    @number_of_calls
    def print_saws(self):
        """
        printing all created saws
        """
        for i in create_saws():
            print(i)

    @number_of_args
    def add_saw(self, saw):
        """
        add a saw to list
        """
        create_saws().append(saw)

    @number_of_args
    def find_saws_more_powerful_than(self, power):
        """
        :return: all saws, which power is more than param
        """
        list_of_powerful_saws = []
        for i in create_saws():
            if i.power > power:
                list_of_powerful_saws.append(i)
        return list_of_powerful_saws

    @number_of_calls
    def find_all_working(self):
        """
        :return: all saws, which are working now
        """
        list_of_working_saws = []
        for i in create_saws():
            if i.is_working is True:
                list_of_working_saws.append(i)
        return list_of_working_saws

    @number_of_calls
    def __len__(self):
        """
        :return: length of saw's brand's name and number of types of supply
        """
        return len(create_saws())

    @number_of_calls
    def __getitem__(self, index):
        """
        :return: types of saw's all fields
        """
        return create_saws()[index]

    @number_of_calls
    def __iter__(self):
        """
        :return: all saw's objects
        """
        return iter(create_saws())

    @number_of_calls
    def comprehension(self):
        """
        :return: list of lengths of all saw's brand's name
        """
        len_list = [len(i.brand) for i in create_saws()]
        return len_list

    @number_of_calls
    def enumerating(self):
        """
        :return: number of each saw in list
        """
        for i in enumerate(self.convert_saws_to_str()):
            print(i)

    @number_of_calls
    def zipping(self):
        """
        :return: list of saws and lengths of name of their brands
        """
        zipped_list = zip(self.convert_saws_to_str(), self.comprehension())
        return list(zipped_list)

    @number_of_calls
    def dictionary(self):
        """
        :return: saws in dictionary form
        """
        return {attr: value for i in create_saws() for attr, value in i.__dict__.items()}

    @number_of_calls
    def all_or_any(self):
        """
        :return: dictionary, in which said if condition is true for all saws in list or if it's true for
         at least one saw in list
        """
        is_all = all(i.power > 1200 for i in create_saws())
        is_any = any(i.power > 1200 for i in create_saws())
        return {"all": is_all, "any": is_any}


if __name__ == '__main__':
    manager = SawManager()
    chainsaw3 = Chainsaw(6.5, "T-1000", 1100, ("fuel", "electricity"), 3.7, 3.5, False)
    chainsaw3.stop()

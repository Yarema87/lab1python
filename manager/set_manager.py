import saw_manager


class SetManager:

    def __init__(self, manager):
        self.manager = manager

    def __iter__(self):
        """
        iterates throw elements of the types of supply
        """
        for i in self.manager.create_saws():
            yield i.types_of_supply

    def __len__(self):
        """
        :return: length of 'types of supply' tuple
        """
        total_len = 0
        for i in self.manager.create_saws():
            total_len += len(i.types_of_supply)
        return total_len

    def __getitem__(self, index):
        """
        :return: types of elements in 'types of supply' tuple
        """
        counter = 0
        for i in self.manager.create_saws():
            if counter <= index < counter + len(i.types_of_supply):
                inner_index = index - counter
                return list(i.types_of_supply)[inner_index]
            counter += len(i.types_of_supply)
        raise IndexError("list is out of range")

    def __next__(self):
        raise StopIteration()




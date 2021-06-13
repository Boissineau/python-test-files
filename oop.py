class Name:
    def __init__(self):
        self.list = []

    def retrieve_list(self):
        return self.list

    def print_list(self):
        print(self.list)

    def add_to_list(self, new_value):
        self.list.append(new_value)


class Name2:
    def __init__(self):
        self.list = []

    def idk(self):
        print('hello')

if __name__ == '__main__':
    x = Name()
    y = (1, 2)
    x.add_to_list(y)
    x.print_list()
    
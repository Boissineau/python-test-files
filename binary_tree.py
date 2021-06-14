import random

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value



class Binary_tree:
    def __init__(self):
        self.root = None
        self.length = 0

    def get_root(self):
        return self.root

    def add_node(self, value):
        self.length += 1
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_node(value, self.root)

    def _add_node(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add_node(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add_node(value, node.right)
            else:
                node.right = Node(value)
    def get_length(self):
        return self.length


def get_randomized_numbers(min, max):
    numbers = list(range(min, max))
    random.shuffle(numbers)
    return numbers


if __name__ == '__main__':
    tree = Binary_tree()
    
    numbers = get_randomized_numbers(0, 1000)
    for num in numbers:
        tree.add_node(num)

    print(tree.get_length())
    

    
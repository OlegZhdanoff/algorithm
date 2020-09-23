# 2) Закодируйте любую строку по алгоритму Хаффмана.

from collections import defaultdict


class Char_Node:
    code = ''

    def __init__(self, value=None, left=None, right=None, weight=None, code=''):
        self.value = value
        self.left = left
        self.right = right
        self.weight = weight
        self.code = code

    def __str__(self):
        return f'{self.value, self.weight, self.left, self.right, self.code}'


class Tree:
    def __init__(self):
        self.root = None

    # функция для добавления узла в дерево
    def new_node(self, value):
        return Char_Node(value)

    # функция для вычисления высоты дерева
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    # функция для распечатки элементов на определенном уровне дерева
    def print_given_level(self, root, level, code):
        if root is None:
            return
        if level == 1:
            root.code = code
            print(root, end='')
        elif level > 1:
            self.print_given_level(root.left, level - 1, root.code + '0')
            self.print_given_level(root.right, level - 1, root.code + '1')

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i, self.root.code)
            print()
            i += 1


def haff(st: str):
    char_freq = defaultdict(int)
    for ch in st:
        char_freq[ch] += 1

    char_freq = dict(sorted(char_freq.items(), key=lambda v: v[1], reverse=True))
    print(char_freq)
    node_dict = []
    while len(char_freq) > 1:
        for _ in range(2):
            if hasattr(list(char_freq.keys())[-1], 'count'):
                node_dict.append(Char_Node())
                node_dict[-1].value, node_dict[-1].weight = char_freq.popitem()
            else:
                char_freq.popitem()
        node_dict.append(Char_Node(None, node_dict[-2], node_dict[-1], node_dict[-2].weight + node_dict[-1].weight))
        char_freq[node_dict[-1]] = node_dict[-2].weight + node_dict[-3].weight
        char_freq = dict(sorted(char_freq.items(), key=lambda v: v[1], reverse=True))

    print('*' * 50)
    char_tree = Tree()
    char_tree.root = node_dict.pop()
    char_tree.print_level_order(char_tree.root)

    print('*' * 50)
    for el in node_dict:
        if hasattr(el.value, 'count'):
            print(el)

    res = ''
    for ch in st:
        for el in node_dict:
            if el.value == ch:
                res += el.code
                break
    return res


string = 'hellooo'
print(f'\n{string} ->>> {haff(string)}')


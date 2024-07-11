class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def __str__(self, shift=0):
        tree_string = ''
        if shift > 1:
            tree_string += '    ' * (shift-1)
        if shift > 0:
            tree_string += '|___'
        tree_string += f'{self.data}\n'
        for child in self.children:
            tree_string += child.__str__(shift+1)
        return tree_string

    def index(self, data, address='/'):
        if self.data == data:
            return address
        elif len(self.children):
            new_address = address + f'{self.data}/'
            for child in self.children:
                addr = child.index(data, new_address)
                if addr:
                    return addr
        return None

    def __getitem__(self, address):
        splitted = address.split('/')
        splitted = [s for s in splitted if s]
        new_addr = '/'.join(splitted[1:]) + '/'
        cur_addr = splitted[0]
        if self.data != cur_addr:
            return None
        if new_addr == '/':
            return self
        else:
            for child in self.children:
                data = child[new_addr]
                if data:
                    return data

    def __setitem__(self, address, new_tree):
        splitted = address.split('/')
        splitted = [s for s in splitted if s]
        new_addr = '/'.join(splitted[1:]) + '/'
        cur_addr = splitted[0]
        if self.data != cur_addr:
            return
        if new_addr == '/':
            # FIXME
            return self
        else:
            for child in self.children:
                data = child[new_addr]
                if data:
                    return data

    def __len__(self):
        depth = 1
        max_child_depth = 0
        for child in self.children:
            max_child_depth = max(max_child_depth, len(child))
        return depth + max_child_depth


root = Tree("root")
left = Tree("left")
left.children = [Tree('left1'), Tree('left2')]
middle = Tree("middle")
middle.children = [Tree('mid1'), Tree('mid2'), Tree('mid3')]
right = Tree("right")
right.children = [Tree('right1'), middle]
root = Tree("root")
root.children = [left, middle, right]
print(root)
# print(f'{root.index("left2") = }')
print(root['/root/right/'])
print(len(root))



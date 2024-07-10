class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data    

    def __str__(self, shift=0):
        tree_string = ''
        if shift > 1:
            tree_string += '|   ' * (shift-1)
        if shift > 0:
            tree_string += '|___'
        tree_string += f'{self.data}\n'
        for child in self.children:
            tree_string += child.__str__(shift+1)
        return tree_string


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

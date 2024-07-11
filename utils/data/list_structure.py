class List:
    def __init__(self, data):
        self.next = None
        self.data = data    

    def __str__(self):
        list_string = f'{self.data}\n'
        if self.next is not None:
            list_string += '|\n' + self.next.__str__()
        return list_string

    def __len__(self):
        length = 1
        if self.next:
            length += len(self.next)
        return length

    def index(self, data, ind=0):
        if self.data == data:
            return ind
        elif self.next:
            return self.next.index(data, ind+1)
        else:
            return None

    def __getitem__(self, ind):
        if ind == 0:
            return self.data
        elif ind > 0 and self.next:
            return self.next[ind-1]
        else:
            return None

    def __setitem__(self, ind, data):
        if ind == 0:
            self.data = data
        elif ind > 0 and self.next:
            self.next[ind-1] = data


e1 = List('first')
e2 = List('second')
e3 = List('third')
e2.next = e3
e1.next = e2
print(e1)
print(len(e1))
print(e1.index('third'))
print(e1[2])
e1[2] = '3rd'
print(e1)

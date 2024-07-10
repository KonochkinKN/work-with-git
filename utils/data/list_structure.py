class List:
    def __init__(self, data):
        self.next = None
        self.data = data    

    def __str__(self):
        list_string = f'{self.data}\n'
        if self.next is not None:
            list_string += '|\n' + self.next.__str__()
        return list_string
    
e1 = List('first')
e2 = List('second')
e3 = List('third')
e2.next = e3
e1.next = e2
print(e1)
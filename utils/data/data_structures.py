"""
- Стэк
- Очередь
- Односвязный список
- Двусвязный список*
"""


def simple_examples():
    # stack
    stack = []
    # appending
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print(f'{stack = }')
    # poping
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(f'{stack = }')
    # queue = [q]
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print(f'{queue = }')
    # poping
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print(f'{queue = }')


def complex_example():
    class Stack4:
        __element1 = None
        __element2 = None
        __element3 = None
        __element4 = None
        __pointer = 0

        def push(self, element):
            if self.__pointer == 0:
                self.__element1 = element
            elif self.__pointer == 1:
                self.__element2 = element
            elif self.__pointer == 2:
                self.__element3 = element
            elif self.__pointer == 3:
                self.__element4 = element
            else:
                raise OverflowError('Stack overflow')
            self.__pointer += 1

        def pop(self):
            if self.__pointer == 1:
                element = self.__element1
                del self.__element1
            elif self.__pointer == 2:
                element = self.__element2
                del self.__element2
            elif self.__pointer == 3:
                element = self.__element3
                del self.__element3
            elif self.__pointer == 4:
                element = self.__element4
                del self.__element4
            else:
                raise MemoryError('Empty stack')
            self.__pointer -= 1
            return element

        def __str__(self):
            string = '{ '
            if self.__pointer in [0, 1]:
                string += '->'
            string += str(self.__element1) + ',\t'
            if self.__pointer == 2:
                string += '->'
            string += str(self.__element2) + ',\t'
            if self.__pointer == 3:
                string += '->'
            string += str(self.__element3) + ',\t'
            if self.__pointer == 4:
                string += '->'
            string += str(self.__element4) + ' }'
            return string

    s = Stack4()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s)
    print(s.pop())
    print(s)


def complex_queue_example():
    class Queue4:
        __element1 = None
        __element2 = None
        __element3 = None
        __element4 = None
        __pointer_i = 0
        __pointer_o = -1

        def push(self, element):
            if self.__pointer_i == 0:
                self.__element1 = element
            elif self.__pointer_i == 1:
                self.__element2 = element
            elif self.__pointer_i == 2:
                self.__element3 = element
            elif self.__pointer_i == 3:
                self.__element4 = element
            else:
                raise OverflowError('Queue overflow')
            self.__pointer_i += 1
            self.__pointer_i %= 4
            # заполненная очередь
            if self.__pointer_o == self.__pointer_i:
                self.__pointer_i = -1
            # в пустую очередь добавили элемент
            if self.__pointer_o == -1:
                self.__pointer_o = 0

        def pop(self):
            if self.__pointer_o == 0:
                element = self.__element1
                del self.__element1
            elif self.__pointer_o == 1:
                element = self.__element2
                del self.__element2
            elif self.__pointer_o == 2:
                element = self.__element3
                del self.__element3
            elif self.__pointer_o == 3:
                element = self.__element4
                del self.__element4
            else:
                raise MemoryError('Empty queue')
            self.__pointer_o += 1
            self.__pointer_o %= 4
            # пустая очередь
            if self.__pointer_o == self.__pointer_i:
                self.__pointer_o = -1
                self.__pointer_i = 0
            # в заполненной освободилось место
            if self.__pointer_i == -1:
                self.__pointer_i = self.__pointer_o
            return element

        def __str__(self):
            return f'[ {self.__element1}, {self.__element2},' \
                   f'{self.__element3}, {self.__element4} ]'

    q = Queue4()
    q.push(1)
    q.push(2)
    q.push(3)
    q.pop()
    q.push(4)
    q.pop()
    q.push(5)
    q.push(1)
    print(q)


if __name__ == '__main__':
    complex_queue_example()

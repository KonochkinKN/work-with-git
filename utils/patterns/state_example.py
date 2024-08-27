from __future__ import annotations
from abc import ABC, abstractmethod


class Computer:
    """ Контекст работы состояний """
    _state = None
    _observers = []

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Компьютер: переход в состояние {type(state).__name__}")
        msg = f'{type(self._state).__name__}->{type(state).__name__}'
        self._state = state
        self._state.context = self
        self.notify(msg)

    def push_reboot(self):
        self._state.reboot()

    def push_power(self):
        self._state.switch_power()

    def do_nothing(self):
        self._state.wait_5_mins()

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, msg):
        for observer in self._observers:
            observer.update(msg)


class State(ABC):
    @property
    def context(self) -> Computer:
        return self._context

    @context.setter
    def context(self, context: Computer) -> None:
        self._context = context

    @abstractmethod
    def reboot(self) -> None:
        pass

    @abstractmethod
    def switch_power(self) -> None:
        pass

    @abstractmethod
    def wait_5_mins(self) -> None:
        pass


class PoweredOn(State):
    def reboot(self) -> None:
        print("Нажата кнопка перезагрузки")
        print("Компьютер перезагружается")
        self.context.transition_to(Reboot())

    def switch_power(self) -> None:
        print("Нажата кнопка питания")
        print("Компьютер выключается")
        self.context.transition_to(PoweredOff())

    def wait_5_mins(self) -> None:
        print("Прошло 5 минут")
        print("Компьютер переходит в режим сна")
        self.context.transition_to(Hibernation())


class PoweredOff(State):
    def reboot(self) -> None:
        print("Нажата кнопка перезагрузки")
        print("Ничего не происходит")

    def switch_power(self) -> None:
        print("Нажата кнопка питания")
        print("Компьютер включается")
        self.context.transition_to(PoweredOn())

    def wait_5_mins(self) -> None:
        print("Прошло 5 минут")
        print("Ничего не происходит")


class Hibernation(State):
    def reboot(self) -> None:
        print("Нажата кнопка перезагрузки")
        print("Компьютер перезагружается")
        self.context.transition_to(Reboot())

    def switch_power(self) -> None:
        print("Нажата кнопка питания")
        print("Компьютер включается")
        self.context.transition_to(PoweredOn())

    def wait_5_mins(self) -> None:
        print("Прошло 5 минут")
        print("Ничего не происходит")


class Reboot(State):
    def reboot(self) -> None:
        print("Нажата кнопка перезагрузки")
        print("Ничего не происходит")

    def switch_power(self) -> None:
        print("Нажата кнопка питания")
        print("Компьютер выключается")
        self.context.transition_to(PoweredOff())

    def wait_5_mins(self) -> None:
        print("Прошло 5 минут")
        print("Компьютер включается")
        self.context.transition_to(PoweredOn())


class PowerPushObserver:
    power_on_counter = 0
    power_off_counter = 0

    def update(self, msg):
        state0, state1 = msg.split('->')
        if state0 != 'PoweredOn' and state1 == 'PoweredOn':
            self.power_on_counter += 1
        elif state0 != 'PoweredOff' and state1 == 'PoweredOff':
            self.power_off_counter += 1
        print(f'UPD: ON: {self.power_on_counter},'
              f' OFF: {self.power_off_counter}')


if __name__ == "__main__":
    # Клиентский код
    computer = Computer(PoweredOff())
    computer.attach(PowerPushObserver())
    computer.push_power()
    computer.do_nothing()
    computer.do_nothing()
    computer.push_reboot()
    computer.do_nothing()
    computer.push_power()

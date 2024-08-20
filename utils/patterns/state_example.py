from __future__ import annotations
from abc import ABC, abstractmethod


class Computer:
    """ Контекст работы состояний """
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Компьютер: переход в состояние {type(state).__name__}")
        self._state = state
        self._state.context = self

    def push_button(self):
        self._state.push_button()

    def do_nothing(self):
        self._state.wait_5_mins()


class State(ABC):
    @property
    def context(self) -> Computer:
        return self._context

    @context.setter
    def context(self, context: Computer) -> None:
        self._context = context

    @abstractmethod
    def push_button(self) -> None:
        pass

    @abstractmethod
    def wait_5_mins(self) -> None:
        pass


class PoweredOn(State):
    def push_button(self) -> None:
        print("Нажата кнопка включения/выключения")
        print("Компьютер выключается")
        self.context.transition_to(PoweredOff())

    def wait_5_mins(self) -> None:
        print("Прошло 5 минут")
        print("Компьютер переходит в режим сна")
        self.context.transition_to(Hibernation())


class PoweredOff(State):
    def push_button(self) -> None:
        print("Нажата кнопка включения/выключения")
        print("Компьютер включается")
        self.context.transition_to(PoweredOn())

    def wait_5_mins(self) -> None:
        print("Прошло 5 минут")
        print("Ничего не меняется")


class Hibernation(State):
    def push_button(self) -> None:
        print("Нажата кнопка включения/выключения")
        print("Компьютер включается")
        self.context.transition_to(PoweredOn())

    def wait_5_mins(self) -> None:
        print("Прошло 5 минут")
        print("Ничего не меняется")


if __name__ == "__main__":
    # Клиентский код.

    computer = Computer(PoweredOff())
    computer.push_button()
    computer.do_nothing()
    computer.do_nothing()
    computer.push_button()
    computer.push_button()
    computer.do_nothing()
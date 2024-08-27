from threading import Thread, Lock, Event
from time import sleep
import os
clear = lambda: os.system('cls')


def simple_threads_example():
    """ простой пример работы с несколькими потоками """
    def delayed_print(string, pause=1):
        sleep(pause)
        print(string)

    # создаем потоки
    t1 = Thread(target=delayed_print, args=["3", 3])
    t2 = Thread(target=delayed_print, args=["2", 2])
    t3 = Thread(target=delayed_print, args=["1", 1])
    # запускаем потоки
    t1.start()
    t2.start()
    t3.start()
    print('all 3 running:')
    # ждем завершения потоков
    t1.join()
    t2.join()
    t3.join()


def counter_example():
    """ пример счетчика в отдельном потоке """
    def timer_3min(event):
        for i in range(180):
            sleep(1)
            clear()
            print('Счетчик:', i)
            print('Чтобы остановить счетчик, введите "s"')
            if event.is_set():
                break

    stop = Event()
    t = Thread(target=timer_3min, args=[stop])
    print(t)
    t.start()
    # ловим нажатие клавиши в основном потоке
    while True:
        sleep(0.1)
        exit = input()
        if exit == 's':
            stop.set()
            break


counter = 0
def locking_example():
    """ пример работы с lock """
    def event(lock):
        global counter
        # блокируем текущий участок кода для других потоков
        lock.acquire()

        local_counter = counter
        local_counter += 1

        sleep(0.1)

        counter = local_counter
        print(f'{counter=}')
        # отключаем блокировку
        lock.release()

    lock = Lock()
    
    t1 = Thread(target=event, args=[lock])
    t2 = Thread(target=event, args=[lock])
    t3 = Thread(target=event, args=[lock])
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    simple_threads_example()
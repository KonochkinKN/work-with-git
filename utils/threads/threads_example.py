import threading
from threading import Thread, Lock, Event
from time import sleep
import os


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
            os.system('cls')
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


def recursion_threading():
    def delayed_print(cnt):
        sleep(1)
        os.system('cls')
        print(f'all threads: {threading.active_count()}')
        print(f'{cnt = }')
        t = Thread(target=delayed_print, args=[cnt+1])
        t.start()

    delayed_print(1)


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


def traffic_light():
    green = Lock()
    traffic_off = Event()
    button_pushed = Event()

    def cars_traffic(direction):
        while not traffic_off.is_set():
            green.acquire()
            print(f'Едут автомобили по {direction}')
            sleep(3)
            green.release()
            sleep(0.1)

    def people_traffic():
        while not traffic_off.is_set():
            if button_pushed.is_set():
                green.acquire()
                print('Идут пешеходы')
                sleep(1)
                green.release()

    def traffic_menu():
        while not traffic_off.is_set():
            action = input("Выберите действие:\n"
                           "\t1) Зеленый для пешеходов (p)\n"
                           "\t2) Выход (e)\n")
            if action == 'p':
                button_pushed.set()
                sleep(0.1)
                button_pushed.clear()
            elif action == 'e':
                traffic_off.set()

    cars_thread_v = Thread(target=cars_traffic, args=['основной дороге'])
    cars_thread_h = Thread(target=cars_traffic, args=['побочной дороге'])
    people_thread = Thread(target=people_traffic)
    menu_thread = Thread(target=traffic_menu)
    menu_thread.start()
    cars_thread_v.start()
    cars_thread_h.start()
    people_thread.start()


if __name__ == '__main__':
    # simple_threads_example()
    # counter_example()
    # recursion_threading()
    # locking_example()
    traffic_light()

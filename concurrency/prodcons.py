#!/usr/bin/env python3
import random
import time

from threading import Lock
from threading import Condition
from threading import Thread
from threading import current_thread


class Merchandise:
    def __init__(self, cap=2):
        self.items = []
        self.cap = cap
        # book keeping articles
        self.mutex = Lock()
        self.item_available = Condition(self.mutex)
        self.space_available = Condition(self.mutex)

    def __repr__(self):
        return f'{self.cap:<3} {self.items}'

    def _is_item_available(self):
        return len(self.items) > 0

    def _is_space_available(self):
        return len(self.items) < self.cap

    def consume(self):
        "returns the first item in produce section"
        with self.item_available:
            # wait for items to be available
            while not self._is_item_available():
                self.item_available.wait()

            # now the item is available
            item = self.items.pop(0)

            # notify that space is available
            self.space_available.notify()

            # and finally return the item
            return item

    def produce(self, item):
        "creates a new item"
        with self.space_available:
            # wait for the space to be available
            if not self._is_space_available():
                self.space_available.wait()

            # insert the item
            self.items.append(item)

            # and notify others that item is available
            self.item_available.notify()


def test():
    m = Merchandise(5)
    # create 4 threads .. two producer two consumer
    # producer sleeps for random time pt
    # consumer sleeps for random time ct
    # and they run total 10 times
    times = 10

    def produce(pt):
        totalwait = 0
        for _ in range(times):
            # first wait for random time
            print(f'Producer {current_thread().name} sleeping')
            time.sleep(max(0, random.normalvariate(pt, 0.2)))
            print(f'Producer {current_thread().name} woke up!')

            item = random.randint(1, 100)
            print(f'Producer {current_thread().name} reports status {m}')
            print(f'Producer {current_thread().name} beginning to produce {item}')

            tick = time.time()
            # now produce
            m.produce(item)
            # note time taken
            taken = int((time.time() - tick) * 1000)
            print(f'Producer {current_thread().name} produced item {item}')
            print(f'Producer {current_thread().name} took {taken}ms')
            print(f'Producer {current_thread().name} after produce reports status {m}')
            totalwait += taken
        print(f'Producer {current_thread().name} totally waited {totalwait} milliseconds')

    def consume(ct):
        totalwait = 0
        for _ in range(times):
            # first wait for random time
            print(f'Consumer {current_thread().name} sleeping')
            time.sleep(max(0, random.normalvariate(ct, 0.2)))
            print(f'Consumer {current_thread().name} woke up!')

            print(f'Consumer {current_thread().name} reports status {m}')
            print(f'Consumer {current_thread().name} beginning to consume')

            tick = time.time()
            # now consume
            item = m.consume()
            # note time taken
            taken = int((time.time() - tick) * 1000)
            print(f'Consumer {current_thread().name} consumed item {item}')
            print(f'Consumer {current_thread().name} took {taken}ms')
            print(f'Consumer {current_thread().name} after consume reports status {m}')
            totalwait += taken
        print(f'Consumer {current_thread().name} totally waited {totalwait} milliseconds')

    tp1 = Thread(name='tp1', target=produce, args=(3.0,))
    tp2 = Thread(name='tp2', target=produce, args=(3.0,))
    tc1 = Thread(name='tc1', target=consume, args=(8.5,))
    tc2 = Thread(name='tc2', target=consume, args=(8.5,))

    # producer is faster than consumer .. so producers will wait more
    # start the threads
    consumers = [tc1, tc2]
    producers = [tp1, tp2]
    # start them now
    for t in consumers + producers:
        t.start()
    # now wait for all
    for t in consumers + producers:
        t.join()
    print('DONE!!!')

import importlib
import random
import sys
import threading
import time


def reader(resource, k, stime_mu, sigma=0.1):
    ttaken = 0

    for _ in range(1000):
        # figure out the time to sleep
        stime = max(0, random.normalvariate(stime_mu, sigma))
        print(f'{threading.current_thread().name} sleeping {stime:.2f}s')
        # and sleep
        time.sleep(stime)
        # read the time diff
        tick = time.time()
        # read the resource
        v = resource.read(k)
        # record the total time for this op
        tottime = (time.time() - tick) * 1000
        print(f'{threading.current_thread().name} read '
              f'{k} --> {v} in {tottime:.3f}ms')
        # and add to total
        ttaken += tottime

    print(f'{threading.current_thread().name} TOOK {ttaken:.2f}s')


def writer(resource, k, stime_mu, sigma=0.1):
    ttaken = 0

    for _ in range(400):
        # figure out the time to sleep
        stime = max(0, random.normalvariate(stime_mu, sigma))
        print(f'{threading.current_thread().name} sleeping {stime:.2f}s')
        # and sleep
        time.sleep(stime)
        # randomize v
        v = random.randint(100, 40000)
        # read the time diff
        tick = time.time()
        # write the resource
        resource.write(k, v)
        # record the total time for this op
        tottime = (time.time() - tick) * 1000
        print(f'{threading.current_thread().name} wrote '
              f'({k}, {v}) in {tottime:.3f}ms')
        # and add to total
        ttaken += tottime

    print(f'{threading.current_thread().name} TOOK {ttaken:.2f}s')


def test(modname):
    module = importlib.import_module(modname)
    # get the resource object
    resource = module.Resource()
    # fix on k, sleep time and no of threads now
    k = 'registerA'
    rsleep = 0.015
    wsleep = 0.035
    sigma = 0.005
    rcount = 10
    wcount = 10
    readers = []
    writers = []

    # now create some readers and writers
    for i in range(rcount):
        readers.append(
            threading.Thread(
                name=f'reader{i}', target=reader, args=(
                    resource, k, rsleep, sigma)))
    for i in range(wcount):
        writers.append(
            threading.Thread(
                name=f'writer{i}', target=writer, args=(
                    resource, k, wsleep, sigma)))

    # record the tick
    tick = time.time()
    # start the threads
    for t in readers + writers:
        t.start()

    # wait for them to finish
    for t in readers + writers:
        t.join()

    # finished the ticker .. print the recorded time
    print(f'C\'est Fini! Time taken {time.time() - tick:.2f}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        modname = 'first'
    else:
        modname = sys.argv[1]

    test(modname)

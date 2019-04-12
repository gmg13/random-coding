import random
import time

from queue import Queue
from threading import Lock, Thread, current_thread
# from weakref import WeakKeyDictionary

MAXQSIZE = 50


class ConnectionPool:
    def __init__(self, cap):
        # limit the cap by some number
        if cap > MAXQSIZE:
            raise RuntimeError(f'can you make the size smaller '
                               f'than {MAXQSIZE} please')

        # some init stuff
        # first consider the exit strategy
        # of course the threads themselves are daemon, so no worries
        self._stopping = False

        # next consider the locking strategy
        self._resplock = Lock()
        self._jobq = Queue(MAXQSIZE)
        self._responses = {}

        # and the book stuffs
        self._cap = cap
        self._threads = []
        self._jobids = set()
        self._completed_wait_time = 0.5

        # next we initialize the thread pool
        for i in range(cap):
            t = Thread(target=self._runner, daemon=True)
            self._threads.append(t)
        # and then start the threads
        for t in self._threads:
            t.start()

    # def _validate(self):
    #     if len(self._threads) < self._cap:
    #         # start another thread
    #         t = Thread(target=self._runner, daemon=True)
    #         self._threads[t] = True

    def _genid(self):
        while True:
            with self._resplock:
                jid = random.randint(1, 10000000)
                if jid in self._jobids:
                    continue
                self._jobids.add(jid)
                return jid

    def submit(self, fn, args) -> int:
        # first validate
        # self._validate()
        # create a random job id
        jid = self._genid()
        # then create the job in the jobQ
        self._jobq.put((jid, fn, args))
        # and return the job id
        return jid

    def as_completed(self, jobs):
        # check for each job if it is in completed state
        completed = []
        while not self._stopping:
            for j in jobs:
                if j in self._responses:
                    with self._resplock:
                        resp = self._responses.pop(j)
                    yield (j, resp)
                    # this is complete now ..
                    # so mark as completed
                    completed.append(j)
                    # also check for exit condition
                    if len(completed) == len(jobs):
                        return
            # and wait for some time .. maybe exponential
            # TODO .. make this exponential
            time.sleep(self._completed_wait_time)
        pass

    def close(self):
        self._stopping = True

    def _runner(self):
        # this is the run method which all the thread in the
        # thread pool run forever
        while not self._stopping:
            # now that i am done, i am ready for more work
            # get me some work
            work = self._jobq.get()
            # now let's do some work
            jobid, fn, args = work
            print(f'{current_thread().name} picked up job {jobid}')
            resp = fn(*args)
            # and store the response
            with self._resplock:
                self._responses[jobid] = resp


def test():
    def func(lbl):
        print(f'entering function func {lbl}')
        # sleep for some time
        time.sleep(1.3)
        # wake up
        print(f'time for some cofee {lbl}')
        # and return some response
        return 2 ** lbl

    # create the connection pool
    pool = ConnectionPool(5)
    # create 10 jobs and submit them
    futures = [pool.submit(func, (i,)) for i in range(10)]
    # run through the futures and print as they complete
    for jid, resp in pool.as_completed(futures):
        print(f'Job {jid} completed -> {resp}')

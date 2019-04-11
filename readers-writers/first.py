from threading import Lock


class Resource:
    "first basic version of readers writers"
    def __init__(self):
        # let's make this a dictionary
        self.resource = {}
        # and all the other concurrency constructs here
        self.rc = 0  # readers count
        self.wmutex = Lock()
        self.rmutex = Lock()

    def write(self, k, v):
        "write an item v in k"
        with self.wmutex:
            self.resource[k] = v

    def read(self, k):
        "read an item in k"
        # entry section
        with self.rmutex:
            self.rc += 1
            # this so that any reader is locking a writer out
            if self.rc == 1:
                self.wmutex.acquire()

        # now read the value with peace
        ret = self.resource.get(k)

        # exit section
        with self.rmutex:
            self.rc -= 1
            # now release writers in case of no readers
            if not self.rc:
                self.wmutex.release()

        # return the value
        return ret

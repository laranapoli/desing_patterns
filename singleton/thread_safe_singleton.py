import threading


class ThreadSafeSingleton:
    # class level variable and lock
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:  # acquires the lock
            if not cls._instance:
                cls._instance = super().__new__(cls)



# use
s1 = ThreadSafeSingleton()
import threading


class SingletonGenerator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance._current = 0
            return cls._instance

    def get_next_number(self):
        self._current += 1
        return self._current
    

gen = SingletonGenerator()
gen2 = SingletonGenerator()
gen3 = SingletonGenerator()

print(gen.get_next_number())
print(gen2.get_next_number())
print(gen2.get_next_number())
print(gen3.get_next_number())
print(gen.get_next_number())
print(gen2.get_next_number())
print(gen.get_next_number())
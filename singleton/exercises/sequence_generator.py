class SingletonGenerator:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._current = 0
        return cls._instance

    def get_next_number(self):
        self._current += 1
        return self._current
    

gen = SingletonGenerator()
print(gen.get_next_number())
print(gen.get_next_number())
print(gen.get_next_number())
print(gen.get_next_number())
class SingletonGenerator:
    _instance = None
    _current_number = 0

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._current_number = 0
        return cls._instance

    def get_next_number(self):
        number = self._current_number
        self._current_number += 1
        return number
    

if __name__ == "__main__":
    gen = SingletonGenerator()
    gen2 = SingletonGenerator()

    print(f"Gen 1: {gen.get_next_number()}")
    print(f"Gen 2: {gen2.get_next_number()}")
    print(f"Gen 2: {gen2.get_next_number()}")
    print(f"Gen 1: {gen.get_next_number()}")
    print(f"Gen 2: {gen2.get_next_number()}")
    print(f"Gen 1: {gen.get_next_number()}")
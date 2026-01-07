class EagerSingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance

    def __call__(cls, *args, **kwargs):
        if args or kwargs:
            raise TypeError(
                f"{cls.__name__} is an eager singleton and "
                "does not accept constructor arguments"
            )
        return cls._instances[cls]


class SingletonGeneratorTwo(metaclass=EagerSingletonMeta):
    
    def __init__(self):
        self._current = 0

    def get_next_number(self):
        self._current += 1
        return self._current
    


gen = SingletonGeneratorTwo()
gen2 = SingletonGeneratorTwo()
gen3 = SingletonGeneratorTwo()

print(gen.get_next_number())
print(gen2.get_next_number())
print(gen2.get_next_number())
print(gen3.get_next_number())
print(gen.get_next_number())
print(gen2.get_next_number())
print(gen.get_next_number())
class EagerSingletonMeta(type):
    _instances = {}
    # override: called during creation of sub-types
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # EAGER LOADING
        cls._instances[cls] = super().__call__()
    
    # returns  the singleton instance
    def __call__(cls, *args, **kwds):
        return cls._instances[cls]
    

class SingletonGeneratorTwo(metaclass=EagerSingletonMeta):
    
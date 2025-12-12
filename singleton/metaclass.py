# ----------------- LAZY INSTANTIATION ------------------------
# metaclass substitui o comportamento de __calll__ da subclasse
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]
    

class Singleton(metaclass=SingletonMeta):
    def some_logic(self):
        pass


# use
s1 = Singleton()


# ----------------- EAGER LOADING ------------------------
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
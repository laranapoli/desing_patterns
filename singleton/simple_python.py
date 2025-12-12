class Singleton:
    _instance = None

    def __new__(cls):
        # NOTE: lazy instantiation
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance
    

# use
s1 = Singleton()
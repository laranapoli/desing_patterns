class ClassicSingleton:
    # class level variable
    _instance = None

    def __init__(self):
        # prevent constructor utilization
        raise RuntimeError('Call instance() instead')
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:  # NOTE: lazy instantiation
            cls._instance = ClassicSingleton
        return cls._instance


# use
s1 = ClassicSingleton.get_instance()
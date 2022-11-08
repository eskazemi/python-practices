from abc import ABC


class Base(ABC):
    _id = 0
    object_list = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def store(cls, obj):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(obj)

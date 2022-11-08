from abc import ABC
from manager import Manager


class Base(ABC):
    _id = 0
    object_list = None
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.set_manager()
        self.store(self)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)

    @classmethod
    def store(cls, obj):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(obj)

class Manager:

    def __init__(self, _class):
        self._class = _class

    def __str__(self):
        print(f"{self._class}")

    def search(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        results = list()
        maximum = False
        minimum = False
        for key, value in kwargs.items():
            if key.endswith("__min"):
                key = key[:-5]
                minimum = True
            if key.endswith("__max"):
                key = key[:-5]
                maximum = True

            for obj in self._class.object_list:
                if hasattr(obj, key):
                    if minimum and maximum:
                        result = value <= getattr(obj, key) >= value
                    elif maximum:
                        result = getattr(obj, key) <= value
                    elif minimum:
                        result = getattr(obj, key) >= value
                    else:
                        result = getattr(obj, key) == value
                    if result:
                        results.append(obj)

        return results


    def get(self, **kwargs):
        maximum = False
        minimum = False
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if minimum and maximum:
                    result = value <= getattr(obj, key) >= value
                elif maximum:
                    result = getattr(obj, key) <= value
                elif minimum:
                    result = getattr(obj, key) >= value
                else:
                    result = getattr(obj, key) == value
                if result:
                    return obj



    def count(self):
        return len(self._class.object_list)


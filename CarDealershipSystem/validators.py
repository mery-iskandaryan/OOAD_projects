class StringValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Value must be a non empty string.")
        instance.__dict__[self.name] = value


class PositiveNumberValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (float, int)) or value < 0:
            raise ValueError("Value must be a non negative number.")
        instance.__dict__[self.name] = value



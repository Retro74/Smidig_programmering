class MyClass:
    def __init__(self, verdi):
        self._value = verdi

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        raise AttributeError("Denne egenskapen kan ikke endres")

# Eksempelbruk
obj = MyClass(77)
print(obj._value)
obj._value = 100  # Vil kaste en AttributeError
print(obj._value)

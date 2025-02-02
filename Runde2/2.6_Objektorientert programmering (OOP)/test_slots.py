class MyClass:
    __slots__ = ('value','baba')  # Kun disse attributtene er tillatt

    def __init__(self):
        self.value = 42
        self.baba = 22

# Eksempelbruk
obj = MyClass()
print(obj.value)  # 42
obj.value = 100  # Vil kaste en AttributeError
print(obj.value)  # 42

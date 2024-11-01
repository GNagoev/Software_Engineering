class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        if hasattr(self, '_value'):
            return self._value
        else:
            raise AttributeError("Значение было удалено")

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")


obj = MyClass(42)
print(obj.value)
obj.set_value(45)
print(obj.value)
obj.set_value(100)
print(obj.value)
obj.del_value()
try:
    print(obj.value)
except AttributeError as e:
    print(e)
#Проблема была в том что геттер принимал value, и в том что после удаления value, мы пытались вывести его без проверки его удалдения.

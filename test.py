class Test:
    def __init__(self):
        self.foo = 11
        self._bar_= 23
        self.__baz = 23
t = Test()
print(dir(t))
info = {'1': 5, '2': 2, '3': 10}
# new_info = sorted(info, key=info.values(), )
# print(info.items())
# li = sorted(info.items(), key=lambda e: e[1], reverse=True)
# print(li)


class Foo:
    __x = 1

    # @staticmethod
    def func(self):
        print(Foo.__x)
        print(self.__x)

obj = Foo()
# print(Foo.__x)
# print(obj.__x)
print(obj._Foo__x)
li = []
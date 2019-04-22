import os

print('============================')


def li_file(dirname):
    for a, b, c in os.walk(dirname):
        for i in c:
            i = os.path.abspath(i)
            print(i)


dir = __file__
li_file(dir)
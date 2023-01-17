def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def fun1():
    pass


print(__name__)
if __name__ == '__main__':
    print(f'I am my_module: {__name__}')  # __name__ = '__main__'
    print(type(__name__))
    res = add(100, 202)
    print(res)

# Python creates a variable __name__. The value of __name__ is '__main__' for the file which we run
# If the python file is imported, the value of __name__ variable for the imported file (module) is the module name.

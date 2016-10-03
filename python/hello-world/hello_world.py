#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name='World'):
    helloObject = name if name else "World"
    return "Hello, %s!" % (helloObject)



def madd(x,y):

    """

    :param x:
    :param y:
    :return: a + b
    """
    return x + y


def mmultiply(a,b):
    """

    :param a:
    :param b:
    :return: a * b
    """
    return  a * b


def msubtract(a,b):
    """

    :param a:
    :param b:
    :return: a-b
    """

    return a -b


def divide(a,b):
    """

    :param a:
    :param b:
    :return: a/b
    """
    if b == 0:
        raise ValueError
    else:
        return a/b


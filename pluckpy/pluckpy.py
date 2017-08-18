# -*- coding: utf-8 -*-

"""Main module."""


def pluck(dictionary, key):
    """
    Return array.

    :param dictionary: array
    :param key: string
    """
    try:
        ages = [li[key] for li in dictionary]
        return ages
    except KeyError as e:
        raise KeyError(e.message)
    except TypeError as e:
        raise TypeError(e.message)

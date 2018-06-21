import re


def cat_dog(str):
    """
    This function checks if "cat" and "dog" appears in a given string the same number os times.

    :param str: It receives a string that contains "cat" and "dog"
    :type str: String
    :return: It returns True if "cat" and "dog" appears the same number of times, otherwise False
    :rtype: bool
    """
    cat = len(re.findall('cat', str))  # Verify how many times 'cat' appears in str
    dog = len(re.findall('dog', str))  # Verify how many times 'dog' appears in str
    return cat == dog

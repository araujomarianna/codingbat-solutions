def sleep_in(weekday, vacation):
    """
    This function verifies if you can or cannot sleep taking into account weekday and vacation values.

    :param weekday: Any bool value
    :type weekday: bool
    :param vacation: Any bool value
    :type vacation: bool
    :return: It returns True if weekday is False or vacation is True
    :rtype: bool
    """
    return not weekday or vacation



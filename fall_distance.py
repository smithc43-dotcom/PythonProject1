def fall_distance(time):
    """
    Calculates the distance an object falls due to gravity
    given the time in seconds.

    Parameters:
        time (float): Time in seconds the object has been falling

    Returns:
        float: Distance fallen in meters
    """
    g = 9.8
    return 0.5 * g * (time ** 2)



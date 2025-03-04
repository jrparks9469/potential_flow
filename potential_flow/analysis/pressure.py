def pressure_coefficient(flow, x_coordinates, y_coordinates, u_inf):
    """Calculates the pressure at a given x and y location

    Pressure coefficient is related to the local velocity by
    Bernoulli's equation:
    Cp = (p - p_inf) / q

    Parameters
    ----------
    flow : PotentialFlow object
        The potential flow field.
    x_coordinates: array_like
        x-coordinates of the points.
    y_coordinates: array_like
        y-coordinates of the points.

    Returns
    -------
    array_like
        Pressure coefficients at the given points.
    """
    velocity_x, velocity_y = flow.velocity(x_coordinates, y_coordinates)
    velocity_mag = (velocity_x**2 + velocity_y**2)**0.5

    pressure_coefficient = 1 - (velocity_mag / u_inf)**2

    return pressure_coefficient
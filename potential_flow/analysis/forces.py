import numpy as np

def calculate_force(flow, body_points, density=1.0):
    """Calculates the force on a body in a potential flow.

    This function uses the pressure integration method to calculate the force
    on a body.  It assumes that the body is represented by a set of points
    that define its surface.

    Parameters
    ----------
    flow : PotentialFlow object
        The potential flow field.
    body_points : array_like, shape (n_points, 2)
        A 2D array of points representing the surface of the body. Each row
        should be [x, y].
    density : float, optional
        The fluid density, by default 1.0.

    Returns
    -------
    tuple : (force_x, force_y)
        The x and y components of the force on the body.
        Returns (0,0) if the body_points array is empty.
    """

    if not body_points.size:
        return 0, 0

    body_points = np.asarray(body_points)

    n_points = body_points.shape[0]
    force_x = 0.0
    force_y = 0.0

    for i in range(n_points):
        # Approximate tangent vector (very basic - needs improvement for real applications)
        # More sophisticated methods would involve curve fitting or other techniques
        if i < n_points - 1:
            next_point = body_points[i + 1]
        else:
            next_point = body_points[0] # loop back to the first point

        dx = next_point[0] - body_points[i][0]
        dy = next_point[1] - body_points[i][1]
        ds = np.sqrt(dx**2 + dy**2)

        if ds == 0: # handling zero length segments
            continue

        nx = dy / ds # normal vector x component
        ny = -dx / ds # normal vector y component

        x, y = body_points[i]
        u, v = flow.velocity(x, y)
        q_squared = u**2 + v**2
        pressure = 0.5 * density * q_squared  # Dynamic pressure

        force_x += pressure * nx * ds
        force_y += pressure * ny * ds

    return force_x, force_y
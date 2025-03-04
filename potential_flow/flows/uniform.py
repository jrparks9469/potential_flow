import numpy as np
from .potential_flow import PotentialFlow


class UniformFlow(PotentialFlow):
    """Represents a uniform flow.

    Parameters
    ----------
    u_inf : float, optional
        Velocity in the x-direction, by default 1.0.
    v_inf : float, optional
        Velocity in the y-direction, by default 0.0.
    x_center : float, optional
        x-coordinate of the center of the flow element, by default 0.0
    y_center : float, optional
        y-coordinate of the center of the flow element, by default 0.0
    """

    def __init__(self, u_inf=1.0, v_inf=0.0, x_center=0.0, y_center=0.0):
        super().__init__(x_center=x_center, y_center=y_center)
        self.u_inf = u_inf
        self.v_inf = v_inf


    def velocity(self, x_coordinates, y_coordinates):
        """Implementation of the PotentialFlow velocity method."""
        return np.full_like(x_coordinates, self.u_inf), np.full_like(y_coordinates, self.v_inf)


    def stream_function(self, x_coordinates, y_coordinates):
        """Implementation of the PotentialFlow stream_function method."""
        return self.u_inf * (y_coordinates - self.y_center) - self.v_inf * (x_coordinates - self.x_center)


    def potential_function(self, x_coordinates, y_coordinates):
        """Implementation of the PotentialFlow potential_function method."""
        return self.u_inf * (x_coordinates - self.x_center) + self.v_inf * (y_coordinates - self.y_center)
import numpy as np
from .potential_flow import PotentialFlow


class Doublet(PotentialFlow):
    """Represents a doublet flow.

    Parameters
    ----------
    flow_strength : float, optional
        Strength of the doublet, by default 1.0.
    x_center : float, optional
        x-coordinate of the center of the flow element, by default 0.0
    y_center : float, optional
        y-coordinate of the center of the flow element, by default 0.0
    """


    def __init__(self, flow_strength=1.0, x_center=0.0, y_center=0.0):
        super().__init__(flow_strength, x_center, y_center)


    def velocity(self, x_coordinates, y_coordinates):
        """Implementation of the PotentialFlow velocity method."""
        dx = x_coordinates - self.x_center
        dy = y_coordinates - self.y_center
        r_fourth = (dx**2 + dy**2)**2

        u = -(self.flow_strength / (2 * np.pi)) * (dx**2 - dy**2) / r_fourth
        v = -(self.flow_strength / (2 * np.pi)) * 2 * dx * dy / r_fourth

        return u, v


    def stream_function(self, x_coordinates, y_coordinates):
        """Implementation of the PotentialFlow stream_function method."""
        dx = x_coordinates - self.x_center
        dy = y_coordinates - self.y_center

        return -(self.flow_strength / (2 * np.pi)) * dy / (dx**2 + dy**2)


    def potential_function(self, x_coordinates, y_coordinates):
        """Implementation of the PotentialFlow potential_function method."""
        dx = x_coordinates - self.x_center
        dy = y_coordinates - self.y_center

        return (self.flow_strength / (2 * np.pi)) * dx / (dx**2 + dy**2)
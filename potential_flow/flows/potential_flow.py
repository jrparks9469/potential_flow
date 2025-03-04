from abc import ABC, abstractmethod


class PotentialFlow(ABC):
    """Abstract base class for potential flow.

    Parameters
    ----------
    flow_strength: float, optional
        Strength of the potential flow, by default 1.0.
    x_center: float, optional
        x-coordinate of the center of the flow element, by default 0.0
    y_center: float, optional
        y-coordinate of the center of the flow element, by default 0.0
    """

    def __init__(self, flow_strength=1.0, x_center=0.0, y_center=0.0):
        self.flow_strength = flow_strength
        self.x_center = x_center
        self.y_center = y_center

    
    @abstractmethod
    def velocity(self, x_coordinates, y_coordinates):
        """Returns the velocity components (u, v) at (x, y).

        Parameters
        ----------
        x_coordinates: array_like
            x-coordinates of the points.
        y_coordinates: array_like
            y-coordinates of the points.

        Returns
        -------
        tuple of array_like
            Tuple containing the u and v velocity components.
        """
        raise NotImplementedError


    @abstractmethod
    def stream_function(self, x_coordinates, y_coordinates):
        """Returns the stream function value at (x, y).

        Parameters
        ----------
        x_coordinates: array_like
            x-coordinates of the points.
        y_coordinates: array_like
            y-coordinates of the points.

        Returns
        -------
        array_like
            Stream function values at the given points.
        """
        raise NotImplementedError


    @abstractmethod
    def potential_function(self, x_coordinates, y_coordinates):
        """Returns the potential function value at (x, y).

        Parameters
        ----------
        x_coordinates: array_like
            x-coordinates of the points.
        y_coordinates: array_like
            y-coordinates of the points.

        Returns
        -------
        array_like
            Potential function values at the given points.
        """
        raise NotImplementedError
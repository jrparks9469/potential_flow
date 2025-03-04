import numpy as np
from ..flows.potential_flow import PotentialFlow

def combine_flows(*flows):
    """Combines multiple potential flows using superposition.

    Parameters
    ----------
    *flows : PotentialFlow objects
        A variable number of PotentialFlow objects to combine.

    Returns
    -------
    CombinedFlow : A new PotentialFlow object representing the superposition.
    """

    class CombinedFlow(PotentialFlow):  # Dynamically create the combined flow class
        def __init__(self, flows):
            super().__init__()  # Initialize the base class
            self.flows = flows
        

        def velocity(self, x_coordinates, y_coordinates):
            u_combined = np.zeros_like(x_coordinates)  # Initialize with zeros
            v_combined = np.zeros_like(y_coordinates)

            for flow in self.flows:
                u, v = flow.velocity(x_coordinates, y_coordinates)
                u_combined += u
                v_combined += v

            return u_combined, v_combined


        def stream_function(self, x_coordinates, y_coordinates):
            psi_combined = np.zeros_like(x_coordinates) # Initialize with zeros

            for flow in self.flows:
                psi_combined += flow.stream_function(x_coordinates, y_coordinates)
            return psi_combined


        def potential_function(self, x_coordinates, y_coordinates):
            phi_combined = np.zeros_like(x_coordinates)

            for flow in self.flows:
                phi_combined += flow.potential_function(x_coordinates, y_coordinates)
            return phi_combined

    return CombinedFlow(flows)  # Return an instance of the combined flow class
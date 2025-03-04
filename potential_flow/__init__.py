"""
The `potential_flow` package provides tools for working with potential flows.

Subpackages:
-----------
flows : Contains classes for different types of potential flows (uniform, source, vortex, etc.).
analysis : Contains functions for analyzing potential flows (superposition, force calculations, etc.).
visualization : Contains functions for visualizing potential flows (plotting streamlines, etc.).
"""

# Import the abstract base class (essential)
from .flows.potential_flow import PotentialFlow

# Import flow classes from the flows subpackage
from .flows.uniform import UniformFlow
from .flows.source import Source
from .flows.vortex import Vortex
from .flows.doublet import Doublet

# Import analysis tools from the analysis subpackage (if any)
from .analysis.superposition import combine_flows
from .analysis.forces import calculate_force
from .analysis.pressure import pressure_coefficient
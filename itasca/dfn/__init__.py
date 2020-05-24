from typing import Any, Tuple

from . import fracture
from . import template
from . import inter
from . import setinter
from . import vertex

def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid dfn objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass

def center_density(*args, **kwargs) -> Any:
    """
    (lower=domain lower bound, upper=domain upper bound) -> float.
    Get the fracture center density.
    The fracture center density is defined as the {P20 value in 2D; P30 value in 3D} as measured in the specified region.
    {P20 in 2D; P30 in 3D} is the number of fracture centers in the specified region per unit area (volume).
    All fractures from all dfns are used in this calculation.
    """
    pass

def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of dfns.
    """
    pass

def create(*args, **kwargs) -> Any:
    """
    (dfn_name=Empty) -> DFN object.
    Create an empty dfn with optional name dfn_name.
    """
    pass

def density(*args, **kwargs) -> Any:
    """
    (lower=domain lower bound, upper=domain upper bound) -> float.
    Get the fracture mass density.
    The fracture mass density is defined as the {P21 value in 2D; P32 value in 3D} as measured in the specified region.
    {P21 in 2D; P32 in 3D} is the cumulated fracture length (surface) in the specified region per unit area (volume).
    All fractures from all dfns are used in this calculation.
    """
    pass

def find(*args, **kwargs) -> Any:
    """
    (id: int or name: str) -> DFN object.
    Get the dfn object with the given ID number or name.
    """
    pass

def list(*args, **kwargs) -> Any:
    """
    () -> DFN iterator object.
    Get a dfn iterator object.
    """
    pass

def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum dfn ID.
    """
    pass

def p10(*args, **kwargs) -> Any:
    """
    (pt1=origin, pt2=origin) -> float.
    Get the P10, or the fracture density per unit length, along the line from pt1 to pt2.
    All fractures from all dfns are used in this calculation.
    """
    pass

def percolation(*args, **kwargs) -> Any:
    """
    (lower=domain lower bound, upper=domain upper bound) -> float.
    Get the fracture percolation.
    The fracture percolation is measured in the region and is defined as {the sum of the squared fracture lengths per unit area in 2D; the sum of pi^2 (area/pi)^(1.5) per unit volume, where area is the fracture area in 3D}.
    """
    pass

class DFN:
    __hash__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass
    
    def center_density(self, *args, **kwargs) -> Any:
        """
        (lower=domain lower bound, upper=domain upper bound) -> float.
        Get the fracture center density.
        The fracture center density is defined as the {P20 value in 2D; P30 value in 3D} as measured in the specified region.
        {P20 in 2D; P30 in 3D} is the number of fracture centers in the specified region per unit area (volume).
        """
        pass
    
    def clone_fracture(self, *args, **kwargs) -> Any:
        """
        (Fracture object) -> Fracture object.
        Clone the fracture, creating a new one in the dfn.
        The fracturecan come from any dfn.
        """
        pass
    
    def contacts(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with the fractures in this dfn.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass
    
    def create_fracture(self, *args, **kwargs) -> Any:
        """
        (pos=origin, size=0, dip=0 ,dipdir=0 (3D ONLY), id=0, vertices=array) -> Fracture object.
        Create a fracture and addit to this dfn.
        In 3D a disk shaped fracture can be created where size is the fracture diameter, pos is the center of the fracture and dip/dipdir and the dip and dip direction in degrees, respectively.In 2D, a line segement fracture can be created where size is the fracture length, pos is the center and dip is the fracture dip in degrees.
        Otherwise one may specify a number of verticesfor {2 in 2D; 3 or more in 3D} that delineate the fracture vertices.
        """
        pass
    
    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete this DFN.
        """
        pass
    
    def density(self, *args, **kwargs) -> Any:
        """
        (lower=domain lower bound, upper=domain upper bound) -> float.
        Get the fracture mass density.
        The fracture mass density is defined as the {P21 value in 2D; P32 value in 3D} as measured in the specified region.
        {P21 in 2D; P32 in 3D} is the cumulated fracture length (surface) in the specified region per unit area (volume).
        """
        pass
    
    def dominance(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the dfn dominance.
        """
        pass
    
    def fracture_count(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the number of fractures in this dfn.
        """
        pass
    
    def fracture_near(self, *args, **kwargs) -> Any:
        """
        (point: vec, radius=0.0) -> Fracture object.
        Find the closest fracture to a point.
        If the optional keyword argument radius is non-zero, only search within this radius.
        """
        pass
    
    def fractures(self, *args, **kwargs) -> Any:
        """
        () -> Fracture iterator object.
        Get a fracture iterator object.
        """
        pass
    
    def fractures_inbox(self, *args, **kwargs) -> Any:
        """
        (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of fracture objects.
        Get a tuple of fractures with extents intersecting a box.
        The extent is the axis-aligned bounding box of the fracture.
        The if the optional keyword argument intersect is False only fractures entirely falling within the box are returned.
        Only fractures belonging to this dfn are are searched.
        """
        pass
    
    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the dfn id.
        """
        pass
    
    def name(self, *args, **kwargs) -> Any:
        """
        () -> string.
        Get the dfn name.
        """
        pass
    
    def p10(self, *args, **kwargs) -> Any:
        """
        (pt1=origin, pt2=origin) -> float.
        Get the P10, or the fracture density per unit length, along the line from pt1 to pt2.
        """
        pass
    
    def percolation(self, *args, **kwargs) -> Any:
        """
        (lower=domain lower bound, upper=domain upper bound) -> float.
        Get the fracture percolation.
        The fracture percolation is measured in the region and is defined as {the sum of the squared fracture lengths per unit area in 2D; the sum of pi^2 (area/pi)^(1.5) per unit volume, where area is the fracture area in 3D}.
        """
        pass
    
    def set_dominance(self, *args, **kwargs) -> Any:
        """
        (value: int) -> None.
        Set the dfn dominance.
        """
        pass
    
    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of all fractures of this dfn.
        """
        pass
    
    def template(self, *args, **kwargs) -> Any:
        """
        () -> DFN Template object.
        Get the template used to create this dfn.
        """
        pass
    
    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this dfn is live.
        """
        pass
    
    def __eq__(self, other) -> Any:
        """
        Return self==value.
        """
        pass
    
    def __ge__(self, other) -> Any:
        """
        Return self>=value.
        """
        pass
    
    def __gt__(self, other) -> Any:
        """
        Return self>value.
        """
        pass
    
    def __le__(self, other) -> Any:
        """
        Return self<=value.
        """
        pass
    
    def __lt__(self, other) -> Any:
        """
        Return self<value.
        """
        pass
    
    def __ne__(self, other) -> Any:
        """
        Return self!=value.
        """
        pass
    

class DFNIter:
    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass
    
    def __iter__(self) -> Any:
        """
        Implement iter(self).
        """
        pass
    
    def __next__(self) -> Any:
        """
        Implement next(self).
        """
        pass
    

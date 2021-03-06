from typing import Any, Tuple

def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid thermal pebble objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass

def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of thermal pebbles.
    """
    pass

def find(*args, **kwargs) -> Any:
    """
    (id: int) -> Thermal pebble object.
    Get the thermal pebble object with the given ID number.
    """
    pass

def inbox(*args, **kwargs) -> Any:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of thermal pebble objects.
    Get a tuple of thermal pebbles with extents intersecting a box.
    The extent is the axis-aligned bounding box of the pebble.
    The if the optional keyword argument intersect is False then only thermal pebbles with positions falling in the box are returned.
    """
    pass

def list(*args, **kwargs) -> Any:
    """
    () -> Thermal pebble iterator object.
    Get a thermal pebble iterator object.
    """
    pass

def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum thermal pebble ID.
    """
    pass

def near(*args, **kwargs) -> Any:
    """
    (point: vec, radius=0.0) -> Thermal pebble object.
    Find the closest thermal pebble to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass

class ThermalPebble:
    __hash__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass
    
    def clump(self, *args, **kwargs) -> Any:
        """
        () -> Thermal clump object.
        Get the thermal clump corresponding to this pebble.
        """
        pass
    
    def contact_count(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this thermal pebble.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The optional type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the optional keyword argument all is True the count includes virtual contacts.
        """
        pass
    
    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this thermal pebble.
        An optional argument can be included which is a piece object (a thermal ball, a thermal pebble or a thermal facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass
    
    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the thermal pebble extra data in the given slot.
        """
        pass
    
    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: int]) -> str.
        Get the thermal pebble group name in a given slot.
        """
        pass
    
    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str ) -> int.
        Remove from the given group from the thermal pebble.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass
    
    def groups(self, *args, **kwargs) -> Any:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this thermal pebble.
        """
        pass
    
    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Returns True if the thermal pebble has the given surface property.
        """
        pass
    
    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the thermal pebble id.
        """
        pass
    
    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Test if the thermal pebble is part of a given group.
        All group slots are searched.
        """
        pass
    
    def pebble(self, *args, **kwargs) -> Any:
        """
        () -> Pebble object.
        Get the pebble corresponding to this thermal pebble.
        """
        pass
    
    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the thermal pebble location (vector).
        """
        pass
    
    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the thermal pebble location.
        """
        pass
    
    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the thermal pebble location.
        """
        pass
    
    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this thermal pebble.
        """
        pass
    
    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this thermal pebble.
        """
        pass
    
    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the thermal pebble extra data in the given slot.
        """
        pass
    
    def set_group(self, *args, **kwargs) -> Any:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the thermal pebble group name in a given slot.
        """
        pass
    
    def set_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the thermal pebble location (vector).
        """
        pass
    
    def set_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the thermal pebble location.
        """
        pass
    
    def set_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the thermal pebble location.
        """
        pass
    
    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this thermal pebble.
        """
        pass
    
    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this thermal pebble is live.
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
    

class ThermalPebbleIter:
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
    

from typing import Any

def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass

def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of facets.
    """
    pass

def find(*args, **kwargs) -> Any:
    """
    (id: int) -> Facet object.
    Get the facet object with the given ID number.
    """
    pass

def inbox(*args, **kwargs) -> Any:
    """
    (lower_bound: vec, upper_bound: vec, boundary=False) -> tuple of Facet objects.
    Get facets with extents intersecting a box.
    If the optional keyword argument boundary is True only return the facets inside the extent.
    """
    pass

def list(*args, **kwargs) -> Any:
    """
    () -> Facet Iterator object.
    Get a wall_facet iterator object.
    """
    pass

def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum facet ID.
    """
    pass

def near(*args, **kwargs) -> Any:
    """
    (point: vec) -> Facet object.
    Find the closest facet to a point.
    """
    pass

class Facet:
    __hash__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass
    
    def active(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the facet activity code.
        The following codes apply: 0 - both sides are active; 1 - the top side (e.g., in the direction of the facet normal) is active; -1 - the bottom side of the facet is active; or 2 - neither side of the facet is active.
        """
        pass
    
    def contact_count(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this Facet.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the count includes virtual contacts.
        """
        pass
    
    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece: object], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this Facet.
        An optional argument can be included which is a piece object (a Ball, a Pebble or a Facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass
    
    def conveyor(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the facet conveyor velocity (vector).
        """
        pass
    
    def conveyor_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the facet conveyor velocity.
        """
        pass
    
    def conveyor_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the facet conveyor velocity.
        """
        pass
    
    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete a facet.
        The wall position is automatically updated.
        """
        pass
    
    def edge_neighbors(self, *args, **kwargs) -> Any:
        """
        () -> tuple of Facet objects.
        Get the neighboring facets.
        Neighboring facets are those sharing a {vertex in 2D; edge in 3D}.
        The tuple is length 3 in 3D and length 2 in 2D.
        Each position in the tuple contains either a Facet object or None if no facet is adjacent to that edge (point in 2d).
        """
        pass
    
    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the facet extra data in the given slot.
        """
        pass
    
    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the facet group name in a given slot.
        """
        pass
    
    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the facet.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass
    
    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this facet is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass
    
    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Returns True if the facet has the given surface property.
        """
        pass
    
    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the facet id.
        """
        pass
    
    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the facet is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass
    
    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the facet normal direction (vector).
        """
        pass
    
    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the facet normal direction.
        """
        pass
    
    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the facet normal direction.
        """
        pass
    
    def point_near(self, *args, **kwargs) -> Any:
        """
        (point: vec) -> vec.
        Get the closest point on the facet to another point.
        """
        pass
    
    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the facet location (vector).
        """
        pass
    
    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the facet location.
        """
        pass
    
    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the facet location.
        """
        pass
    
    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this facet.
        """
        pass
    
    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this facet.
        """
        pass
    
    def set_active(self, *args, **kwargs) -> Any:
        """
        (activity_code: int) -> None.
        The following codes apply: 0 - both sides are active; 1 - the top side (e.g., in the direction of the facet normal) is active; -1 - the bottom side of the facet is active; or 2 - neither side of the facet is active.
        """
        pass
    
    def set_conveyor(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the facet conveyor velocity (vector).
        """
        pass
    
    def set_conveyor_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the facet conveyor velocity.
        """
        pass
    
    def set_conveyor_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the facet conveyor velocity.
        """
        pass
    
    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the facet extra data in the given slot.
        """
        pass
    
    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the facet group name in a given slot.
        """
        pass
    
    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this facet.
        """
        pass
    
    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this facet is live.
        """
        pass
    
    def vertices(self, *args, **kwargs) -> Any:
        """
        () -> tuple of WallVertex objects.
        Get the facet vertices.
        """
        pass
    
    def wall(self, *args, **kwargs) -> Any:
        """
        () -> Wall object.
        Get the facet's wall.
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
    

class FacetIter:
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
    

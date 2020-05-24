from typing import Any

from . import facet
from . import vertex
from . import thermal

def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass

def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of walls.
    """
    pass

def energy(*args, **kwargs) -> Any:
    """
    (energy_name: str) -> double.
    Get the wall total energy contribution.
    The string argument is the energy name, "energy-boundary" is the only energy type defined.
    """
    pass

def find(*args, **kwargs) -> Any:
    """
    (id: int or str) -> Wall object.
    Get the Wall object with the given ID number or the name.
    """
    pass

def inbox(*args, **kwargs) -> Any:
    """
    (lower_bound: vec, upper_bound: vec, boundary=False) -> tuple of Wall objects.
    Get walls with extents intersecting a box.
    If the optional keyword argument boundary is True only return the walls inside the extent.
    """
    pass

def list(*args, **kwargs) -> Any:
    """
    () -> Wall object iterator.
    Get a wall iterator object.
    """
    pass

def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum wall ID.
    """
    pass

def near(*args, **kwargs) -> Any:
    """
    (point: vec) -> Wall object.
    Find the closest wall to a point.
    """
    pass

class Wall:
    __hash__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass
    
    def closed(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the wall closure status.
        A closed wall is one where all edges are shared.
        """
        pass
    
    def contact_count(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> int.
        Get number of contacts associated with this Wall.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the count includes virtual contacts.
        """
        pass
    
    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece: object], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this Wall.
        An optional argument can be included which is a piece object (a Ball, a Pebble or a wallFacet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass
    
    def convex(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the convexity status.
        The wall must also be closed to be convex.
        """
        pass
    
    def cutoff(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the cutoff angle.
        The cutoff angle is used during contact resolution to determine whether or not contact state information is propagated.
        """
        pass
    
    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete this wall.
        """
        pass
    
    def disp(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the wall displacement (vector).
        """
        pass
    
    def disp_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the wall displacement.
        """
        pass
    
    def disp_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the wall displacement.
        """
        pass
    
    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the wall extra data in the given slot.
        """
        pass
    
    def facets(self, *args, **kwargs) -> Any:
        """
        () -> Facet iterator object.
        Get the facets of the wall.
        """
        pass
    
    def force_contact(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the wall contact force (vector).
        """
        pass
    
    def force_contact_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the wall contact force.
        """
        pass
    
    def force_contact_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the wall contact force.
        """
        pass
    
    def fragment(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the wall fragment ID.
        """
        pass
    
    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the wall group name in a given slot.
        """
        pass
    
    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the wall.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass
    
    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this wall is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass
    
    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the wall id.
        """
        pass
    
    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the wall is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass
    
    def inside(self, *args, **kwargs) -> Any:
        """
        (point: vec) -> bool.
        Test whether a point is inside a wall.
        The wall must be closed.
        """
        pass
    
    def moment_contact(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the wall contact moment.
        """
        pass
    
    def name(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the wall name.
        Once a wall has been created its name cannot be changed.
        """
        pass
    
    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the wall location (vector).
        """
        pass
    
    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the wall location.
        """
        pass
    
    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the wall location.
        """
        pass
    
    def rotation(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the wall orientation.
        """
        pass
    
    def rotation_center(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the wall center of rotation (vector).
        """
        pass
    
    def rotation_center_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the wall center of rotation.
        """
        pass
    
    def rotation_center_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the wall center of rotation.
        """
        pass
    
    def servo_active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the wall servo activity status.
        """
        pass
    
    def servo_force(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the wall servo force.
        """
        pass
    
    def servo_gain(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the wall servo gain.
        """
        pass
    
    def servo_gainfactor(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the wall servo gain relaxation factor.
        """
        pass
    
    def servo_gainupdate(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the wall servo gain update interval.
        """
        pass
    
    def servo_set_active(self, *args, **kwargs) -> Any:
        """
        (b:bool) -> None.
        Set the wall servo activity status.
        """
        pass
    
    def servo_set_force(self, *args, **kwargs) -> Any:
        """
        (force:vec) -> None.
        Set the wall servo force.
        """
        pass
    
    def servo_set_gainfactor(self, *args, **kwargs) -> Any:
        """
        (fac:float) -> None.
        Set the wall servo gain relaxation factor.
        """
        pass
    
    def servo_set_gainupdate(self, *args, **kwargs) -> Any:
        """
        (i:int) -> None.
        Set the wall servo gain update interval.
        """
        pass
    
    def servo_set_vmax(self, *args, **kwargs) -> Any:
        """
        (vmax:float) -> None.
        Set the wall servo cap velocity.
        """
        pass
    
    def servo_vmax(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the wall servo cap velocity.
        """
        pass
    
    def set_cutoff(self, *args, **kwargs) -> Any:
        """
        (angle: float) -> None.
        Set the cutoff angle.
        The cutoff angle is used during contact resolution to determine whether or not contact state information is propagated.
        """
        pass
    
    def set_disp(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the wall displacement (vector).
        """
        pass
    
    def set_disp_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the wall displacement.
        """
        pass
    
    def set_disp_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the wall displacement.
        """
        pass
    
    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the wall extra data in the given slot.
        """
        pass
    
    def set_force_contact(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the wall contact force (vector).
        """
        pass
    
    def set_force_contact_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the wall contact force.
        """
        pass
    
    def set_force_contact_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the wall contact force.
        """
        pass
    
    def set_fragment(self, *args, **kwargs) -> Any:
        """
        (id: int) -> None.
        Set wall fragment ID.
        """
        pass
    
    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the wall group name in a given slot.
        """
        pass
    
    def set_moment_contact(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the wall contact moment.
        """
        pass
    
    def set_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the wall location (vector).
        """
        pass
    
    def set_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the wall location.
        """
        pass
    
    def set_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the wall location.
        """
        pass
    
    def set_prop(self, *args, **kwargs) -> Any:
        """
        (name: str, value: any) -> None.
        Set a property of all facets.
        Properties are name-value pairs that are used to fill contact model properties.
        """
        pass
    
    def set_rotation(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the wall orientation.
        """
        pass
    
    def set_rotation_center(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the wall center of rotation (vector).
        """
        pass
    
    def set_rotation_center_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the wall center of rotation.
        """
        pass
    
    def set_rotation_center_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the wall center of rotation.
        """
        pass
    
    def set_spin(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the wall angular velocity.
        """
        pass
    
    def set_vel(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the wall velocity (vector).
        """
        pass
    
    def set_vel_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the wall velocity.
        """
        pass
    
    def set_vel_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the wall velocity.
        """
        pass
    
    def spin(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the wall angular velocity.
        """
        pass
    
    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this wall is live.
        """
        pass
    
    def vel(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the wall velocity (vector).
        """
        pass
    
    def vel_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the wall velocity.
        """
        pass
    
    def vel_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the wall velocity.
        """
        pass
    
    def vertices(self, *args, **kwargs) -> Any:
        """
        () -> Vertex iterator object.
        Get the vertices of this wall.
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
    

class WallIter:
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
    

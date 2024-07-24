from typing import Any, Tuple


def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid fracture objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of fractures.
    """
    pass


def find(*args, **kwargs) -> Any:
    """
    (id: int) -> Fracture object.
    Get the fracture object with the given ID number.
    """
    pass


def inbox(*args, **kwargs) -> Any:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of fracture objects.
    Get a tuple of fractures with extents intersecting a box.
    The extent is the axis-aligned bounding box of the fracture.
    The if the optional keyword argument intersect is False only fractures falling entirely within the box are returned.
    All fractures are searched.
    """
    pass


def list(*args, **kwargs) -> Any:
    """
    () -> Fracture iterator object.
    Get a Fracture iterator object.
    """
    pass


def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum fracture ID.
    """
    pass


def near(*args, **kwargs) -> Any:
    """
    (point: vec, radius=0.0) -> Fracture object.
    Find the closest fracture to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    All fractures are searched.
    """
    pass


class Fracture:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def aperture(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the fracture aperture.
        """
        pass

    def contact_count(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this fracture.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The optional type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the optional keyword argument all is True the count includes virtual contacts.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> tuple of Contact objects.Get a tuple of contacts associated with this fracture.
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass

    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete this fracture.
        """
        pass

    def dfn(self, *args, **kwargs) -> Any:
        """
        () -> DFN object.
        Get the dfn to which this fracture belongs.
        """
        pass

    def dip(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the fracture dip.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the fracture extra data in the given slot.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the fracture group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the fracture.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this fracture is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Returns True if the fracture has the given surface property.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the fracture id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the fracture is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def intersections(self, *args, **kwargs) -> Any:
        """
        (DFN object) -> tuple of Intersection objects.
        Get the intersections with this fracture.
        An optional DFN object can be specified to limit the intersections to fractures belonging to that dfn.
        """
        pass

    def intersects(self, *args, **kwargs) -> Any:
        """
        (Fracture object) -> bool.
        Get a boolean indicating the intersection status of the given fracture with this fracture.
        """
        pass

    def len(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the fracture length.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the fracture normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the fracture normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the fracture normal.
        """
        pass

    def point_near(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Get the point on the fracture closest to the given point (vector).
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the fracture location (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the fracture location.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the fracture location.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this fracture.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this fracture.
        """
        pass

    def set_aperture(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the fracture aperture.
        """
        pass

    def set_dip(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the fracture dip.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the fracture extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the fracture group name in a given slot.
        """
        pass

    def set_len(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the fracture length.
        """
        pass

    def set_normal(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the fracture normal (vector).
        """
        pass

    def set_normal_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the fracture normal.
        """
        pass

    def set_normal_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the fracture normal.
        """
        pass

    def set_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the fracture location (vector).
        """
        pass

    def set_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the fracture location.
        """
        pass

    def set_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the fracture location.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this fracture.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this fracture is live.
        """
        pass

    def vertices(self, *args, **kwargs) -> Any:
        """
        () -> tuple of Vertex objects.
        Get the vertices of this fracture.
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


class FractureIter:
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

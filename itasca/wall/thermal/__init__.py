import typing
from typing import Any

import vec

import itasca.wall.thermal
from . import facet


def _plist() -> typing.Tuple[itasca.wall.thermal.ThermalWall, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid thermal Wall objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count() -> int:
    """
    () -> int.
    Get the number of thermal walls.
    """
    pass


def find(id: int) -> itasca.wall.thermal.ThermalWall:
    """
    (id: int) -> Thermal wall object.
    Get the thermal wall object with the given ID number.
    """
    pass


def inbox(lower_bound: vec.vec, upper_bound: vec.vec, intersect=...) -> typing.Tuple[
    itasca.wall.thermal.ThermalWall, ...]:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of thermal wall objects.
    Get a tuple of thermal walls with extents intersecting a box.
    The extent is the axis-aligned bounding box of the thermal wall.
    The if the optional keyword argument intersect is False then only thermal walls with positions falling in the box are returned.
    """
    pass


def list() -> itasca.wall.thermal.ThermalWallIter:
    """
    () -> Thermal wall iterator object.
    Get a thermal wall iterator object.
    """
    pass


def maxid() -> int:
    """
    () -> int.
    Get the maximum thermal wall ID.
    """
    pass


def near(point: vec.vec, radius=...) -> itasca.wall.thermal.ThermalWall:
    """
    (point: vec, radius=0.0) -> Thermal wall object.
    Find the closest wall to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass


class ThermalWall:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def contact_count(self, all=..., type=...) -> int:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this thermal wall.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The optional type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the optional keyword argument all is True the count includes virtual contacts.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this wall.
        An optional argument can be included which is a piece object (a thermal ball, a thermal pebble or a thermal facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the thermal wall extra data in the given slot.
        """
        pass

    def facets(self) -> itasca.wall.thermal.ThermalFacetIter:
        """
        () -> Thermal facet iterator object.
        Get the thermal facets of this thermal wall.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the thermal wall group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> int:
        """
        (group_name: str or int[, slot: str or int]) -> int.
        Remove from the given group from the thermal wall.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this thermal wall.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the thermal wall id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the thermal wall is part of a given group.
        All group slots are searched.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the thermal wall location (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the thermal wall location.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the thermal wall location.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the thermal wall extra data in the given slot.
        """
        pass

    def set_group(self, group_name: typing.Union[str, int] = ..., slot: typing.Union[str, int] = ...) -> None:
        """
        ([group_name:  str or int[, slot: str or int]]) -> None.
        Set the thermal wall group name in a given slot.
        """
        pass

    def set_pos(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the thermal wall location (vector).
        """
        pass

    def set_pos_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the thermal wall location.
        """
        pass

    def set_pos_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the thermal wall location.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of all thermal facets.
        """
        pass

    def set_temp(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal wall facet temperatures of this wall.
        """
        pass

    def valid(self) -> bool:
        """
        () -> bool.
        Returns True if this thermal wall is live.
        """
        pass

    def wall(self) -> itasca.wall.Wall:
        """
        () -> Wall object.
        Get the wall corresponding to this thermal wall.
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


class ThermalWallIter:
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

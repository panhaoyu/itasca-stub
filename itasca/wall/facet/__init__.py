import typing
from typing import Any

import vec

import itasca.wall.facet


def _plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count() -> int:
    """
    () -> int.
    Get the number of facets.
    """
    pass


def find(id: int) -> itasca.wall.facet.Facet:
    """
    (id: int) -> Facet object.
    Get the facet object with the given ID number.
    """
    pass


def inbox(lower_bound: vec.vec, upper_bound: vec.vec, boundary=...) -> typing.Tuple[itasca.wall.facet.Facet, ...]:
    """
    (lower_bound: vec, upper_bound: vec, boundary=False) -> tuple of Facet objects.
    Get facets with extents intersecting a box.
    If the optional keyword argument boundary is True only return the facets inside the extent.
    """
    pass


def list() -> itasca.wall.facet.FacetIter:
    """
    () -> Facet Iterator object.
    Get a wall_facet iterator object.
    """
    pass


def maxid() -> int:
    """
    () -> int.
    Get the maximum facet ID.
    """
    pass


def near(point: vec.vec) -> itasca.wall.facet.Facet:
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

    def active(self) -> int:
        """
        () -> int.
        Get the facet activity code.
        The following codes apply: 0 - both sides are active; 1 - the top side (e.g., in the direction of the facet normal) is active; -1 - the bottom side of the facet is active; or 2 - neither side of the facet is active.
        """
        pass

    def contact_count(self, all=..., type=...) -> int:
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

    def conveyor(self) -> vec.vec:
        """
        () -> vec.
        Get the facet conveyor velocity (vector).
        """
        pass

    def conveyor_x(self) -> float:
        """
        () -> float.
        Get the x-component of the facet conveyor velocity.
        """
        pass

    def conveyor_y(self) -> float:
        """
        () -> float.
        Get the y-component of the facet conveyor velocity.
        """
        pass

    def delete(self) -> None:
        """
        () -> None.
        Delete a facet.
        The wall position is automatically updated.
        """
        pass

    def edge_neighbors(self) -> typing.Tuple[itasca.wall.facet.Facet, ...]:
        """
        () -> tuple of Facet objects.
        Get the neighboring facets.
        Neighboring facets are those sharing a {vertex in 2D; edge in 3D}.
        The tuple is length 3 in 3D and length 2 in 2D.
        Each position in the tuple contains either a Facet object or None if no facet is adjacent to that edge (point in 2d).
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the facet extra data in the given slot.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the facet group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the facet.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this facet is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Returns True if the facet has the given surface property.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the facet id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the facet is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the facet normal direction (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the facet normal direction.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the facet normal direction.
        """
        pass

    def point_near(self, point: vec.vec) -> vec.vec:
        """
        (point: vec) -> vec.
        Get the closest point on the facet to another point.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the facet location (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the facet location.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the facet location.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this facet.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this facet.
        """
        pass

    def set_active(self, activity_code: int) -> None:
        """
        (activity_code: int) -> None.
        The following codes apply: 0 - both sides are active; 1 - the top side (e.g., in the direction of the facet normal) is active; -1 - the bottom side of the facet is active; or 2 - neither side of the facet is active.
        """
        pass

    def set_conveyor(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the facet conveyor velocity (vector).
        """
        pass

    def set_conveyor_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the facet conveyor velocity.
        """
        pass

    def set_conveyor_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the facet conveyor velocity.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the facet extra data in the given slot.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the facet group name in a given slot.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this facet.
        """
        pass

    def valid(self) -> bool:
        """
        () -> bool.
        Returns True if this facet is live.
        """
        pass

    def vertices(self) -> typing.Tuple[itasca.wall.WallVertex, ...]:
        """
        () -> tuple of WallVertex objects.
        Get the facet vertices.
        """
        pass

    def wall(self) -> itasca.wall.Wall:
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

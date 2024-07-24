import typing
from typing import Any

import vec

import itasca.clump.pebble
import itasca.rblock.template


def _plist() -> typing.Tuple[itasca.clump.Clump, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid Clump objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count() -> int:
    """
    () -> int.
    Get the number of pebbles.
    """
    pass


def find(id: int) -> itasca.clump.pebble.Pebble:
    """
    (id: int) -> Pebble object.
    Get the Pebble object with the given ID number.
    """
    pass


def inbox(lower_bound: vec.vec, upper_bound: vec.vec, intersect=...) -> typing.Tuple[itasca.clump.pebble.Pebble, ...]:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of Pebble objects.
    Get a tuple of pebbles with extents intersecting a box.
    The extent is the axis-aligned bounding box of the pebble.
    The if the optional keyword argument intersect is False only pebbles with positions falling in the box are returned.
    """
    pass


def list() -> itasca.clump.pebble.PebbleIter:
    """
    () -> Pebble iterator object.
    Get a pebble iterator object.
    """
    pass


def maxid() -> int:
    """
    () -> int.
    Get the maximum pebble ID.
    """
    pass


def near(point: vec.vec, radius=...) -> itasca.clump.pebble.Pebble:
    """
    (point: vec, radius=0.0) -> Pebble object.
    Find the closest pebble to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass


class Pebble:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def clump(self) -> itasca.clump.Clump:
        """
        () -> Clump object.
        Get the clump object to which this pebble belongs.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece: object], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this ball.
        An optional argument can be included which is a piece object (a Ball, a Pebble or a Facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass

    def delete(self) -> None:
        """
        () -> None.
        Delete this pebble.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the pebble extra data in the given slot.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the pebble group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the pebble.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this pebble is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Returns True if the pebble has the given surface property.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the pebble id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the pebble is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the pebble location (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the pebble location.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the pebble location.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this pebble.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this pebble.
        """
        pass

    def radius(self) -> float:
        """
        () -> float.
        Get the pebble radius.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the pebble extra data in the given slot.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the pebble group name in a given slot.
        """
        pass

    def set_pos(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the pebble location.
        (vector).
        """
        pass

    def set_pos_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the pebble location.
        """
        pass

    def set_pos_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the pebble location.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this pebble.
        """
        pass

    def set_radius(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the pebble radius.
        """
        pass

    def template(self) -> typing.Union[itasca.rblock.template.Template, itasca.clump.template.Template]:
        """
        () -> Template object.
        Get the clump template this pebble belongs to.
        """
        pass

    def valid(self) -> bool:
        """
        () -> bool.
        Returns True if this pebble is live.
        """
        pass

    def vel(self) -> vec.vec:
        """
        () -> vec.
        Get the pebble velocity (vector).
        """
        pass

    def vel_x(self) -> float:
        """
        () -> float.
        Get the x-component of the pebble velocity.
        """
        pass

    def vel_y(self) -> float:
        """
        () -> float.
        Get the y-component of the pebble velocity.
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


class PebbleIter:
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

import typing
from typing import Any

import vec

import itasca.clump.thermal
from . import pebble


def _plist() -> typing.Tuple[itasca.clump.thermal.ThermalClump, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid thermal clump objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count() -> int:
    """
    () -> int.
    Get the number of thermal clumps.
    """
    pass


def find(id: int) -> itasca.clump.thermal.ThermalClump:
    """
    (id: int) -> Thermal clump object.
    Get the thermal clump object with the given ID number.
    """
    pass


def inbox(lower_bound: vec.vec, upper_bound: vec.vec, intersect=...) -> typing.Tuple[
    itasca.clump.thermal.ThermalClump, ...]:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of thermal clump objects.
    Get a tuple of thermal clumps with extents intersecting a box.
    The extent is the axis-aligned bounding box of the clump.
    The if the optional keyword argument intersect is False then only thermal clumps with positions falling in the box are returned.
    """
    pass


def list() -> itasca.clump.thermal.ThermalClumpIter:
    """
    () -> Thermal clump iterator object.
    Get a thermal clump iterator object.
    """
    pass


def maxid() -> int:
    """
    () -> int.
    Get the thermal maximum clump ID.
    """
    pass


def near(point: vec.vec, radius=...) -> itasca.clump.thermal.ThermalClump:
    """
    (point: vec, radius=0.0) -> Thermal clump object.
    Find the closest thermal clump to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass


class ThermalClump:
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
        Get the clump corresponding to this thermal clump.
        """
        pass

    def contact_count(self, all=..., type=...) -> int:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this thermal clump.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The optional type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the optional keyword argument all is True the count includes virtual contacts.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this clump.
        An optional argument can be included which is a piece object (a thermal ball, a thermal pebble or a thermal facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass

    def del_temp(self) -> float:
        """
        () -> float.
        Get the thermal clump temperature increment.
        """
        pass

    def expansion(self) -> float:
        """
        () -> float.
        Get the thermal clump expansion coefficient.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the thermal clump extra data in the given slot.
        """
        pass

    def fix(self) -> bool:
        """
        () -> bool.
        Get the thermal clump fixity.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the thermal clump group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> int:
        """
        (group_name: str or int[, slot: str or int]) -> int.
        Remove from the given group from the thermal clump.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this thermal clump.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the thermal clump id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the thermal clump is part of a given group.
        All group slots are searched.
        """
        pass

    def pebbles(self) -> itasca.clump.thermal.ThermalPebbleIter:
        """
        () -> Thermal pebble iterator object.
        Get the thermal pebbles of this thermal clump.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the thermal clump location (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the thermal clump location.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the thermal clump location.
        """
        pass

    def power_app(self) -> float:
        """
        () -> float.
        Get the thermal clump applied power.
        """
        pass

    def power_unbal(self) -> float:
        """
        () -> float.
        Get the thermal clump unbalanced power.
        """
        pass

    def set_del_temp(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal clump temperature increment.
        """
        pass

    def set_expansion(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal clump expansion coefficient.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the thermal clump extra data in the given slot.
        """
        pass

    def set_fix(self, value: bool) -> None:
        """
        (value: bool) -> None.
        Set the thermal clump fixity.
        """
        pass

    def set_group(self, group_name: typing.Union[str, int] = ..., slot: typing.Union[str, int] = ...) -> None:
        """
        ([group_name:  str or int[, slot: str or int]]) -> None.
        Set the thermal clump group name in a given slot.
        """
        pass

    def set_pos(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the thermal clump location (vector).
        """
        pass

    def set_pos_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the thermal clump location.
        """
        pass

    def set_pos_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the thermal clump location.
        """
        pass

    def set_power_app(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal clump applied power.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of all thermal pebbles.
        """
        pass

    def set_specific_heat(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal clump specific heat.
        """
        pass

    def set_temp(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal clump temperature.
        """
        pass

    def specific_heat(self) -> float:
        """
        () -> float.
        Get the thermal clump specific heat.
        """
        pass

    def temp(self) -> float:
        """
        () -> float.
        Get the thermal clump temperature.
        """
        pass

    def valid(self) -> bool:
        """
        () -> bool.
        Returns True if this thermal clump is live.
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


class ThermalClumpIter:
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

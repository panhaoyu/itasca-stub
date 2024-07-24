import typing
from typing import Any

import vec

import itasca.ball.thermal


def _plist() -> typing.Tuple[itasca.ball.thermal.ThermalBall, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid thermal ball objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count() -> int:
    """
    () -> int.
    Get the number of thermal balls.
    """
    pass


def find(id: int) -> itasca.ball.thermal.ThermalBall:
    """
    (id: int) -> Thermal ball object.
    Get the ball thermal object with the given ID number.
    """
    pass


def inbox(lower_bound: vec.vec, upper_bound: vec.vec, intersect=...) -> typing.Tuple[
    itasca.ball.thermal.ThermalBall, ...]:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of thermal ball objects.
    Get a tuple of thermal balls with extents intersecting a box.
    The extent is the axis-aligned bounding box of the thermal ball.
    The if the optional keyword argument intersect is False then only balls with positions falling in the box are returned.
    """
    pass


def list() -> itasca.ball.thermal.ThermalBallIter:
    """
    () -> Thermal ball iterator object.
    Get a ball thermal iterator object.
    """
    pass


def maxid() -> int:
    """
    () -> int.
    Get the maximum thermal ball ID.
    """
    pass


def near(point: vec.vec, radius=...) -> itasca.ball.thermal.ThermalBall:
    """
    (point: vec, radius=0.0) -> Thermal ball object.
    Find the closest thermal ball to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass


class ThermalBall:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def ball(self) -> itasca.ball.Ball:
        """
        () -> Ball object.
        Get the ball corresponding to this thermal ball.
        """
        pass

    def contact_count(self, all=..., type=...) -> int:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this thermal ball.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The optional type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the optional keyword argument all is True the count includes virtual contacts.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this thermal ball.
        An optional argument can be included which is a piece object (a thermal ball, a thermal pebble or a thermal facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallThermalContact, itasca.BallPebbleThermalContact, itasca.PebblePebbleThermalContact, itasca.BallFacetThermalContact or itasca.PebbleFacetThermalContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass

    def del_temp(self) -> float:
        """
        () -> float.
        Get the thermal ball temperature increment.
        """
        pass

    def expansion(self) -> float:
        """
        () -> float.
        Get the thermal ball expansion coefficient.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the thermal ball extra data in the given slot.
        """
        pass

    def fix(self) -> bool:
        """
        () -> bool.
        Get the thermal ball fixity.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the thermal ball group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> int:
        """
        (group_name: str or int[, slot: str or int]) -> int.
        Remove from the given group from the thermal ball.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this thermal ball.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Returns True if the thermal ball has the given surface property.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the thermal ball id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the thermal ball is part of a given group.
        All group slots are searched.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the thermal ball location (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the thermal ball location.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the thermal ball location.
        """
        pass

    def power_app(self) -> float:
        """
        () -> float.
        Get the thermal ball applied power.
        """
        pass

    def power_unbal(self) -> float:
        """
        () -> float.
        Get the thermal ball unbalanced power.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this thermal ball.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this thermal ball.
        """
        pass

    def set_del_temp(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal ball temperature increment.
        """
        pass

    def set_expansion(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal ball expansion coefficient.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the thermal ball extra data in the given slot.
        """
        pass

    def set_fix(self, value: bool) -> None:
        """
        (value: bool) -> None.
        Set the thermal ball fixity.
        """
        pass

    def set_group(self, group_name: typing.Union[str, int] = ..., slot: typing.Union[str, int] = ...) -> None:
        """
        ([group_name:  str or int[, slot: str or int]]) -> None.
        Set the thermal ball group name in a given slot.
        """
        pass

    def set_pos(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the thermal ball location (vector).
        """
        pass

    def set_pos_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the thermal ball location.
        """
        pass

    def set_pos_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the thermal ball location.
        """
        pass

    def set_power_app(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal ball applied power.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this thermal ball.
        """
        pass

    def set_specific_heat(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal ball specific heat.
        """
        pass

    def set_temp(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the thermal ball temperature.
        """
        pass

    def specific_heat(self) -> float:
        """
        () -> float.
        Get the thermal ball specific heat.
        """
        pass

    def temp(self) -> float:
        """
        () -> float.
        Get the thermal ball temperature.
        """
        pass

    def valid(self) -> bool:
        """
        () -> bool.
        Returns True if this thermal ball is live.
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


class ThermalBallIter:
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

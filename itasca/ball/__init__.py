from typing import Any, Tuple, Iterator

from . import thermal


def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid Ball objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count() -> int:
    """
    Get the number of balls.
    """
    pass


def create(*args, **kwargs) -> 'Ball':
    """
    (radius: double, centroid: vec [,id: int]) -> Ball object.
    Create a ball.
    """
    pass


def energy(energy_name: str) -> float:
    """
    Get the ball total energy contribution.
    """
    pass


def find(id: int) -> 'Ball':
    """
    Get the ball object with the given ID number.
    """
    pass


def inbox(*args, **kwargs) -> Tuple['Ball']:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of ball objects.
    Get a tuple of balls with extents intersecting a box.
    The extent is the axis-aligned bounding box of the ball.
    The if the optional keyword argument intersect is False then only balls with positions falling in the box are returned.
    """
    pass


def list() -> Iterator['Ball']:
    """
    Get a ball iterator object.
    """
    pass


def maxid() -> int:
    """
    Get the maximum ball ID.
    """
    pass


def near(*args, **kwargs) -> 'Ball':
    """
    (point: vec, radius=0.0) -> Ball object.
    Find the closest ball to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass


class Ball:
    def __init__(self) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def contact_count(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this ball.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The optional type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the optional keyword argument all is True the count includes virtual contacts.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece: ball], all=False, type=None) -> tuple of Contact objects.
        Get a tuple of contacts associated with this ball.
        An optional argument can be included which is a piece object (a Ball, a Pebble or a Facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        """
        pass

    def damp(self) -> float:
        """
        Get the ball local damping.
        """
        pass

    def delete(self) -> None:
        """
        Delete this ball.
        """
        pass

    def density(self) -> float:
        """
        Get the ball density.
        """
        pass

    def disp(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the ball displacement (vector).
        """
        pass

    def disp_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the ball displacement.
        """
        pass

    def disp_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the ball displacement.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the ball extra data in the given slot.
        """
        pass

    def fix(self, *args, **kwargs) -> Any:
        """
        (component: int) -> bool.
        Get the ball fixity condition.
        The first argument is the vector component.
        """
        pass

    def force_app(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the ball applied force (vector).
        """
        pass

    def force_app_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the ball applied force.
        """
        pass

    def force_app_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the ball applied force.
        """
        pass

    def force_contact(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the ball contact force (vector).
        """
        pass

    def force_contact_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the ball contact force.
        """
        pass

    def force_contact_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the ball contact force.
        """
        pass

    def force_unbal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the ball unbalanced force (vector).
        """
        pass

    def force_unbal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the ball unbalanced force.
        """
        pass

    def force_unbal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the ball unbalanced force.
        """
        pass

    def fragment(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the ball fragment ID.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the ball group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the ball.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this ball is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Returns True if the ball has the given surface property.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the ball id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the ball is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def mass(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball inertial mass.
        """
        pass

    def mass_real(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball real (gravitational) mass.
        """
        pass

    def moi(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball moment of inertia.
        """
        pass

    def moi_real(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball real (gravitational) moment of inertia.
        """
        pass

    def moment_app(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball applied moment.
        """
        pass

    def moment_contact(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball contact moment.
        """
        pass

    def moment_unbal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball unbalanced moment.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the ball centroid location (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the ball centroid location.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the ball centroid location.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this ball.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this ball.
        """
        pass

    def radius(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball radius.
        """
        pass

    def rotation(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball orientation.
        """
        pass

    def set_damp(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the ball local damping.
        """
        pass

    def set_density(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the ball density.
        """
        pass

    def set_disp(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the ball displacement (vector).
        """
        pass

    def set_disp_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the ball displacement.
        """
        pass

    def set_disp_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the ball displacement.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the ball extra data in the given slot.
        """
        pass

    def set_fix(self, *args, **kwargs) -> Any:
        """
        (component: int, fix: bool) -> None.
        Set the ball fixity condition.
        The first argument is the vector component to set and the second components is a the fixity flag.
        """
        pass

    def set_force_app(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the ball applied force (vector).
        """
        pass

    def set_force_app_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the ball applied force.
        """
        pass

    def set_force_app_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the ball applied force.
        """
        pass

    def set_force_contact(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the ball contact force (vector).
        """
        pass

    def set_force_contact_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the ball contact force.
        """
        pass

    def set_force_contact_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the ball contact force.
        """
        pass

    def set_fragment(self, *args, **kwargs) -> Any:
        """
        (id: int) -> None.
        Set ball fragment ID.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the ball group name in a given slot.
        """
        pass

    def set_moment_app(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the ball applied moment.
        """
        pass

    def set_moment_contact(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the ball contact moment.
        """
        pass

    def set_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the ball centroid location (vector).
        """
        pass

    def set_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the ball centroid location.
        """
        pass

    def set_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the ball centroid location.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this ball.
        """
        pass

    def set_radius(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the ball radius.
        """
        pass

    def set_rotation(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the ball orientation.
        """
        pass

    def set_spin(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the ball angular velocity.
        """
        pass

    def set_vel(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the ball velocity (vector).
        """
        pass

    def set_vel_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the ball velocity.
        """
        pass

    def set_vel_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the ball velocity.
        """
        pass

    def spin(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the ball angular velocity.
        """
        pass

    def stress(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the stress tensor arising from all contacts acting on the ball.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this ball is live.
        """
        pass

    def vel(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the ball velocity (vector).
        """
        pass

    def vel_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the ball velocity.
        """
        pass

    def vel_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the ball velocity.
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


class BallIter:
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

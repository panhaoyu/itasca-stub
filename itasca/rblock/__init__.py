import typing
from typing import Any

import vec

import itasca.rblock
from . import template


def _plist() -> typing.Tuple[itasca.rblock.RBlock, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid RBlock objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def containing(point: vec.vec) -> itasca.rblock.RBlock:
    """
    (point: vec) -> RBlock object.
    Find the rigid block containing the point.
    The core shapes are used to determine if the point falls within the rigid block.
    """
    pass


def count() -> int:
    """
    () -> int.
    Get the number of rblocks.
    """
    pass


def energies() -> typing.Dict[str, float]:
    """
    () -> dict {str: float}.
    Get the rblock total energy contribution as a dictionary with string keys and float values.
    """
    pass


def energy(energy_name: str) -> float:
    """
    (energy_name: str) -> float.
    Get the rblock total energy contribution.
    This is the sum over all rblocks of the energy with name energy_na,e (see the set energy command).
    Available energies are: "energy-body", "energy-damp" and "energy-kinetic".
    """
    pass


def find(id: int) -> itasca.rblock.RBlock:
    """
    (id: int) -> RBlock object.
    Get the RBlock object with the given ID number.
    """
    pass


def inbox(lower_bound: vec.vec, upper_bound: vec.vec, intersect=...) -> typing.Tuple[itasca.rblock.RBlock, ...]:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of RBlock objects.
    Get a tuple of rblocks with extents intersecting a box.
    The extent is the axis-aligned bounding box of the rblock.
    The if the optional keyword argument intersect is False only rblocks with positions falling in the box are returned.
    """
    pass


def list() -> itasca.rblock.RBlockIter:
    """
    () -> RBlock object iterator.
    Get a rblock iterator object.
    """
    pass


def maxid() -> int:
    """
    () -> int.
    Get the maximum rblock ID.
    """
    pass


def near(point: vec.vec, radius=...) -> itasca.rblock.RBlock:
    """
    (point: vec, radius=0.0) -> RBlock object.
    Find the closest rblock to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass


class RBlock:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def aspect_ratio(self) -> float:
        """
        () -> float.
        Get the rblock aspect ratio..
        """
        pass

    def ball_pos(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock ball radius (vector).
        """
        pass

    def ball_pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock ball radius.
        """
        pass

    def ball_pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock ball radius.
        """
        pass

    def ball_radius(self) -> float:
        """
        () -> float.
        Get the rblock ball radius..
        """
        pass

    def collide(self, object) -> bool:
        """
        (object: rblock) -> bool.
        Get the intersection status of two rigid blocks.
        """
        pass

    def contact_count(self, all=..., type=...) -> int:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this rblock.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the count includes virtual contacts.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece: object], all=False, type=None) -> Tuple of Contact objects.
        Get a tuple of contacts associated with this rblock.
        An optional argument can be included which is a piece object (a Ball, a Pebble, an RBlock or a Facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        .
        """
        pass

    def damp(self) -> float:
        """
        () -> float.
        Get the rblock local damping.
        """
        pass

    def delete(self) -> None:
        """
        () -> None.
        Delete this rblock.
        """
        pass

    def density(self) -> float:
        """
        () -> float.
        Get the rblock density.
        """
        pass

    def disp(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock displacement (vector).
        """
        pass

    def disp_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock displacement.
        """
        pass

    def disp_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock displacement.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the rblock extra data in the given slot.
        """
        pass

    def fix(self, component: int) -> bool:
        """
        (component: int) -> bool.
        Get the rblock fixity condition.
        The integer degree-of-freedom cooresponds to the following order: in 3D: 0) x-velocity, 1) y-velocity, 2) z-velocity, 3) x-angular velocity, 4) y-angular velocity, 5) z-angular velocity.
        in 2D: 0) x-velocity, 1) y-velocity, 2) angular velocity.
        The return value is false for free and true for fixed conditions.
        """
        pass

    def force_app(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock applied force (vector).
        """
        pass

    def force_app_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock applied force.
        """
        pass

    def force_app_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock applied force.
        """
        pass

    def force_contact(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock contact force (vector).
        """
        pass

    def force_contact_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock contact force.
        """
        pass

    def force_contact_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock contact force.
        """
        pass

    def force_unbal(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock unbalanced force (vector).
        """
        pass

    def force_unbal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock unbalanced force.
        """
        pass

    def force_unbal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock unbalanced force.
        """
        pass

    def fragment(self) -> int:
        """
        () -> int.
        Get the rblock fragment ID.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the rblock group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the rblock.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this rblock is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Returns True if the rblock has the given surface property.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the rblock id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the rblock is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inside(self, point: vec.vec) -> bool:
        """
        (point: vec) -> bool.
        Test whether a point is inside a rblock.
        """
        pass

    def mass(self) -> float:
        """
        () -> float.
        Get the rblock inertial mass.
        """
        pass

    def mass_real(self) -> float:
        """
        () -> float.
        Get the rblock real (gravitational) mass.
        """
        pass

    def moi(self) -> vec.tens3:
        """
        () -> tensor.
        Get the rblock moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        """
        pass

    def moi_fix(self) -> bool:
        """
        () -> bool.
        Get the moment of intertia fixity state.
        When activated, the rblock moment of inertia will not be automatically updated when a rblock is scaled, the volume is changed, or when the density is changed.
        This is activated automatically when either the volume or moment of inertia is set manually via the rblock attribute command or via the RBlock object methods vol(), moi_real() or moi_prinreal().
        """
        pass

    def moi_prin_real(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock real principal moment of inertia.
        When modified no other rblock attributes are changed.
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method) (vector).
        """
        pass

    def moi_prin_real_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock real principal moment of inertia.
        When modified no other rblock attributes are changed.
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method).
        """
        pass

    def moi_prin_real_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock real principal moment of inertia.
        When modified no other rblock attributes are changed.
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method).
        """
        pass

    def moi_real(self) -> vec.tens3:
        """
        () -> tensor.
        Get the rblock real moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        """
        pass

    def moment_app(self) -> float:
        """
        () -> float.
        Get the rblock applied moment.
        """
        pass

    def moment_contact(self) -> float:
        """
        () -> float.
        Get the rblock contact moment.
        """
        pass

    def moment_unbal(self) -> float:
        """
        () -> float.
        Get the rblock unbalanced moment.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock centroid location (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock centroid location.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock centroid location.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a surface property value of this rblock.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get a dictionary of all the surface properties of this rblock.
        """
        pass

    def rotate(self, axis: vec.vec, rotation_angle: float) -> None:
        """
        (axis: vec, rotation_angle: float) -> None.
        Rotate a rblock.
        The rotation point is the rblock position and it is rotated in a right handed sense about the given axis by rotation_angle degrees.
        """
        pass

    def rotation(self) -> float:
        """
        () -> float.
        Get the rblock orientation.
        """
        pass

    def rounding(self) -> float:
        """
        () -> float.
        Get the rblock rounding..
        """
        pass

    def scale_sphere(self, diameter: float) -> None:
        """
        (diameter: float) -> None.
        Scale the rblock to an equivalent sphere.
        The rblock is scaled so that its {area in 2D; volume in 3D} is the same as a {circle in 2D; sphere in 3D} of the given diameter.
        If the volume or moment of inertia has been previously specified by the user either via rblock attribute or via the RBlock object methods (vol(), moi_prin_real() or moi_real()), the principal moment of inertial is in a fixed state and will not be scaled.
        See the Cump object moi_fix() method for further details.
        """
        pass

    def scale_vol(self, volume: float) -> None:
        """
        (volume: float) -> None.
        Scale the rblock.
        The rblock is scaled so that its {volume per unit thickness in 2D; volume in 3D} is as specified.
        If the volume or moment of inertia has been previously specified by the user either via rblock attribute or via the RBlock object methods (vol(), moi_prin_real() or moi_real()), the principal moment of inertial is in a fixed state and will not be scaled.
        See the Cump object moi_fix() method for further details.
        """
        pass

    def set_damp(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the rblock local damping.
        """
        pass

    def set_density(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the rblock density.
        """
        pass

    def set_disp(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the rblock displacement (vector).
        """
        pass

    def set_disp_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the rblock displacement.
        """
        pass

    def set_disp_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the rblock displacement.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the rblock extra data in the given slot.
        """
        pass

    def set_fix(self, component: int, fixity: bool) -> None:
        """
        (component: int, fixity: bool) -> None.
        Get the rblock fixity condition.
        The integer degree-of-freedom cooresponds to the following order: in 3D: 1) x-velocity, 2) y-velocity, 3) z-velocity, 4) x-angular velocity, 5) y-angular velocity, 6) z-angular velocity.
        in 2D: 1) x-velocity, 2) y-velocity, 3) angular velocity.
        The fixity value is false for free and true for fixed conditions.
        """
        pass

    def set_force_app(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the rblock applied force (vector).
        """
        pass

    def set_force_app_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the rblock applied force.
        """
        pass

    def set_force_app_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the rblock applied force.
        """
        pass

    def set_force_contact(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the rblock contact force (vector).
        """
        pass

    def set_force_contact_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the rblock contact force.
        """
        pass

    def set_force_contact_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the rblock contact force.
        """
        pass

    def set_fragment(self, id: int) -> None:
        """
        (id: int) -> None.
        Set rblock fragment ID.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the rblock group name in a given slot.
        """
        pass

    def set_moi_fix(self, fixity: bool) -> None:
        """
        (fixity: bool) -> None.
        Set the moment of intertia fixity state.
          When activated, the rblock moment of inertia will not be automatically updated when a rblock is scaled, the volume is changed, or when the density is changed.
        This is activated automatically when either the volume or moment of inertia is set manually via the rblock attribute command or via the RBlock object methods vol(), moi_real() or moi_prinreal().
        """
        pass

    def set_moi_prin_real(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the rblock real principal moment of inertia.
        When modified no other rblock attributes are changed.
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method) (vector).
        """
        pass

    def set_moi_prin_real_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the rblock real principal moment of inertia.
        When modified no other rblock attributes are changed.
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method).
        """
        pass

    def set_moi_prin_real_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the rblock real principal moment of inertia.
        When modified no other rblock attributes are changed.
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method).
        """
        pass

    def set_moi_real(self) -> vec.tens3:
        """
        () -> tensor.
        Get the rblock real moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        When modified no other rblock attributes are changed.
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method).
        """
        pass

    def set_moment_app(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the rblock applied moment.
        """
        pass

    def set_moment_contact(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the rblock contact moment.
        """
        pass

    def set_pos(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the rblock centroid location (vector).
        """
        pass

    def set_pos_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the rblock centroid location.
        """
        pass

    def set_pos_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the rblock centroid location.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a surface property of this rblock.
        """
        pass

    def set_rotation(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the rblock orientation.
        """
        pass

    def set_spin(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the rblock angular velocity.
        """
        pass

    def set_vel(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the rblock velocity (vector).
        """
        pass

    def set_vel_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the rblock velocity.
        """
        pass

    def set_vel_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the rblock velocity.
        """
        pass

    def set_vol(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the rblock volume.
        In 2D this is the volume per unit thickness.
        """
        pass

    def spin(self) -> float:
        """
        () -> float.
        Get the rblock angular velocity.
        """
        pass

    def stress(self) -> vec.tens3:
        """
        () -> tensor.
        Get the stress tensor arising from all contacts acting on the rblock.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Rotate a vector from principal system.
        The returned vector is in the global axis system.
        """
        pass

    def to_prin(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Rotate a vector to principal system.
        """
        pass

    def valid(self) -> bool:
        """
        () -> bool.
        Returns True if this rblock is live.
        """
        pass

    def vel(self) -> vec.vec:
        """
        () -> vec.
        Get the rblock velocity (vector).
        """
        pass

    def vel_x(self) -> float:
        """
        () -> float.
        Get the x-component of the rblock velocity.
        """
        pass

    def vel_y(self) -> float:
        """
        () -> float.
        Get the y-component of the rblock velocity.
        """
        pass

    def vol(self) -> float:
        """
        () -> float.
        Get the rblock volume.
        In 2D this is the volume per unit thickness.
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


class RBlockIter:
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

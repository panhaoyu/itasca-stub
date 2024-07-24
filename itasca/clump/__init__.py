from typing import Any, Tuple

from . import template
from . import pebble
from . import thermal


def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid Clump objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of clumps.
    """
    pass


def energies(*args, **kwargs) -> Any:
    """
    () -> dict {str: float}.
    Get the clump total energy contribution as a dictionary with string keys and float values.
    """
    pass


def energy(*args, **kwargs) -> Any:
    """
    (energy_name: str) -> float.
    Get the clump total energy contribution.
    This is the sum over all clumps of the energy with name energy_na,e (see the set energy command).
    Available energies are: "energy-body", "energy-damp" and "energy-kinetic".
    """
    pass


def find(*args, **kwargs) -> Any:
    """
    (id: int) -> Clump object.
    Get the Clump object with the given ID number.
    """
    pass


def inbox(*args, **kwargs) -> Any:
    """
    (lower_bound: vec, upper_bound: vec, intersect=True) -> Tuple of Clump objects.
    Get a tuple of clumps with extents intersecting a box.
    The extent is the axis-aligned bounding box of the clump.
    The if the optional keyword argument intersect is False only clumps with positions falling in the box are returned.
    """
    pass


def list(*args, **kwargs) -> Any:
    """
    () -> Clump object iterator.
    Get a clump iterator object.
    """
    pass


def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum clump ID.
    """
    pass


def near(*args, **kwargs) -> Any:
    """
    (point: vec, radius=0.0) -> Clump object.
    Find the closest clump to a point.
    If the optional keyword argument radius is non-zero, only search within this radius.
    """
    pass


class Clump:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def add_pebble(self, *args, **kwargs) -> Any:
        """
        (pebble_radius: float, pebble_centroid: vec [,id: int]) -> Pebble object.
        Add a pebble to a clump.
        This operation has no impact on the clump inertial attributes.
        The clump no longer refers to a clump template.
        The pebble must fall within the model domain.
        """
        pass

    def calculate(self, *args, **kwargs) -> Any:
        """
        (error_percentage=0.01) -> None.
        Calculate the clump interial properties.
        The optional error_percentage argument should be in the range 0.0005 < x < 1.
        The current pebble distribution is used with a voxelation approach to calculate the interial properties within a specified error.
        See the clump template command for further details.
        The pebbles are not translated but the clump centroid location may be modified.
        The moment of inertia will be modified by changes in volume or density after this operation.
        """
        pass

    def contact_count(self, *args, **kwargs) -> Any:
        """
        (all=False, type=None) -> int.
        Get the number of contacts associated with this clump.
        If the optional keyword argument type is given, the count is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the count includes virtual contacts.
        """
        pass

    def contacts(self, *args, **kwargs) -> Any:
        """
        ([piece: object], all=False, type=None) -> Tuple of Contact objects.
        Get a tuple of contacts associated with this clump.
        An optional argument can be included which is a piece object (a Ball, a Pebble or a Facet).
        If the optional keyword argument type is given, the returned list is limited to the contact types specified.
        The type keyword argument should be a Python type object (one of: itasca.BallBallContact, itasca.BallPebbleContact, itasca.PebblePebbleContact, itasca.BallFacetContact or itasca.PebbleFacetContact).
        If the (optional) keyword argument all is True the returned list includes virtual contacts.
        .
        """
        pass

    def damp(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump local damping.
        """
        pass

    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete this clump.
        """
        pass

    def delete_pebble(self, *args, **kwargs) -> Any:
        """
        (pebble: Pebble object) -> None.
        Delete a pebble from this clump.
        This operation has no impact on the clump inertial attributes.
        The clump no longer refers to a clump template.
        """
        pass

    def density(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump density.
        """
        pass

    def disp(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump displacement (vector).
        """
        pass

    def disp_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump displacement.
        """
        pass

    def disp_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump displacement.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the clump extra data in the given slot.
        """
        pass

    def fix(self, *args, **kwargs) -> Any:
        """
        (component: int) -> bool.
        Get the clump fixity condition.
        The integer degree-of-freedom cooresponds to the following order: in 3D: 0) x-velocity, 1) y-velocity, 2) z-velocity, 3) x-angular velocity, 4) y-angular velocity, 5) z-angular velocity.
        in 2D: 0) x-velocity, 1) y-velocity, 2) angular velocity.
        The return value is false for free and true for fixed conditions.
        """
        pass

    def force_app(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump applied force (vector).
        """
        pass

    def force_app_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump applied force.
        """
        pass

    def force_app_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump applied force.
        """
        pass

    def force_contact(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump contact force (vector).
        """
        pass

    def force_contact_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump contact force.
        """
        pass

    def force_contact_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump contact force.
        """
        pass

    def force_unbal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump unbalanced force (vector).
        """
        pass

    def force_unbal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump unbalanced force.
        """
        pass

    def force_unbal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump unbalanced force.
        """
        pass

    def fragment(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the clump fragment ID.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the clump group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the clump.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this clump is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the clump id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the clump is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def mass(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump inertial mass.
        """
        pass

    def mass_real(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump real (gravitational) mass.
        """
        pass

    def moi(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the clump moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        """
        pass

    def moi_fix(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the moment of intertia fixity state.
        When activated, the clump moment of inertia will not be automatically updated when a clump is scaled, the volume is changed, or when the density is changed.
        This is activated automatically when either the volume or moment of inertia is set manually via the clump attribute command or via the Clump object methods vol(), moi_real() or moi_prinreal().
        """
        pass

    def moi_prin_real(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump real principal moment of inertia.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method) (vector).
        """
        pass

    def moi_prin_real_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump real principal moment of inertia.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method).
        """
        pass

    def moi_prin_real_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump real principal moment of inertia.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method).
        """
        pass

    def moi_real(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the clump real moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        """
        pass

    def moment_app(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump applied moment.
        """
        pass

    def moment_contact(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump contact moment.
        """
        pass

    def moment_unbal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump unbalanced moment.
        """
        pass

    def pebbles(self, *args, **kwargs) -> Any:
        """
        () -> Pebble iterator object.
        Get the pebbles of this clump.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump centroid location (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump centroid location.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump centroid location.
        """
        pass

    def rotate(self, *args, **kwargs) -> Any:
        """
        (axis: vec, rotation_angle: float) -> None.
        Rotate a clump.
        The rotation point is the clump position and it is rotated in a right handed sense about the given axis by rotation_angle degrees.
        """
        pass

    def rotation(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump orientation.
        """
        pass

    def scale_sphere(self, *args, **kwargs) -> Any:
        """
        (diameter: float) -> None.
        Scale the clump to an equivalent sphere.
        The clump is scaled so that its {area in 2D; volume in 3D} is the same as a {circle in 2D; sphere in 3D} of the given diameter.
        The pebbles are scaled, their positions are modified and the volume is updated.
        All pebbles of the scaled clump must fall within the model domain for the operation to succeed.
        If the volume or moment of inertia has been previously specified by the user either via clump attribute or via the Clump object methods (vol(), moi_prin_real() or moi_real()), the principal moment of inertial is in a fixed state and will not be scaled.
        See the Cump object moi_fix() method for further details.
        """
        pass

    def scale_vol(self, *args, **kwargs) -> Any:
        """
        (volume: float) -> None.
        Scale the clump.
        The clump is scaled so that its {volume per unit thickness in 2D; volume in 3D} is as specified.
        The pebbles are scaled, their positions are modified and the volume is updated.
        All pebbles of the scaled clump must fall within the model domain for the operation to succeed.
        If the volume or moment of inertia has been previously specified by the user either via clump attribute or via the Clump object methods (vol(), moi_prin_real() or moi_real()), the principal moment of inertial is in a fixed state and will not be scaled.
        See the Cump object moi_fix() method for further details.
        """
        pass

    def set_damp(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump local damping.
        """
        pass

    def set_density(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump density.
        """
        pass

    def set_disp(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump displacement (vector).
        """
        pass

    def set_disp_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump displacement.
        """
        pass

    def set_disp_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump displacement.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the clump extra data in the given slot.
        """
        pass

    def set_fix(self, *args, **kwargs) -> Any:
        """
        (component: int, fixity: bool) -> None.
        Get the clump fixity condition.
        The integer degree-of-freedom cooresponds to the following order: in 3D: 1) x-velocity, 2) y-velocity, 3) z-velocity, 4) x-angular velocity, 5) y-angular velocity, 6) z-angular velocity.
        in 2D: 1) x-velocity, 2) y-velocity, 3) angular velocity.
        The fixity value is false for free and true for fixed conditions.
        """
        pass

    def set_force_app(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump applied force (vector).
        """
        pass

    def set_force_app_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump applied force.
        """
        pass

    def set_force_app_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump applied force.
        """
        pass

    def set_force_contact(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump contact force (vector).
        """
        pass

    def set_force_contact_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump contact force.
        """
        pass

    def set_force_contact_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump contact force.
        """
        pass

    def set_fragment(self, *args, **kwargs) -> Any:
        """
        (id: int) -> None.
        Set clump fragment ID.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the clump group name in a given slot.
        """
        pass

    def set_moi_fix(self, *args, **kwargs) -> Any:
        """
        (fixity: bool) -> None.
        Set the moment of intertia fixity state.
          When activated, the clump moment of inertia will not be automatically updated when a clump is scaled, the volume is changed, or when the density is changed.
        This is activated automatically when either the volume or moment of inertia is set manually via the clump attribute command or via the Clump object methods vol(), moi_real() or moi_prinreal().
        """
        pass

    def set_moi_prin_real(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump real principal moment of inertia.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method) (vector).
        """
        pass

    def set_moi_prin_real_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump real principal moment of inertia.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method).
        """
        pass

    def set_moi_prin_real_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump real principal moment of inertia.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method).
        """
        pass

    def set_moi_real(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the clump real moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method).
        """
        pass

    def set_moment_app(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump applied moment.
        """
        pass

    def set_moment_contact(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump contact moment.
        """
        pass

    def set_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump centroid location (vector).
        """
        pass

    def set_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump centroid location.
        """
        pass

    def set_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump centroid location.
        """
        pass

    def set_rotation(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump orientation.
        """
        pass

    def set_spin(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump angular velocity.
        """
        pass

    def set_vel(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump velocity (vector).
        """
        pass

    def set_vel_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump velocity.
        """
        pass

    def set_vel_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump velocity.
        """
        pass

    def set_vol(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump volume.
        In 2D this is the volume per unit thickness.
        """
        pass

    def spin(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump angular velocity.
        """
        pass

    def template(self, *args, **kwargs) -> Any:
        """
        () -> Template object or None.
        Get the template associated with this clump.
        The result will be None if no Template is associated with this clump.
        """
        pass

    def template_rotation(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump template relative orientation.
        """
        pass

    def template_scale(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump template relative scaling factor.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Rotate a vector from principal system.
        The returned vector is in the global axis system.
        """
        pass

    def to_prin(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Rotate a vector to principal system.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this clump is live.
        """
        pass

    def vel(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump velocity (vector).
        """
        pass

    def vel_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump velocity.
        """
        pass

    def vel_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump velocity.
        """
        pass

    def vol(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump volume.
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


class ClumpIter:
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

import numpy


def damp() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump local damping.
    """
    pass


def density() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump density.
    """
    pass


def disp() -> numpy.ndarray:
    """
    () -> array float{clump,2}.
    Get a numpy array of the clump displacement.
    """
    pass


def extra(slot: int) -> numpy.ndarray:
    """
    (slot: int) -> array float{clump} or float{clump}.
    Get the clump extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass


def fill_damp(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump local damping.
    The array must be the correct shape.
    """
    pass


def fill_density(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump density.
    The array must be the correct shape.
    """
    pass


def fill_disp(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Fill an existing array with the clump displacement.
    The array must be the correct shape.
    """
    pass


def fill_force_app(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Fill an existing array with the clump applied force.
    The array must be the correct shape.
    """
    pass


def fill_force_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Fill an existing array with the clump contact force.
    The array must be the correct shape.
    """
    pass


def fill_force_unbal(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Fill an existing array with the clump unbalanced force.
    The array must be the correct shape.
    """
    pass


def fill_mass(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the inertial clump mass.
    The array must be the correct shape.
    """
    pass


def fill_mass_real(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the real (gravitational) clump mass.
    The array must be the correct shape.
    """
    pass


def fill_moi_prin_real(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,dim}) -> None.
    Fill an existing array with the clump principal moments of inertia.
    The array must be the correct shape.
    """
    pass


def fill_moment_app(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump applied moment.
    The array must be the correct shape.
    """
    pass


def fill_moment_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump contact moment.
    The array must be the correct shape.
    """
    pass


def fill_moment_unbal(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump unbalanced moment.
    The array must be the correct shape.
    """
    pass


def fill_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Fill an existing array with the clump centroid location.
    The array must be the correct shape.
    """
    pass


def fill_rotation(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump orientation.
    The array must be the correct shape.
    """
    pass


def fill_spin(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump angular velocity.
    The array must be the correct shape.
    """
    pass


def fill_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Fill an existing array with the clump velocity.
    The array must be the correct shape.
    """
    pass


def fill_vol(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Fill an existing array with the clump volume.
    The array must be the correct shape.
    """
    pass


def force_app() -> numpy.ndarray:
    """
    () -> array float{clump,2}.
    Get a numpy array of the clump applied force.
    """
    pass


def force_contact() -> numpy.ndarray:
    """
    () -> array float{clump,2}.
    Get a numpy array of the clump contact force.
    """
    pass


def force_unbal() -> numpy.ndarray:
    """
    () -> array float{clump,2}.
    Get a numpy array of the clump unbalanced force.
    """
    pass


def ids() -> numpy.ndarray:
    """
    () -> array int{clump}.
    Get the clump ids as an array.
    """
    pass


def in_group(group_name: str, slot=...) -> numpy.ndarray:
    """
    (group_name: str, slot=1) -> array bool{clump}.
    Return clump group membership as a Boolean array.
    """
    pass


def mass() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the inertial clump mass.
    """
    pass


def mass_real() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the real (gravitational) clump mass.
    """
    pass


def moi_prin_real() -> numpy.ndarray:
    """
    () -> array float{clump,dim}.
    Get a numpy array of the clump principal moments of inertia.
    """
    pass


def moment_app() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump applied moment.
    """
    pass


def moment_contact() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump contact moment.
    """
    pass


def moment_unbal() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump unbalanced moment.
    """
    pass


def pos() -> numpy.ndarray:
    """
    () -> array float{clump,2}.
    Get a numpy array of the clump centroid location.
    """
    pass


def rotation() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump orientation.
    """
    pass


def set_damp(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Set the clump local damping from an array.
    """
    pass


def set_density(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Set the clump density from an array.
    """
    pass


def set_disp(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Set the clump displacement from an array.
    """
    pass


def set_extra(slot: int, data: numpy.ndarray) -> None:
    """
    (slot: int, data: array float{clump} or float{clump}) -> None.
    Set the clump extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass


def set_force_app(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Set the clump applied force from an array.
    """
    pass


def set_force_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Set the clump contact force from an array.
    """
    pass


def set_group(membership: numpy.ndarray, group_name: str, slot=...) -> None:
    """
    (membership: array bool{clump}, group_name: str, slot=1) -> None.
    Set clump group from an array.
    Where membership True set the corresponding clump to be a member of group group_name in the given slot.
    """
    pass


def set_moi_prin_real(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,dim}) -> None.
    Set the clump principal moments of inertia from an array.
    When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
    The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state.
    """
    pass


def set_moment_app(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Set the clump applied moment from an array.
    """
    pass


def set_moment_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Set the clump contact moment from an array.
    """
    pass


def set_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Set the clump centroid location from an array.
    """
    pass


def set_rotation(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Set the clump orientation from an array.
    """
    pass


def set_spin(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Set the clump angular velocity from an array.
    """
    pass


def set_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{clump,2}) -> None.
    Set the clump velocity from an array.
    """
    pass


def set_vol(data: numpy.ndarray) -> None:
    """
    (data: array float{clump}) -> None.
    Set the clump volume from an array.
    In 2D this is the volume per unit thickness.
    When modified no other clump attributes are changed (e.g., moment of inertia, pebble sizes, etc.).
    The specification of the volume in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state.
    """
    pass


def spin() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump angular velocity.
    """
    pass


def vel() -> numpy.ndarray:
    """
    () -> array float{clump,2}.
    Get a numpy array of the clump velocity.
    """
    pass


def vol() -> numpy.ndarray:
    """
    () -> array float{clump}.
    Get a numpy array of the clump volume.
    """
    pass

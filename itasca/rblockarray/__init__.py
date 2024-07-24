from typing import Any


def damp(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock local damping.
    """
    pass


def density(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock density.
    """
    pass


def disp(*args, **kwargs) -> Any:
    """
    () -> array float{rblock,2}.
    Get a numpy array of the rblock displacement.
    """
    pass


def extra(*args, **kwargs) -> Any:
    """
    (slot: int) -> array float{rblock} or float{rblock}.
    Get the rblock extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass


def fill_damp(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock local damping.
    The array must be the correct shape.
    """
    pass


def fill_density(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock density.
    The array must be the correct shape.
    """
    pass


def fill_disp(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Fill an existing array with the rblock displacement.
    The array must be the correct shape.
    """
    pass


def fill_force_app(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Fill an existing array with the rblock applied force.
    The array must be the correct shape.
    """
    pass


def fill_force_contact(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Fill an existing array with the rblock contact force.
    The array must be the correct shape.
    """
    pass


def fill_force_unbal(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Fill an existing array with the rblock unbalanced force.
    The array must be the correct shape.
    """
    pass


def fill_mass(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the inertial rblock mass.
    The array must be the correct shape.
    """
    pass


def fill_mass_real(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the real (gravitational) rblock mass.
    The array must be the correct shape.
    """
    pass


def fill_moi_prin_real(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,dim}) -> None.
    Fill an existing array with the rblock principal moments of inertia.
    The array must be the correct shape.
    """
    pass


def fill_moment_app(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock applied moment.
    The array must be the correct shape.
    """
    pass


def fill_moment_contact(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock contact moment.
    The array must be the correct shape.
    """
    pass


def fill_moment_unbal(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock unbalanced moment.
    The array must be the correct shape.
    """
    pass


def fill_pos(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Fill an existing array with the rblock centroid location.
    The array must be the correct shape.
    """
    pass


def fill_rotation(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock orientation.
    The array must be the correct shape.
    """
    pass


def fill_spin(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock angular velocity.
    The array must be the correct shape.
    """
    pass


def fill_vel(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Fill an existing array with the rblock velocity.
    The array must be the correct shape.
    """
    pass


def fill_vol(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Fill an existing array with the rblock volume.
    The array must be the correct shape.
    """
    pass


def force_app(*args, **kwargs) -> Any:
    """
    () -> array float{rblock,2}.
    Get a numpy array of the rblock applied force.
    """
    pass


def force_contact(*args, **kwargs) -> Any:
    """
    () -> array float{rblock,2}.
    Get a numpy array of the rblock contact force.
    """
    pass


def force_unbal(*args, **kwargs) -> Any:
    """
    () -> array float{rblock,2}.
    Get a numpy array of the rblock unbalanced force.
    """
    pass


def ids(*args, **kwargs) -> Any:
    """
    () -> array int{rblock}.
    Get the rblock ids as an array.
    """
    pass


def in_group(*args, **kwargs) -> Any:
    """
    (group_name: str, slot=1) -> array bool{rblock}.
    Return rblock group membership as a Boolean array.
    """
    pass


def mass(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the inertial rblock mass.
    """
    pass


def mass_real(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the real (gravitational) rblock mass.
    """
    pass


def moi_prin_real(*args, **kwargs) -> Any:
    """
    () -> array float{rblock,dim}.
    Get a numpy array of the rblock principal moments of inertia.
    """
    pass


def moment_app(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock applied moment.
    """
    pass


def moment_contact(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock contact moment.
    """
    pass


def moment_unbal(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock unbalanced moment.
    """
    pass


def pos(*args, **kwargs) -> Any:
    """
    () -> array float{rblock,2}.
    Get a numpy array of the rblock centroid location.
    """
    pass


def rotation(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock orientation.
    """
    pass


def set_damp(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Set the rblock local damping from an array.
    """
    pass


def set_density(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Set the rblock density from an array.
    """
    pass


def set_disp(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Set the rblock displacement from an array.
    """
    pass


def set_extra(*args, **kwargs) -> Any:
    """
    (slot: int, data: array float{rblock} or float{rblock}) -> None.
    Set the rblock extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass


def set_force_app(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Set the rblock applied force from an array.
    """
    pass


def set_force_contact(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Set the rblock contact force from an array.
    """
    pass


def set_group(*args, **kwargs) -> Any:
    """
    (membership: array bool{rblock}, group_name: str, slot=1) -> None.
    Set rblock group from an array.
    Where membership True set the corresponding rblock to be a member of group group_name in the given slot.
    """
    pass


def set_moi_prin_real(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,dim}) -> None.
    Set the rblock principal moments of inertia from an array.
    When modified no other rblock attributes are changed (e.g., pebble sizes, rblock volume, etc.).
    The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state.
    """
    pass


def set_moment_app(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Set the rblock applied moment from an array.
    """
    pass


def set_moment_contact(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Set the rblock contact moment from an array.
    """
    pass


def set_pos(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Set the rblock centroid location from an array.
    """
    pass


def set_rotation(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Set the rblock orientation from an array.
    """
    pass


def set_spin(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Set the rblock angular velocity from an array.
    """
    pass


def set_vel(*args, **kwargs) -> Any:
    """
    (data: array float{rblock,2}) -> None.
    Set the rblock velocity from an array.
    """
    pass


def set_vol(*args, **kwargs) -> Any:
    """
    (data: array float{rblock}) -> None.
    Set the rblock volume from an array.
    In 2D this is the volume per unit thickness.
    When modified no other rblock attributes are changed (e.g., moment of inertia, pebble sizes, etc.).
    The specification of the volume in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state.
    """
    pass


def spin(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock angular velocity.
    """
    pass


def vel(*args, **kwargs) -> Any:
    """
    () -> array float{rblock,2}.
    Get a numpy array of the rblock velocity.
    """
    pass


def vol(*args, **kwargs) -> Any:
    """
    () -> array float{rblock}.
    Get a numpy array of the rblock volume.
    """
    pass

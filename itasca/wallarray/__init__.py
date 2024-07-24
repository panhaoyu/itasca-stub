import numpy


def cutoff() -> numpy.ndarray:
    """
    () -> array float{wall}.
    Get a numpy array of the wall cutoff angle.
    """
    pass


def disp() -> numpy.ndarray:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall displacement.
    """
    pass


def extra(slot: int) -> numpy.ndarray:
    """
    (slot: int) -> array float{wall} or float{wall}.
    Get the wall extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass


def fill_cutoff(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall cutoff angle.
    The array must be the correct shape.
    """
    pass


def fill_disp(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall displacement.
    The array must be the correct shape.
    """
    pass


def fill_force_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall contact force.
    The array must be the correct shape.
    """
    pass


def fill_moment_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall contact moment.
    The array must be the correct shape.
    """
    pass


def fill_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall location.
    The array must be the correct shape.
    """
    pass


def fill_rotation(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall orientation.
    The array must be the correct shape.
    """
    pass


def fill_rotation_center(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,dim}) -> None.
    Fill an existing array with the wall center of rotation.
    The array must be the correct shape.
    """
    pass


def fill_spin(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall angular velocity.
    The array must be the correct shape.
    """
    pass


def fill_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall velocity.
    The array must be the correct shape.
    """
    pass


def force_contact() -> numpy.ndarray:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall contact force.
    """
    pass


def ids() -> numpy.ndarray:
    """
    () -> array int{wall}.
    Get the wall ids as an array.
    """
    pass


def in_group(group_name: str, slot=...) -> numpy.ndarray:
    """
    (group_name: str, slot=1) -> array bool{wall}.
    Return wall group membership as a Boolean array.
    """
    pass


def moment_contact() -> numpy.ndarray:
    """
    () -> array float{wall}.
    Get a numpy array of the wall contact moment.
    """
    pass


def pos() -> numpy.ndarray:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall location.
    """
    pass


def rotation() -> numpy.ndarray:
    """
    () -> array float{wall}.
    Get a numpy array of the wall orientation.
    """
    pass


def rotation_center() -> numpy.ndarray:
    """
    () -> array float{wall,dim}.
    Get a numpy array of the wall center of rotation.
    """
    pass


def set_cutoff(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Set the wall cutoff angle from an array.
    """
    pass


def set_disp(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Set the wall displacement from an array.
    """
    pass


def set_extra(slot: int, data: numpy.ndarray) -> None:
    """
    (slot: int, data: array float{wall} or float{wall}) -> None.
    Set the wall extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass


def set_force_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Set the wall contact force from an array.
    """
    pass


def set_group(membership: numpy.ndarray, group_name: str, slot=...) -> None:
    """
    (membership: array bool{wall}, group_name: str, slot=1) -> None.
    Set wall group from an array.
    Where membership True set the corresponding wall to be a member of group group_name in the given slot.
    """
    pass


def set_moment_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Set the wall contact moment from an array.
    """
    pass


def set_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Set the wall location from an array.
    """
    pass


def set_rotation(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Set the wall orientation from an array.
    """
    pass


def set_rotation_center(data: numpy.ndarray) -> None:
    """
    ((data: array float{wall,dim}) -> None.
    Set the wall center of rotation from an array.
    """
    pass


def set_spin(data: numpy.ndarray) -> None:
    """
    (data: array float{wall}) -> None.
    Set the wall angular velocity from an array.
    """
    pass


def set_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{wall,2}) -> None.
    Set the wall velocity from an array.
    """
    pass


def spin() -> numpy.ndarray:
    """
    () -> array float{wall}.
    Get a numpy array of the wall angular velocity.
    """
    pass


def vel() -> numpy.ndarray:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall velocity.
    """
    pass

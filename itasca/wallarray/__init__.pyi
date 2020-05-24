from typing import Any

def cutoff(*args, **kwargs) -> Any:
    """
    () -> array float{wall}.
    Get a numpy array of the wall cutoff angle.
    """
    pass

def disp(*args, **kwargs) -> Any:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall displacement.
    """
    pass

def extra(*args, **kwargs) -> Any:
    """
    (slot: int) -> array float{wall} or float{wall}.
    Get the wall extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass

def fill_cutoff(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall cutoff angle.
    The array must be the correct shape.
    """
    pass

def fill_disp(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall displacement.
    The array must be the correct shape.
    """
    pass

def fill_force_contact(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall contact force.
    The array must be the correct shape.
    """
    pass

def fill_moment_contact(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall contact moment.
    The array must be the correct shape.
    """
    pass

def fill_pos(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall location.
    The array must be the correct shape.
    """
    pass

def fill_rotation(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall orientation.
    The array must be the correct shape.
    """
    pass

def fill_rotation_center(*args, **kwargs) -> Any:
    """
    (data: array float{wall,dim}) -> None.
    Fill an existing array with the wall center of rotation.
    The array must be the correct shape.
    """
    pass

def fill_spin(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Fill an existing array with the wall angular velocity.
    The array must be the correct shape.
    """
    pass

def fill_vel(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Fill an existing array with the wall velocity.
    The array must be the correct shape.
    """
    pass

def force_contact(*args, **kwargs) -> Any:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall contact force.
    """
    pass

def ids(*args, **kwargs) -> Any:
    """
    () -> array int{wall}.
    Get the wall ids as an array.
    """
    pass

def in_group(*args, **kwargs) -> Any:
    """
    (group_name: str, slot=1) -> array bool{wall}.
    Return wall group membership as a Boolean array.
    """
    pass

def moment_contact(*args, **kwargs) -> Any:
    """
    () -> array float{wall}.
    Get a numpy array of the wall contact moment.
    """
    pass

def pos(*args, **kwargs) -> Any:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall location.
    """
    pass

def rotation(*args, **kwargs) -> Any:
    """
    () -> array float{wall}.
    Get a numpy array of the wall orientation.
    """
    pass

def rotation_center(*args, **kwargs) -> Any:
    """
    () -> array float{wall,dim}.
    Get a numpy array of the wall center of rotation.
    """
    pass

def set_cutoff(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Set the wall cutoff angle from an array.
    """
    pass

def set_disp(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Set the wall displacement from an array.
    """
    pass

def set_extra(*args, **kwargs) -> Any:
    """
    (slot: int, data: array float{wall} or float{wall}) -> None.
    Set the wall extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass

def set_force_contact(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Set the wall contact force from an array.
    """
    pass

def set_group(*args, **kwargs) -> Any:
    """
    (membership: array bool{wall}, group_name: str, slot=1) -> None.
    Set wall group from an array.
    Where membership True set the corresponding wall to be a member of group group_name in the given slot.
    """
    pass

def set_moment_contact(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Set the wall contact moment from an array.
    """
    pass

def set_pos(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Set the wall location from an array.
    """
    pass

def set_rotation(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Set the wall orientation from an array.
    """
    pass

def set_rotation_center(*args, **kwargs) -> Any:
    """
    ((data: array float{wall,dim}) -> None.
    Set the wall center of rotation from an array.
    """
    pass

def set_spin(*args, **kwargs) -> Any:
    """
    (data: array float{wall}) -> None.
    Set the wall angular velocity from an array.
    """
    pass

def set_vel(*args, **kwargs) -> Any:
    """
    (data: array float{wall,2}) -> None.
    Set the wall velocity from an array.
    """
    pass

def spin(*args, **kwargs) -> Any:
    """
    () -> array float{wall}.
    Get a numpy array of the wall angular velocity.
    """
    pass

def vel(*args, **kwargs) -> Any:
    """
    () -> array float{wall,2}.
    Get a numpy array of the wall velocity.
    """
    pass


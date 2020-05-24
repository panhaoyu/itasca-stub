from typing import Any

def extra(*args, **kwargs) -> Any:
    """
    (slot: int) -> array float{pebble} or float{pebble}.
    Get the pebble extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass

def fill_pos(*args, **kwargs) -> Any:
    """
    (data: array float{pebble,2}) -> None.
    Fill an existing array with the pebble location.
    The array must be the correct shape.
    """
    pass

def fill_radius(*args, **kwargs) -> Any:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the pebble radii.
    The array must be the correct shape.
    """
    pass

def fill_vel(*args, **kwargs) -> Any:
    """
    (data: array float{pebble,2}) -> None.
    Fill an existing array with the pebble velocity.
    The array must be the correct shape.
    """
    pass

def ids(*args, **kwargs) -> Any:
    """
    () -> array int{pebble}.
    Get the pebble ids as an array.
    """
    pass

def in_group(*args, **kwargs) -> Any:
    """
    (group_name: str, slot=1) -> array bool{pebble}.
    Return pebble group membership as a Boolean array.
    """
    pass

def pos(*args, **kwargs) -> Any:
    """
    () -> array float{pebble,2}.
    Get a numpy array of the pebble location.
    """
    pass

def radius(*args, **kwargs) -> Any:
    """
    () -> array float{ball}.
    Get a numpy array of the pebble radii.
    """
    pass

def set_extra(*args, **kwargs) -> Any:
    """
    (slot: int, data: array float{pebble} or float{pebble}) -> None.
    Set the pebble extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass

def set_group(*args, **kwargs) -> Any:
    """
    (membership: array bool{pebble}, group_name: str, slot=1) -> None.
    Set pebble group from an array.
    Where membership True set the corresponding pebble to be a member of group group_name in the given slot.
    """
    pass

def set_pos(*args, **kwargs) -> Any:
    """
    (data: array float{pebble,2}) -> None.
    Set the pebble location from an array.
    """
    pass

def set_radius(*args, **kwargs) -> Any:
    """
    (data: array float{ball}) -> None.
    Set the pebble radii from an array.
    """
    pass

def vel(*args, **kwargs) -> Any:
    """
    () -> array float{pebble,2}.
    Get a numpy array of the pebble velocity.
    """
    pass


from typing import Any


def branch(*args, **kwargs) -> Any:
    """
    () -> array float{contact,2}.
    Get a numpy array of the contact branch vectors in the global coordinate system.
    """
    pass


def extra(*args, **kwargs) -> Any:
    """
    (slot: int) -> array float{contact} or float{contact}.
    Get the contact extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass


def fill_branch(*args, **kwargs) -> Any:
    """
    (data: array float{contact,2}) -> None.
    Fill an existing array with the contact branch vectors in the global coordinate system.
    The array must be the correct shape.
    """
    pass


def fill_force_global(*args, **kwargs) -> Any:
    """
    (data: array float{contact,2}) -> None.
    Fill an existing array with the contact force in the global coordinate system.
    The array must be the correct shape.
    """
    pass


def fill_force_local(*args, **kwargs) -> Any:
    """
    (data: array float{contact,2}) -> None.
    Fill an existing array with the contact force in the local coordinate system.
    The array must be the correct shape.
    """
    pass


def fill_force_normal(*args, **kwargs) -> Any:
    """
    (data: array float{contact}) -> None.
    Fill an existing array with the contact normal force.
    The array must be the correct shape.
    """
    pass


def fill_force_shear(*args, **kwargs) -> Any:
    """
    (data: array float{contact}) -> None.
    Fill an existing array with the contact shear force magnitude.
    The array must be the correct shape.
    """
    pass


def fill_gap(*args, **kwargs) -> Any:
    """
    (data: array float{contact}) -> None.
    Fill an existing array with the contact gap.
    The array must be the correct shape.
    """
    pass


def fill_moment1_global(*args, **kwargs) -> Any:
    """
    (data: array float{contact}) -> None.
    Fill an existing array with the contact moment acting on end 1 in the global coordinate system.
    The array must be the correct shape.
    """
    pass


def fill_moment1_local(*args, **kwargs) -> Any:
    """
    (data: array float{contact}) -> None.
    Fill an existing array with the contact moment acting on end 1 in the local coordinate system.
    The array must be the correct shape.
    """
    pass


def fill_moment2_global(*args, **kwargs) -> Any:
    """
    (data: array float{contact}) -> None.
    Fill an existing array with the contact moment acting on end 2 in the global coordinate system.
    The array must be the correct shape.
    """
    pass


def fill_moment2_local(*args, **kwargs) -> Any:
    """
    (data: array float{contact}) -> None.
    Fill an existing array with the contact moment acting on end 2 in the local coordinate system.
    The array must be the correct shape.
    """
    pass


def fill_normal(*args, **kwargs) -> Any:
    """
    (data: array float{contact,2}) -> None.
    Fill an existing array with the contact normal.
    The array must be the correct shape.
    """
    pass


def fill_offset(*args, **kwargs) -> Any:
    """
    (data: array float{contact,2}) -> None.
    Fill an existing array with the contact offset.
    The array must be the correct shape.
    """
    pass


def fill_pos(*args, **kwargs) -> Any:
    """
    (data: array float{contact,2}) -> None.
    Fill an existing array with the contact position.
    The array must be the correct shape.
    """
    pass


def force_global(*args, **kwargs) -> Any:
    """
    () -> array float{contact,2}.
    Get a numpy array of the contact force in the global coordinate system.
    """
    pass


def force_local(*args, **kwargs) -> Any:
    """
    () -> array float{contact,2}.
    Get a numpy array of the contact force in the local coordinate system.
    """
    pass


def force_normal(*args, **kwargs) -> Any:
    """
    () -> array float{contact}.
    Get a numpy array of the contact normal force.
    """
    pass


def force_shear(*args, **kwargs) -> Any:
    """
    () -> array float{contact}.
    Get a numpy array of the contact shear force magnitude.
    """
    pass


def gap(*args, **kwargs) -> Any:
    """
    () -> array float{contact}.
    Get a numpy array of the contact gap.
    """
    pass


def ids(*args, **kwargs) -> Any:
    """
    () -> array int{contact}.
    Get the contact ids as an array.
    """
    pass


def in_group(*args, **kwargs) -> Any:
    """
    (group_name: str, slot=1) -> array bool{contact}.
    Return contact group membership as a Boolean array.
    """
    pass


def indices(*args, **kwargs) -> Any:
    """
    () -> array int64{contact,2}.
    Get a numpy array of the indices of the balls on end1 and end2 of the contacts.
    The ball indices are relative to the ball arrays returned by the itasca.ballarray module.
    """
    pass


def moment1_global(*args, **kwargs) -> Any:
    """
    () -> array float{contact}.
    Get a numpy array of the contact moment acting on end 1 in the global coordinate system.
    """
    pass


def moment1_local(*args, **kwargs) -> Any:
    """
    () -> array float{contact}.
    Get a numpy array of the contact moment acting on end 1 in the local coordinate system.
    """
    pass


def moment2_global(*args, **kwargs) -> Any:
    """
    () -> array float{contact}.
    Get a numpy array of the contact moment acting on end 2 in the global coordinate system.
    """
    pass


def moment2_local(*args, **kwargs) -> Any:
    """
    () -> array float{contact}.
    Get a numpy array of the contact moment acting on end 2 in the local coordinate system.
    """
    pass


def normal(*args, **kwargs) -> Any:
    """
    () -> array float{contact,2}.
    Get a numpy array of the contact normal.
    """
    pass


def offset(*args, **kwargs) -> Any:
    """
    () -> array float{contact,2}.
    Get a numpy array of the contact offset.
    """
    pass


def pos(*args, **kwargs) -> Any:
    """
    () -> array float{contact,2}.
    Get a numpy array of the contact position.
    """
    pass


def set_extra(*args, **kwargs) -> Any:
    """
    (slot: int, data: array float{contact} or float{contact}) -> None.
    Set the contact extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass


def set_group(*args, **kwargs) -> Any:
    """
    (membership: array bool{contact}, group_name: str, slot=1) -> None.
    Set contact group from an array.
    Where membership True set the corresponding contact to be a member of group group_name in the given slot.
    """
    pass

import numpy


def conveyor() -> numpy.ndarray:
    """
    () -> array float{facet,dim}.
    Get a numpy array of the facet conveyor velocity.
    """
    pass


def extra(slot: int) -> numpy.ndarray:
    """
    (slot: int) -> array float{facet} or float{facet}.
    Get the facet extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass


def fill_conveyor(data: numpy.ndarray) -> None:
    """
    (data: array float{facet,dim}) -> None.
    Fill an existing array with the facet conveyor velocity.
    The array must be the correct shape.
    """
    pass


def fill_normal(data: numpy.ndarray) -> None:
    """
    (data: array float{facet,dim}) -> None.
    Fill an existing array with the facet normal.
    The array must be the correct shape.
    """
    pass


def fill_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{facet,2}) -> None.
    Fill an existing array with the facet location.
    The array must be the correct shape.
    """
    pass


def ids() -> numpy.ndarray:
    """
    () -> array int{facet}.
    Get the facet ids as an array.
    """
    pass


def in_group(group_name: str, slot=...) -> numpy.ndarray:
    """
    (group_name: str, slot=1) -> array bool{facet}.
    Return facet group membership as a Boolean array.
    """
    pass


def normal() -> numpy.ndarray:
    """
    () -> array float{facet,dim}.
    Get a numpy array of the facet normal.
    """
    pass


def pos() -> numpy.ndarray:
    """
    () -> array float{facet,2}.
    Get a numpy array of the facet location.
    """
    pass


def set_conveyor(data: numpy.ndarray) -> None:
    """
    ((data: array float{facet,dim}) -> None.
    Set the facet conveyor velocity from an array.
    """
    pass


def set_extra(slot: int, data: numpy.ndarray) -> None:
    """
    (slot: int, data: array float{facet} or float{facet}) -> None.
    Set the facet extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass


def set_group(membership: numpy.ndarray, group_name: str, slot=...) -> None:
    """
    (membership: array bool{facet}, group_name: str, slot=1) -> None.
    Set facet group from an array.
    Where membership True set the corresponding facet to be a member of group group_name in the given slot.
    """
    pass

import numpy


def fill_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{vertex,2}) -> None.
    Fill an existing array with the vertex location.
    The array must be the correct shape.
    """
    pass


def fill_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{vertex,2}) -> None.
    Fill an existing array with the vertex velocity.
    The array must be the correct shape.
    """
    pass


def ids() -> numpy.ndarray:
    """
    () -> array int{vertex}.
    Get the vertex ids as an array.
    """
    pass


def pos() -> numpy.ndarray:
    """
    () -> array float{vertex,2}.
    Get a numpy array of the vertex location.
    """
    pass


def set_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{vertex,2}) -> None.
    Set the vertex location from an array.
    """
    pass


def set_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{vertex,2}) -> None.
    Set the vertex velocity from an array.
    """
    pass


def vel() -> numpy.ndarray:
    """
    () -> array float{vertex,2}.
    Get a numpy array of the vertex velocity.
    """
    pass

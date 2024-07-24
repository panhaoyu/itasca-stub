from typing import Any


def fill_pos(*args, **kwargs) -> Any:
    """
    (data: array float{vertex,2}) -> None.
    Fill an existing array with the vertex location.
    The array must be the correct shape.
    """
    pass


def fill_vel(*args, **kwargs) -> Any:
    """
    (data: array float{vertex,2}) -> None.
    Fill an existing array with the vertex velocity.
    The array must be the correct shape.
    """
    pass


def ids(*args, **kwargs) -> Any:
    """
    () -> array int{vertex}.
    Get the vertex ids as an array.
    """
    pass


def pos(*args, **kwargs) -> Any:
    """
    () -> array float{vertex,2}.
    Get a numpy array of the vertex location.
    """
    pass


def set_pos(*args, **kwargs) -> Any:
    """
    (data: array float{vertex,2}) -> None.
    Set the vertex location from an array.
    """
    pass


def set_vel(*args, **kwargs) -> Any:
    """
    (data: array float{vertex,2}) -> None.
    Set the vertex velocity from an array.
    """
    pass


def vel(*args, **kwargs) -> Any:
    """
    () -> array float{vertex,2}.
    Get a numpy array of the vertex velocity.
    """
    pass

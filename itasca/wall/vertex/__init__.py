from typing import Any


def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of wall vertices.
    """
    pass


def find(*args, **kwargs) -> Any:
    """
    (id: int) -> WallVertex object.
    Get the WallVertex object with the given ID number.
    """
    pass


def inbox(*args, **kwargs) -> Any:
    """
    (lower_bound: vec, upper_bound: vec, boundary=False) -> tuple of WallVertex objects.
    Get vertices with extents intersecting a box.
    If the optional keyword argument boundary is True only return the vertexs inside the extent.
    """
    pass


def list(*args, **kwargs) -> Any:
    """
    () -> WallVertex iterator.
    Get a WallVertex iterator object.
    """
    pass


def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum vertex ID.
    """
    pass


def near(*args, **kwargs) -> Any:
    """
    (point: vec) -> WallVertex object.
    Find the closest vertex to a point.
    """
    pass


class Vertex:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete this vertex.
        All facets sharing the vertex are deleted and the wall position is updated.
        """
        pass

    def facets(self, *args, **kwargs) -> Any:
        """
        () -> tuple of facet objects.
        Get the facets sharing this vertex.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the vertex id.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the vertex location (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the vertex location.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the vertex location.
        """
        pass

    def set_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the vertex location (vector).
        """
        pass

    def set_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the vertex location.
        """
        pass

    def set_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the vertex location.
        """
        pass

    def set_vel(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the vertex velocity (vector).
        """
        pass

    def set_vel_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the vertex velocity.
        """
        pass

    def set_vel_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the vertex velocity.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get True of this object is a live vertex.
        """
        pass

    def vel(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the vertex velocity (vector).
        """
        pass

    def vel_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the vertex velocity.
        """
        pass

    def vel_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the vertex velocity.
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


class VertexIter:
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

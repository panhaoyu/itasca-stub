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
    Get the number of rblock templates.
    """
    pass


def find(*args, **kwargs) -> Any:
    """
    (template_name: str) -> Template object.
    Find a rblock template by name.
    """
    pass


def findpebble(*args, **kwargs) -> Any:
    """
    (pebble_id: int) -> RBlock Template Pebble object.
    Find the rblock template pebble with the given ID, in the rblock template.
    """
    pass


def list(*args, **kwargs) -> Any:
    """
    () -> RBlock template iterator object.
    Get a rblock template iterator object.
    """
    pass


def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum rblock templates ID.
    """
    pass


class Template:
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
        Delete this rblock template.
        All rblocks that referred to this rblock template no longer refer to any rblock template.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the rblock template id.
        """
        pass

    def moi(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the rblock template moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        """
        pass

    def moi_prin(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the rblock template principal moment of inertia (vector).
        """
        pass

    def moi_prin_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the rblock template principal moment of inertia.
        """
        pass

    def moi_prin_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the rblock template principal moment of inertia.
        """
        pass

    def name(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the rblock template name.
        """
        pass

    def set_moi(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the rblock template moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        When modified no other rblock attributes are changed (e.g., pebble sizes, rblock volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a rblock unless the user changes the fix state (see the RBlock moi_fix() method).
        """
        pass

    def set_moi_prin(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the rblock template principal moment of inertia (vector).
        """
        pass

    def set_moi_prin_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the rblock template principal moment of inertia.
        """
        pass

    def set_moi_prin_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the rblock template principal moment of inertia.
        """
        pass

    def set_vol(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the rblock template volume.
        In 2D this is the volume per unit thickness.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True of this object is a live rblock template.
        """
        pass

    def vol(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the rblock template volume.
        In 2D this is the volume per unit thickness.
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


class TemplateIter:
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

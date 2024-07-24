from typing import Any


def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid Measure objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of measures.
    """
    pass


def find(*args, **kwargs) -> Any:
    """
    (id: int) -> Measure object.
    Get the measure object with the given ID number.
    """
    pass


def list(*args, **kwargs) -> Any:
    """
    () -> Measure iterator object.
    Get a measure iterator object.
    """
    pass


def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum measure ID.
    """
    pass


class Measure:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def coordination(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the measure coordination.
        """
        pass

    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete this measurement object.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the measure id.
        """
        pass

    def porosity(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the measure porosity.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the measure location (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the measure location.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the measure location.
        """
        pass

    def radius(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the measure radius.
        """
        pass

    def set_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the measure location (vector).
        """
        pass

    def set_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the measure location.
        """
        pass

    def set_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the measure location.
        """
        pass

    def set_radius(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the measure radius.
        """
        pass

    def size(self, *args, **kwargs) -> Any:
        """
        () -> array float{nbin,2}.
        Get a numpy array of the cumulative size distribution falling withinthis measure object where nbin is the number of bins for the size distribution calculation (see the MEASURE CREATE or MEASURE MODIFY commands.
        """
        pass

    def strainrate(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the strain rate tensor calculated for this measurement object.
        """
        pass

    def strainrate_full(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the full strain rate tensor calculated for this measurement object.
        """
        pass

    def stress(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the stress tensor calculated for this measurement object.
        """
        pass

    def stress_full(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the full stress tensor calculated for this measurement object.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this measure is live.
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


class MeasureIter:
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

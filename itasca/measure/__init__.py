import typing
from typing import Any

import numpy
import vec

import itasca.measure


def _plist() -> typing.Tuple[itasca.measure.Measure, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid Measure objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def count() -> int:
    """
    () -> int.
    Get the number of measures.
    """
    pass


def find(id: int) -> itasca.measure.Measure:
    """
    (id: int) -> Measure object.
    Get the measure object with the given ID number.
    """
    pass


def list() -> itasca.measure.MeasureIter:
    """
    () -> Measure iterator object.
    Get a measure iterator object.
    """
    pass


def maxid() -> int:
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

    def coordination(self) -> float:
        """
        () -> float.
        Get the measure coordination.
        """
        pass

    def delete(self) -> None:
        """
        () -> None.
        Delete this measurement object.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the measure id.
        """
        pass

    def porosity(self) -> float:
        """
        () -> float.
        Get the measure porosity.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the measure location (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the measure location.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the measure location.
        """
        pass

    def radius(self) -> float:
        """
        () -> float.
        Get the measure radius.
        """
        pass

    def set_pos(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the measure location (vector).
        """
        pass

    def set_pos_x(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the x-component of the measure location.
        """
        pass

    def set_pos_y(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the y-component of the measure location.
        """
        pass

    def set_radius(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the measure radius.
        """
        pass

    def size(self) -> numpy.ndarray:
        """
        () -> array float{nbin,2}.
        Get a numpy array of the cumulative size distribution falling withinthis measure object where nbin is the number of bins for the size distribution calculation (see the MEASURE CREATE or MEASURE MODIFY commands.
        """
        pass

    def strainrate(self) -> vec.tens3:
        """
        () -> tensor.
        Get the strain rate tensor calculated for this measurement object.
        """
        pass

    def strainrate_full(self) -> vec.tens3:
        """
        () -> tensor.
        Get the full strain rate tensor calculated for this measurement object.
        """
        pass

    def stress(self) -> vec.tens3:
        """
        () -> tensor.
        Get the stress tensor calculated for this measurement object.
        """
        pass

    def stress_full(self) -> vec.tens3:
        """
        () -> tensor.
        Get the full stress tensor calculated for this measurement object.
        """
        pass

    def valid(self) -> bool:
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

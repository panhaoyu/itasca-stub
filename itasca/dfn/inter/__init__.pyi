from typing import Any

def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid intersect objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass

def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of intersections.
    """
    pass

def find(*args, **kwargs) -> Any:
    """
    (id: int) -> Intersection object.
    Get the intersection object with the given ID number.
    """
    pass

def list(*args, **kwargs) -> Any:
    """
    () -> Intersection iterator object.
    Get an intersection iterator object.
    """
    pass

def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum intersection ID.
    """
    pass

class Inter:
    __hash__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass
    
    def end1(self, *args, **kwargs) -> Any:
        """
        () -> Fracture object.
        Get the end1 fracture object.
        """
        pass
    
    def end2(self, *args, **kwargs) -> Any:
        """
        () -> Fracture object.
        Get the end2 fracture object.
        """
        pass
    
    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the intersection extra data in the given slot.
        """
        pass
    
    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the intersection group name in a given slot.
        """
        pass
    
    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the intersection.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass
    
    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this intersection is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass
    
    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the intersection id.
        """
        pass
    
    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the intersection is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass
    
    def pos1(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the intersection first end position (vector).
        """
        pass
    
    def pos1_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the intersection first end position.
        """
        pass
    
    def pos1_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the intersection first end position.
        """
        pass
    
    def pos2(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the intersection second end position (vector).
        """
        pass
    
    def pos2_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the intersection second end position.
        """
        pass
    
    def pos2_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the intersection second end position.
        """
        pass
    
    def set(self, *args, **kwargs) -> Any:
        """
        () -> Intersection set object.
        Get the intersection set to which this intersection belongs.
        """
        pass
    
    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the intersection extra data in the given slot.
        """
        pass
    
    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the intersection group name in a given slot.
        """
        pass
    
    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this intersection is live.
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
    

class InterIter:
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
    

from typing import Any

def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid intersection set objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass

def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of intersection sets.
    """
    pass

def find(*args, **kwargs) -> Any:
    """
    (id: int) -> Intersection set object.
    Get the intersection set object with the given ID number.
    """
    pass

def list(*args, **kwargs) -> Any:
    """
    () -> Intersection set iterator object.
    Get an intersection set iterator object.
    """
    pass

def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum intersection set ID.
    """
    pass

class Setinter:
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
        Delete this intersection set, includingall intersections.
        """
        pass
    
    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the intersection set id.
        """
        pass
    
    def inter_count(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the number of intersections in this intersection set.
        """
        pass
    
    def inters(self, *args, **kwargs) -> Any:
        """
        () -> Intersection iterator object.
        Get an intersection iterator object of all intersections falling within this intersection set.
        """
        pass
    
    def name(self, *args, **kwargs) -> Any:
        """
        () -> string.
        Get the intersection set name.
        """
        pass
    
    def path(self, *args, **kwargs) -> Any:
        """
        (fracture1, fracture2) -> tuple of Fracture objects.
        Get the path between fractures fracture1 and fracture2.
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
    

class SetinterIter:
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
    

from typing import Any

def _plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid template objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass

def count(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of templates.
    """
    pass

def find(*args, **kwargs) -> Any:
    """
    (id: int) -> template object.
    Get the template object with the given ID number.
    """
    pass

def list(*args, **kwargs) -> Any:
    """
    () -> template iterator object.
    Get a template iterator object.
    """
    pass

def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum template ID.
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
    
    def dipmax(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the template maximum dip in degrees.
        """
        pass
    
    def dipmin(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the template minimum dip in degrees.
        """
        pass
    
    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the template id.
        """
        pass
    
    def name(self, *args, **kwargs) -> Any:
        """
        () -> string.
        Get the template name.
        """
        pass
    
    def norientparam(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the template number of orientation parameters.
        """
        pass
    
    def nposparam(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the template number of position parameters.
        """
        pass
    
    def nsizeparam(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the template number of size parameters.
        """
        pass
    
    def orientparam(self, *args, **kwargs) -> Any:
        """
        (index) -> string or float.
        Get a orientation parameter.
        The number of parameters can be assessed with the norientparam method.
        """
        pass
    
    def orienttype(self, *args, **kwargs) -> Any:
        """
        () -> string.
        Get the template orientation type name.
        Acceptable values are uniform, gauss, powerlaw, bootstrapped, fish, fisher (3D only) and dips (3D only).
        """
        pass
    
    def posparam(self, *args, **kwargs) -> Any:
        """
        (index) -> string or float.
        Get a position parameter.
        The number of parameters can be assessed with the nposparam method.
        """
        pass
    
    def postype(self, *args, **kwargs) -> Any:
        """
        () -> string.
        Get the template orientation type name.
        Acceptable values are uniform, gauss, bootstrapped and fish.
        """
        pass
    
    def set_dipmax(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the template maximum dip in degrees.
        """
        pass
    
    def set_dipmin(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the template minimum dip in degrees.
        """
        pass
    
    def set_orientparam(self, *args, **kwargs) -> Any:
        """
        (index, parameter) -> None.
        Set an orientation parameter.
        The parameter can be either a string or a float depending on the parameter.
        The number of parameters can be assessed with the norientparam method.
        """
        pass
    
    def set_orienttype(self, *args, **kwargs) -> Any:
        """
        (value: string) -> None.
        Set the template orientation type name.
        Acceptable values are uniform, gauss, powerlaw, bootstrapped, fish, fisher (3D only) and dips (3D only).
        """
        pass
    
    def set_posparam(self, *args, **kwargs) -> Any:
        """
        (index, parameter) -> None.
        Set a position parameter.
        The parameter can be either a string or a float depending on the parameter.
        The number of parameters can be assessed with the nposparam method.
        """
        pass
    
    def set_postype(self, *args, **kwargs) -> Any:
        """
        (value: string) -> None.
        Set the template orientation type name.
        Acceptable values are uniform, gauss, bootstrapped and fish.
        """
        pass
    
    def set_sizemax(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the template maximum size.
        The fracture size is defined as the {fracture length in 2D; disk diameter in 3D}.
        """
        pass
    
    def set_sizemin(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the template minimum size.
        The fracture size is defined as the {fracture length in 2D; disk diameter in 3D}.
        """
        pass
    
    def set_sizeparam(self, *args, **kwargs) -> Any:
        """
        (index, parameter) -> None.
        Set a size parameter.
        The parameter can be either a string or a float depending on the parameter.
        The number of parameters can be assessed with the nposparam method.
        """
        pass
    
    def set_sizetype(self, *args, **kwargs) -> Any:
        """
        (value: string) -> None.
        Set the template size type name.
        Acceptable values are uniform, gauss, powerlaw, bootstrapped and fish.
        """
        pass
    
    def sizemax(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the template maximum size.
        The fracture size is defined as the {fracture length in 2D; disk diameter in 3D}.
        """
        pass
    
    def sizemin(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the template minimum size.
        The fracture size is defined as the {fracture length in 2D; disk diameter in 3D}.
        """
        pass
    
    def sizeparam(self, *args, **kwargs) -> Any:
        """
        (index) -> string or float.
        Get a size parameter.
        The number of parameters can be assessed with the nsizeparam method.
        """
        pass
    
    def sizetype(self, *args, **kwargs) -> Any:
        """
        () -> string.
        Get the template size type name.
        Acceptable values are uniform, gauss, powerlaw, bootstrapped and fish.
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
    

class templateIter:
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
    

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
    Get the number of clump templates.
    """
    pass


def find(*args, **kwargs) -> Any:
    """
    (template_name: str) -> Template object.
    Find a clump template by name.
    """
    pass


def findpebble(*args, **kwargs) -> Any:
    """
    (pebble_id: int) -> Clump Template Pebble object.
    Find the clump template pebble with the given ID, in the clump template.
    """
    pass


def list(*args, **kwargs) -> Any:
    """
    () -> Clump template iterator object.
    Get a clump template iterator object.
    """
    pass


def make(*args, **kwargs) -> Any:
    """
    (clump template: Clump template object, template_name: str) -> Template object.
    Make a clump template from a clump.
    No clumps refer to the created clump template.
    """
    pass


def maxid(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the maximum clump templates ID.
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

    def add_pebble(self, *args, **kwargs) -> Any:
        """
        (pebble_radius: float, pebble_position: vec [,pebble_id: int]) -> TemplatePebble object.
        Add a pebble to a clump template.
        This operation has no impact on the clump template inertial attributes.
        If the optional argument ID is not specified the id if the newly created pebble is set to the next available number.
        """
        pass

    def clone(self, *args, **kwargs) -> Any:
        """
        (new_template_name: str) -> Template object.
        Clone this clump template.
        The new clump template has name new_template_name and no clumps refer to the created clump template.
        """
        pass

    def delete(self, *args, **kwargs) -> Any:
        """
        () -> None.
        Delete this clump template.
        All clumps that referred to this clump template no longer refer to any clump template.
        """
        pass

    def delete_pebble(self, *args, **kwargs) -> Any:
        """
        (pebble: TemplatePebbel object) -> None.
        Delete a TemplatePebble from this clump.
        This operation has no impact on the clump template inertial attributes.
        The clump no longer refers to a clump template.
        This operation will raise an exception if any clumps refer to the clump template.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the clump template id.
        """
        pass

    def moi(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the clump template moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        """
        pass

    def moi_prin(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump template principal moment of inertia (vector).
        """
        pass

    def moi_prin_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump template principal moment of inertia.
        """
        pass

    def moi_prin_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump template principal moment of inertia.
        """
        pass

    def name(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the clump template name.
        """
        pass

    def orig_pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the clump template original position (vector).
        """
        pass

    def orig_pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the clump template original position.
        """
        pass

    def orig_pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the clump template original position.
        """
        pass

    def pebbles(self, *args, **kwargs) -> Any:
        """
        () -> tuple of TemplatePebble objects.
        Get the pebbles of this clump template.
        """
        pass

    def set_moi(self, *args, **kwargs) -> Any:
        """
        () -> tensor.
        Get the clump template moment of intertia.
        In 2D the polar moment of intertial is used so the return value is a float.
        When modified no other clump attributes are changed (e.g., pebble sizes, clump volume, etc.).
        The specification of the moment of inertia in this way results in the principal moments of inertia being in a fixed state so that they will not be automatically updated when scaling a clump unless the user changes the fix state (see the Clump moi_fix() method).
        """
        pass

    def set_moi_prin(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump template principal moment of inertia (vector).
        """
        pass

    def set_moi_prin_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump template principal moment of inertia.
        """
        pass

    def set_moi_prin_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump template principal moment of inertia.
        """
        pass

    def set_orig_pos(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> None.
        Set the clump template original position (vector).
        """
        pass

    def set_orig_pos_x(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the x-component of the clump template original position.
        """
        pass

    def set_orig_pos_y(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the y-component of the clump template original position.
        """
        pass

    def set_vol(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the clump template volume.
        In 2D this is the volume per unit thickness.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True of this object is a live clump template.
        """
        pass

    def vol(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the clump template volume.
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

import typing
from typing import Any

import itasca.contact


def count(process: str, type_class: type, all: bool) -> typing.Any:
    """
    (<process: str>, <type: TypeObject>, <all=False>) -> int.
    Get the number of contacts.
    All the arguments to this function are optional.
    The first argument is the contact class, this defaults to "mechanical".
    If the (optional) keyword argument type is given the count is limited to that type.
    The type keyword argument should be a Python type object (itasca.BallBallContact, itasca.BallFacetContact, itasca.BallPebbleContact, itasca.PebblePebbleContact or itasca.PebbleFacetContact).
    If the (optional) keyword argument all is given, virtual contacts are included in the count.
    """
    pass


def energy(energy_name: str, process=..., type=...) -> float:
    """
    (energy_name: str, process="mechanical", type=TypeObject) -> float.
    Get energy values accumulated over contacts.
    The first argument should be the name of an energy quantity.
    Two optional keyword arguments are accepted, process which should be a string (defaults to "mechanical") and type which should be a Python contact type object.
    """
    pass


def find(type: Any, id: typing.Union[int, typing.Tuple[typing.Any, typing.Any]]) -> itasca.contact.Contact:
    """
    (type: TypeObject, id: int or (object1, object2)) -> Contact object.
    Get the contact of the given type, the second argument is either an integer ID or a length two tuple containing two objects (for example a wall object and a ball object).
    """
    pass


def list(process_name=..., type=..., all=...) -> itasca.contact.ContactIter:
    """
    (process_name="Mechanical", type=None, all=False) -> Contact iterator object.
    Get a contact iterator object.
    The optional argument is the name of a process, the default is "mechanical".
    If the (optional) keyword argument type is given the returned contacts are limited to that type.
    The type keyword argument should be a Python type object (itasca.BallBallContact, itasca.BallFacetContact, itasca.BallPebbleContact, itasca.PebblePebbleContact or itasca.PebbleFacetContact).
    If the (optional) keyword argument all is given, virtual contacts are also returned.
    """
    pass


def model_prop_index(model_name: str, property_name: str) -> int:
    """
    (model_name: str, property_name: str) -> int.
    Get a contact model property index.
    """
    pass


class Contact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
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


class ContactIter:
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

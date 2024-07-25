import typing


def call_function(func: str, args: typing.Tuple = ...) -> typing.Any:
    """
    (func: string, [(tuple: any)]) -> Any.
    Call FISH function func return result.
    """
    pass


def get(var: str) -> typing.Any:
    """
    (var: string) -> any.
    Return value of the FISH variable var.
    """
    pass


def has(var: str) -> bool:
    """
    (var: string) -> Boolean.
    Return True if the FISH variable var is defined, False otherwise.
    """
    pass


def is_function(var: str) -> bool:
    """
    (var: string) -> Boolean.
    Return True if the FISH variable var is defined and is a function, False otherwise.
    """
    pass


def set(var: str, value: typing.Any) -> None:
    """
    (var: string, value:any) -> None.
    Set the FISH variable var to value.
    If no FISH variable with name var exists, then it is created.
    """
    pass

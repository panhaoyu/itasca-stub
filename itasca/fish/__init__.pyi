from typing import Any

def call_function(*args, **kwargs) -> Any:
    """
    (func: string, [(tuple: any)]) -> Any.
    Call FISH function func return result.
    """
    pass

def get(*args, **kwargs) -> Any:
    """
    (var: string) -> any.
    Return value of the FISH variable var.
    """
    pass

def has(*args, **kwargs) -> Any:
    """
    (var: string) -> Boolean.
    Return True if the FISH variable var is defined, False otherwise.
    """
    pass

def is_function(*args, **kwargs) -> Any:
    """
    (var: string) -> Boolean.
    Return True if the FISH variable var is defined and is a function, False otherwise.
    """
    pass

def set(*args, **kwargs) -> Any:
    """
    (var: string, value:any) -> None.
    Set the FISH variable var to value.
    If no FISH variable with name var exists, then it is created.
    """
    pass


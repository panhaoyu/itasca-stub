from typing import Any

from . import contact
from . import fish
from . import ballarray
from . import clumparray
from . import pebblearray
from . import wallarray
from . import facetarray
from . import vertexarray
from . import ballballarray
from . import ballpebblearray
from . import ballfacetarray
from . import pebblepebblearray
from . import pebblefacetarray
from . import ball
from . import clump
from . import wall
from . import measure
from . import dfn
from . import rblockarray
from . import rblockrblockarray
from . import ballrblockarray
from . import pebblerblockarray
from . import rblockfacetarray
from . import rblock


def _add_control_action(*args, **kwargs) -> Any:
    """
    (QDockWidget Pointer created by dockWidget method, QAction Pointer) -> None.
    Add a control action.
    This action must not be destroyed (or the parent object) or a crash will result.
    """
    pass


def _add_execute_button(*args, **kwargs) -> Any:
    """
    (QDockWidget Pointer created by dockWidget method, Boolean) -> None.
    Add/remove the execute/stop button.
    """
    pass


def _add_polling(*args, **kwargs) -> Any:
    """
    () -> None.
    Activate polling.
    """
    pass


def _ballball_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballballthermal_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballfacet_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballfacetthermal_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballpebble_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballpebblethermal_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballrblock_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _busy(*args, **kwargs) -> Any:
    """
    (state) -> None.
    Inform the GUI of the processing state (True or False).
    """
    pass


def _cycling(*args, **kwargs) -> Any:
    """
    () -> Bool.
    Returns the cycling state.
    """
    pass


def _exception(*args, **kwargs) -> Any:
    """
    (exception text) -> None.
    Throw an engine exception.
    """
    pass


def _exit(*args, **kwargs) -> Any:
    """
    () -> None.
    Quit the application.
    """
    pass


def _finish_execution(*args, **kwargs) -> Any:
    """
    () -> None.
    Called when the IPython console is finished executing Python code.
    """
    pass


def _freelist_stack_pointer(*args, **kwargs) -> Any:
    """
    () -> int.
    Return the Itasca Python object freelist stack pointer.
    """
    pass


def _interrupt_action(*args, **kwargs) -> Any:
    """
    () -> QAction.
    Get the interrupt action.
    """
    pass


def _options_dialog(*args, **kwargs) -> Any:
    """
    (QDockWidget Pointer created by dockWidget method) -> QDialog Pointer.
    Create an options dialog.
    """
    pass


def _options_dialog_toolbox(*args, **kwargs) -> Any:
    """
    (QDialog Pointer created by _options_dialog method) -> QToolBox Pointer.
    Get the QToolBox to which one can add entries.
    """
    pass


def _pebblefacet_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblefacetthermal_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblepebble_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblepebblethermal_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblerblock_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _rblockfacet_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _rblockrblock_plist(*args, **kwargs) -> Any:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _record_error(*args, **kwargs) -> Any:
    """
    (value: string) -> None.
    Mark the last line executed in Python as an error in the record.
    """
    pass


def _remove_polling(*args, **kwargs) -> Any:
    """
    () -> None.
    Deactivate polling.
    """
    pass


def _to_record(*args, **kwargs) -> Any:
    """
    (value: string) -> None.
    Add these commands to the record.
    """
    pass


def command(*args, **kwargs) -> Any:
    """
    (command: string) -> None.
    Issue a command.
    """
    pass


def cycle(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the cycle number.
    """
    pass


def deterministic(*args, **kwargs) -> Any:
    """
    () -> bool.
    Get the deterministic mode.
    In deterministic mode, all model runs starting with identical initial conditions result in identical solutions at the cost of a > 20% reduction in performance.
    In nondeterministic mode, on the other hand, identical initial conditions may lead to divergent solutions.
    The divergence is due only to the order of summation, and all solutions are equally valid to machine precision.
    """
    pass


def dim(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the code dimensionality.
    """
    pass


def dockWidget(*args, **kwargs) -> Any:
    """
    (window name: string, dock location: string, add close controls: bool) -> Pointer to QDockWidget.
    Return a pointer to an empty QDockWidget with the specified attributes.
    One must use shiboken.wrapInstance to access the QDockWidget class through PySide bindings.
    """
    pass


def domain_condition(*args, **kwargs) -> Any:
    """
    (value: string) -> string.
    Get the domain condition given a domain direction.
    Acceptable values are {'x' or 'y' in 2D; 'x', 'y' or 'z' in 3D}.
    """
    pass


def domain_max(*args, **kwargs) -> Any:
    """
    () -> vec.
    Get domain upper bound (vector).
    """
    pass


def domain_max_x(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the x-component of domain upper bound.
    """
    pass


def domain_max_y(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the y-component of domain upper bound.
    """
    pass


def domain_min(*args, **kwargs) -> Any:
    """
    () -> vec.
    Get domain lower bound (vector).
    """
    pass


def domain_min_x(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the x-component of domain lower bound.
    """
    pass


def domain_min_y(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the y-component of domain lower bound.
    """
    pass


def domain_strain_rate(*args, **kwargs) -> Any:
    """
    () -> tens3.
    Get the domain strain-rate tensor.
    """
    pass


def fos(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the factor of safety.
    """
    pass


def gravity(*args, **kwargs) -> Any:
    """
    () -> vec.
    Get the gravity (vector).
    """
    pass


def gravity_x(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the x-component of the gravity.
    """
    pass


def gravity_y(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the y-component of the gravity.
    """
    pass


def mainWindow(*args, **kwargs) -> Any:
    """
    () -> QMainWindow.
    Get the string pointer address of the QMainWindow.
    """
    pass


def mech_age(*args, **kwargs) -> Any:
    """
    () -> float.
    Return the accumulated mechanical time.
    """
    pass


def remove_callback(*args, **kwargs) -> Any:
    """
    (function_name: str, call_point: float or str) -> None.
    Remove a python function from the callback system.
    The first argument is the string name of a function and the second argument can either be a float (which gives the location in the cycling sequence) or a string corresponding to one of the pre-defined callback events.
    """
    pass


def set_callback(*args, **kwargs) -> Any:
    """
    (function_name: str, call_point: float or str) -> None.
    Register a python function to be called during the cycling sequence.
    The first argument is the string name of a function and the second argument can either be a float (which gives the location in the cycling sequence) or a string corresponding to one of the pre-defined callback events.
    A function of the given name should exist in the __main__ python namespace and should be callable with any number of arguments.
    """
    pass


def set_deterministic(*args, **kwargs) -> Any:
    """
    (value: bool) -> None.
    Set the deterministic mode.
    In deterministic mode, all model runs starting with identical initial conditions result in identical solutions at the cost of a > 20% reduction in performance.
    In nondeterministic mode, on the other hand, identical initial conditions may lead to divergent solutions.
    The divergence is due only to the order of summation, and all solutions are equally valid to machine precision.
    """
    pass


def set_domain_condition(*args, **kwargs) -> Any:
    """
    (direction: string, condition: string) -> None.
    Set the domain condition for a given domain direction.
    Acceptable values of the domain direction are {'x' or 'y' in 2D; 'x', 'y' or 'z' in 3D}.
    Acceptable conditions are 'destroy', 'periodic', 'reflect' and 'stop'.
    """
    pass


def set_domain_max(*args, **kwargs) -> Any:
    """
    (value: vec) -> None.
    Set domain upper bound (vector).
    """
    pass


def set_domain_max_x(*args, **kwargs) -> Any:
    """
    (value: float) -> None.
    Set the x-component of domain upper bound.
    """
    pass


def set_domain_max_y(*args, **kwargs) -> Any:
    """
    (value: float) -> None.
    Set the y-component of domain upper bound.
    """
    pass


def set_domain_min(*args, **kwargs) -> Any:
    """
    (value: vec) -> None.
    Set domain lower bound (vector).
    """
    pass


def set_domain_min_x(*args, **kwargs) -> Any:
    """
    (value: float) -> None.
    Set the x-component of domain lower bound.
    """
    pass


def set_domain_min_y(*args, **kwargs) -> Any:
    """
    (value: float) -> None.
    Set the y-component of domain lower bound.
    """
    pass


def set_domain_strain_rate(*args, **kwargs) -> Any:
    """
    (stress: tens3) -> None.
    Set the domain strain-rate tensor.
    """
    pass


def set_gravity(*args, **kwargs) -> Any:
    """
    (value: vec) -> None.
    Set the gravity (vector).
    """
    pass


def set_gravity_x(*args, **kwargs) -> Any:
    """
    (value: float) -> None.
    Set the x-component of the gravity.
    """
    pass


def set_gravity_y(*args, **kwargs) -> Any:
    """
    (value: float) -> None.
    Set the y-component of the gravity.
    """
    pass


def set_threads(*args, **kwargs) -> Any:
    """
    (value: int) -> None.
    Set the number of threads.
    """
    pass


def state_callbacks(*args, **kwargs) -> Any:
    """
    () -> dict {any: tuple of str}.
    Return a dictionary of the currently defined Python new, save and restore callback events.
    The return value is a dictionary, the keys are the callback points and the values are tuples of Python function names given as strings.
    """
    pass


def threads(*args, **kwargs) -> Any:
    """
    () -> int.
    Get the number of threads.
    """
    pass


def timestep(*args, **kwargs) -> Any:
    """
    () -> float.
    Get the global timestep.
    """
    pass


class BallBallContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, *args, **kwargs) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class BallBallContactIter:
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


class BallBallThermalContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, *args, **kwargs) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class BallBallThermalContactIter:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
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


class BallFacetContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class BallFacetContactIter:
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


class BallFacetThermalContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class BallFacetThermalContactIter:
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


class BallPebbleContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class BallPebbleContactIter:
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


class BallPebbleThermalContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class BallPebbleThermalContactIter:
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


class BallRBlockContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class BallRBlockContactIter:
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


class PebbleFacetContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class PebbleFacetContactIter:
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


class PebbleFacetThermalContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class PebbleFacetThermalContactIter:
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


class PebblePebbleContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class PebblePebbleContactIter:
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


class PebblePebbleThermalContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, *args, **kwargs) -> Any:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class PebblePebbleThermalContactIter:
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


class PebbleRBlockContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class PebbleRBlockContactIter:
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


class RBlockFacetContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class RBlockFacetContactIter:
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


class RBlockRBlockContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def branch(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self, *args, **kwargs) -> Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, *args, **kwargs) -> Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, *args, **kwargs) -> Any:
        """
        ([slot: str]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, *args, **kwargs) -> Any:
        """
        (group_name: str) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self, *args, **kwargs) -> Any:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self, *args, **kwargs) -> Any:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, *args, **kwargs) -> Any:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args: dict = None) -> Any:
        """
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self, *args, **kwargs) -> Any:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self, *args, **kwargs) -> Any:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, *args, **kwargs) -> Any:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, *args, **kwargs) -> Any:
        """
        (group_name: str[, slot: str]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, *args, **kwargs) -> Any:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, *args, **kwargs) -> Any:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, *args, **kwargs) -> Any:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, *args, **kwargs) -> Any:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self, *args, **kwargs) -> Any:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self, *args, **kwargs) -> Any:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, *args, **kwargs) -> Any:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self, *args, **kwargs) -> Any:
        """
        () -> bool.
        Returns True if this contact is live.
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


class RBlockRBlockContactIter:
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

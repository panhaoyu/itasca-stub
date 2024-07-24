import typing
from typing import Any

import PySide2.QtWidgets
import vec

from . import ball
from . import ballarray
from . import ballballarray
from . import ballfacetarray
from . import ballpebblearray
from . import ballrblockarray
from . import clump
from . import clumparray
from . import contact
from . import facetarray
from . import fish
from . import history
from . import measure
from . import pebblearray
from . import pebblefacetarray
from . import pebblepebblearray
from . import pebblerblockarray
from . import rblock
from . import rblockarray
from . import rblockfacetarray
from . import rblockrblockarray
from . import vertexarray
from . import wall
from . import wallarray


def _add_control_action(QDockWidget_Pointer_created_by_dockWidget_method, QAction_Pointer) -> None:
    """
    (QDockWidget Pointer created by dockWidget method, QAction Pointer) -> None.
    Add a control action.
    This action must not be destroyed (or the parent object) or a crash will result.
    """
    pass


def _add_execute_button(QDockWidget_Pointer_created_by_dockWidget_method, Boolean) -> None:
    """
    (QDockWidget Pointer created by dockWidget method, Boolean) -> None.
    Add/remove the execute/stop button.
    """
    pass


def _add_polling() -> None:
    """
    () -> None.
    Activate polling.
    """
    pass


def _ballball_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballballthermal_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballfacet_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballfacetthermal_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballpebble_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballpebblethermal_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _ballrblock_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _busy(state) -> None:
    """
    (state) -> None.
    Inform the GUI of the processing state (True or False).
    """
    pass


def _cycling() -> bool:
    """
    () -> Bool.
    Returns the cycling state.
    """
    pass


def _exception(exception_text) -> None:
    """
    (exception text) -> None.
    Throw an engine exception.
    """
    pass


def _exit() -> None:
    """
    () -> None.
    Quit the application.
    """
    pass


def _finish_execution() -> None:
    """
    () -> None.
    Called when the IPython console is finished executing Python code.
    """
    pass


def _freelist_stack_pointer() -> int:
    """
    () -> int.
    Return the Itasca Python object freelist stack pointer.
    """
    pass


def _interrupt_action() -> PySide2.QtWidgets.QAction:
    """
    () -> QAction.
    Get the interrupt action.
    """
    pass


def _options_dialog(QDockWidget_Pointer_created_by_dockWidget_method) -> PySide2.QtWidgets.QDialog:
    """
    (QDockWidget Pointer created by dockWidget method) -> QDialog Pointer.
    Create an options dialog.
    """
    pass


def _pebblefacet_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblefacetthermal_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblepebble_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblepebblethermal_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _pebblerblock_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _rblockfacet_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _rblockrblock_plist() -> typing.Tuple[object, ...]:
    """
    () -> tuple of PyObject pointers for the currenly in-scope and valid objects.
    This function is used for internal testing and is not needed for general PFC use.
    """
    pass


def _record_error(value: str) -> None:
    """
    (value: string) -> None.
    Mark the last line executed in Python as an error in the record.
    """
    pass


def _remove_polling() -> None:
    """
    () -> None.
    Deactivate polling.
    """
    pass


def _to_record(value: str) -> None:
    """
    (value: string) -> None.
    Add these commands to the record.
    """
    pass


def add_save_variable(variable_name: str) -> None:
    """
    (variable_name: string) -> None.
    Add the name of Python variable name to the list of variables to be saved in the save file.
    """
    pass


def clear_save_variables() -> None:
    """
    () -> None.
    Clear the list of names of the Python variables to be saved in the save file.
    """
    pass


def command(command: str) -> None:
    """
    (command: string) -> None.
    Issue a command.
    """
    pass


def cycle() -> int:
    """
    () -> int.
    Get the cycle number.
    """
    pass


def deterministic() -> bool:
    """
    () -> bool.
    Get the deterministic mode.
    In deterministic mode, all model runs starting with identical initial conditions result in identical solutions at the cost of a > 20% reduction in performance.
    In nondeterministic mode, on the other hand, identical initial conditions may lead to divergent solutions.
    The divergence is due only to the order of summation, and all solutions are equally valid to machine precision.
    """
    pass


def dim() -> int:
    """
    () -> int.
    Get the code dimensionality.
    """
    pass


def dockWidget(window_name: str, dock_location: str, add_close_controls: bool) -> PySide2.QtWidgets.QDockWidget:
    """
    (window name: string, dock location: string, add close controls: bool) -> Pointer to QDockWidget.
    Return a pointer to an empty QDockWidget with the specified attributes.
    One must use shiboken.wrapInstance to access the QDockWidget class through PySide bindings.
    """
    pass


def domain_condition(value: str) -> str:
    """
    (value: string) -> string.
    Get the domain condition given a domain direction.
    Acceptable values are {'x' or 'y' in 2D; 'x', 'y' or 'z' in 3D}.
    """
    pass


def domain_max() -> vec.vec:
    """
    () -> vec.
    Get domain upper bound (vector).
    """
    pass


def domain_max_x() -> float:
    """
    () -> float.
    Get the x-component of domain upper bound.
    """
    pass


def domain_max_y() -> float:
    """
    () -> float.
    Get the y-component of domain upper bound.
    """
    pass


def domain_min() -> vec.vec:
    """
    () -> vec.
    Get domain lower bound (vector).
    """
    pass


def domain_min_x() -> float:
    """
    () -> float.
    Get the x-component of domain lower bound.
    """
    pass


def domain_min_y() -> float:
    """
    () -> float.
    Get the y-component of domain lower bound.
    """
    pass


def domain_strain_rate() -> vec.tens3:
    """
    () -> tens3.
    Get the domain strain-rate tensor.
    """
    pass


def fos() -> float:
    """
    () -> float.
    Get the factor of safety.
    """
    pass


def get_save_variables() -> typing.Tuple[str, ...]:
    """
    () -> tuple of str.
    Get the names of the Python variables to be saved in the save file.
    """
    pass


def gravity() -> vec.vec:
    """
    () -> vec.
    Get the gravity (vector).
    """
    pass


def gravity_x() -> float:
    """
    () -> float.
    Get the x-component of the gravity.
    """
    pass


def gravity_y() -> float:
    """
    () -> float.
    Get the y-component of the gravity.
    """
    pass


def group(group_name: str) -> int:
    """
    (group_name: str) -> int.
    Return the group index associated with a given group name.
    A group index can be used instead of a string for faster execution.
    """
    pass


def mainWindow() -> PySide2.QtWidgets.QMainWindow:
    """
    () -> QMainWindow.
    Get the string pointer address of the QMainWindow.
    """
    pass


def mech_age() -> float:
    """
    () -> float.
    Return the accumulated mechanical time.
    """
    pass


def remove_callback(function_name: str, call_point: typing.Union[float, str]) -> None:
    """
    (function_name: str, call_point: float or str) -> None.
    Remove a python function from the callback system.
    The first argument is the string name of a function and the second argument can either be a float (which gives the location in the cycling sequence) or a string corresponding to one of the pre-defined callback events.
    """
    pass


def remove_save_variable(variable_name: str) -> None:
    """
    (variable_name: string) -> None.
    Remove the name of the Python variable from the list of variables to be saved in the save file.
    """
    pass


def set_callback(function_name: str, call_point: typing.Union[float, str]) -> None:
    """
    (function_name: str, call_point: float or str) -> None.
    Register a python function to be called during the cycling sequence.
    The first argument is the string name of a function and the second argument can either be a float (which gives the location in the cycling sequence) or a string corresponding to one of the pre-defined callback events.
    A function of the given name should exist in the __main__ python namespace and should be callable with any number of arguments.
    """
    pass


def set_deterministic(value: bool) -> None:
    """
    (value: bool) -> None.
    Set the deterministic mode.
    In deterministic mode, all model runs starting with identical initial conditions result in identical solutions at the cost of a > 20% reduction in performance.
    In nondeterministic mode, on the other hand, identical initial conditions may lead to divergent solutions.
    The divergence is due only to the order of summation, and all solutions are equally valid to machine precision.
    """
    pass


def set_domain_condition(direction: str, condition: str) -> None:
    """
    (direction: string, condition: string) -> None.
    Set the domain condition for a given domain direction.
    Acceptable values of the domain direction are {'x' or 'y' in 2D; 'x', 'y' or 'z' in 3D}.
    Acceptable conditions are 'destroy', 'periodic', 'reflect' and 'stop'.
    """
    pass


def set_domain_max(value: vec.vec) -> None:
    """
    (value: vec) -> None.
    Set domain upper bound (vector).
    """
    pass


def set_domain_max_x(value: float) -> None:
    """
    (value: float) -> None.
    Set the x-component of domain upper bound.
    """
    pass


def set_domain_max_y(value: float) -> None:
    """
    (value: float) -> None.
    Set the y-component of domain upper bound.
    """
    pass


def set_domain_min(value: vec.vec) -> None:
    """
    (value: vec) -> None.
    Set domain lower bound (vector).
    """
    pass


def set_domain_min_x(value: float) -> None:
    """
    (value: float) -> None.
    Set the x-component of domain lower bound.
    """
    pass


def set_domain_min_y(value: float) -> None:
    """
    (value: float) -> None.
    Set the y-component of domain lower bound.
    """
    pass


def set_domain_strain_rate(stress: vec.tens3) -> None:
    """
    (stress: tens3) -> None.
    Set the domain strain-rate tensor.
    """
    pass


def set_gravity(value: vec.vec) -> None:
    """
    (value: vec) -> None.
    Set the gravity (vector).
    """
    pass


def set_gravity_x(value: float) -> None:
    """
    (value: float) -> None.
    Set the x-component of the gravity.
    """
    pass


def set_gravity_y(value: float) -> None:
    """
    (value: float) -> None.
    Set the y-component of the gravity.
    """
    pass


def set_threads(value: int) -> None:
    """
    (value: int) -> None.
    Set the number of threads.
    """
    pass


def slot(slot_name: str) -> int:
    """
    (slot_name: str) -> int.
    Return the slot index associated with a given group name.
    A slot index can be used instead of a string for faster execution.
    """
    pass


def state_callbacks() -> typing.Dict[typing.Any, typing.Tuple[str, ...]]:
    """
    () -> dict {any: tuple of str}.
    Return a dictionary of the currently defined Python new, save and restore callback events.
    The return value is a dictionary, the keys are the callback points and the values are tuples of Python function names given as strings.
    """
    pass


def threads() -> int:
    """
    () -> int.
    Get the number of threads.
    """
    pass


def timestep() -> float:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot: int = ...) -> str:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name: str) -> int:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name: str) -> bool:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self) -> float:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, group_name: str = ..., slot: int = ...) -> None:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self) -> bool:
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


class BallFacetContact:
    __hash__: Any = ...

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.
         See help(type) for accurate signature.
        """
        pass

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot: int = ...) -> str:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name: str) -> int:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name: str) -> bool:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self) -> float:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, group_name: str = ..., slot: int = ...) -> None:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot: int = ...) -> str:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name: str) -> int:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name: str) -> bool:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self) -> float:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, group_name: str = ..., slot: int = ...) -> None:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot: int = ...) -> str:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name: str) -> int:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name: str) -> bool:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self) -> float:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, group_name: str = ..., slot: int = ...) -> None:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot: int = ...) -> str:
        """
        ([slot: int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name: str) -> int:
        """
        (group_name: str ) -> int.
        Remove from the given group from the contact.
        One argument of type string, giving the group name, is required.
        The return value is an integer which is the first slot in which the group name was found or -1 if not found.
        """
        pass

    def groups(self) -> typing.Tuple[str, ...]:
        """
        () -> tuple of strings.
        Get a tuple of group names assigned to this contact.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name: str) -> bool:
        """
        (group_name: str) -> bool.
        Test if the contact is part of a given group.
        All group slots are searched.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def power(self) -> float:
        """
        () -> float.
        Get the contact power.
        """
        pass

    def prop(self, property_name: str) -> typing.Any:
        """
        (property_name: str) -> any.
        Get a contact model property.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_group(self, group_name: str = ..., slot: int = ...) -> None:
        """
        ([group_name: str[, slot: int]]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_power(self, value: float) -> None:
        """
        (value: float) -> None.
        Set the contact power.
        """
        pass

    def set_prop(self, property_name: str, value: typing.Any) -> None:
        """
        (property_name: str, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

    def activate(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def activated(self) -> bool:
        """
        () -> bool.
        Get the contact activated state.
        If a contact has been activated it is always active.
        """
        pass

    def active(self) -> bool:
        """
        () -> bool.
        Get the contact activity state.
        """
        pass

    def bonded(self) -> bool:
        """
        () -> bool.
        Get the contact bonded flag.
        """
        pass

    def branch(self) -> vec.vec:
        """
        () -> vec.
        Get the contact branch vector in the global coordinate system (vector).
        """
        pass

    def branch_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact branch vector in the global coordinate system.
        """
        pass

    def branch_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact branch vector in the global coordinate system.
        """
        pass

    def end1(self) -> typing.Any:
        """
        () -> any.
        Get the object at the first end of this contact.
        """
        pass

    def end2(self) -> typing.Any:
        """
        () -> any.
        Get the object at the second end of this contact.
        """
        pass

    def energies(self) -> typing.Dict[str, float]:
        """
        () -> dict {str: float}.
        Get the energy partitions as a dictionary.
        """
        pass

    def energy(self, energy_name: str) -> float:
        """
        (energy_name: str) -> float.
        Get the current value of an energy partition.
        """
        pass

    def extra(self, slot: int) -> typing.Any:
        """
        (slot: int) -> any.
        Get the contact extra data in the given slot.
        """
        pass

    def fid(self) -> int:
        """
        () -> int.
        Get the contact fracture ID.
        """
        pass

    def force_global(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the global coordinate system (vector).
        """
        pass

    def force_global_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the global coordinate system.
        """
        pass

    def force_global_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the global coordinate system.
        """
        pass

    def force_local(self) -> vec.vec:
        """
        () -> vec.
        Get the contact force in the local coordinate system (vector).
        """
        pass

    def force_local_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact force in the local coordinate system.
        """
        pass

    def force_local_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact force in the local coordinate system.
        """
        pass

    def force_normal(self) -> float:
        """
        () -> float.
        Get the contact signed magnitude of the normal force.
        """
        pass

    def force_shear(self) -> float:
        """
        () -> float.
        Get the contact magnitude of the shear force.
        """
        pass

    def gap(self) -> float:
        """
        () -> float.
        Get the contact gap.
        """
        pass

    def group(self, slot=...) -> str:
        """
        ([slot: str or int]) -> str.
        Get the contact group name in a given slot.
        """
        pass

    def group_remove(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Remove from the given group from all group slots of the contact.
        One argument of type string, giving the group name, is required.
        The return value is a bool which is True if the group was removed from any slot, otherwise False.
        """
        pass

    def groups(self) -> typing.Dict[typing.Union[str, int], str]:
        """
        () -> {slot: group_name}.
        Get a dictionary describing which groups this contact is part of.
        The keys of the dictionary are the slot names and the values are the group names.
        """
        pass

    def has_prop(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Query the existence of a contact model property.
        A single string argument is required.
        """
        pass

    def id(self) -> int:
        """
        () -> int.
        Get the contact id.
        """
        pass

    def in_group(self, group_name, slot=...) -> bool:
        """
        (group_name: str or int[, slot: str or int]) -> bool.
        Test if the contact is part of a given group.
        If the optional argument slot is given, only that slot is searched.
        Otherwise, all group slots are searched.
        """
        pass

    def inherit(self, property_name: str) -> bool:
        """
        (property_name: str) -> bool.
        Get the property inheritance.
        """
        pass

    def inhibit(self) -> bool:
        """
        () -> bool.
        Get the contact inhibit flag.
        """
        pass

    def is_energy(self, energy_name: str) -> bool:
        """
        (energy_name: str) -> bool.
        Query the existence of a contact model energy.
        """
        pass

    def method(self, method_name: str, args=...) -> None:
        """
        (method_name: str <, args: dict {str: any}>) -> None.
        Execute a contact model method.
        The first argument must be a string identifying a method that exists in the contact model assigned to the contact.
        The optional second argument should be a dictionary with string keys which give the contact model method arguments (the values associated with the string keys are the arguments).
        """
        pass

    def model(self) -> str:
        """
        () -> str.
        Get the contact model name.
        """
        pass

    def moment1_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the global coordinate system.
        """
        pass

    def moment1_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end1 in the local coordinate system.
        """
        pass

    def moment2_global(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the global coordinate system.
        """
        pass

    def moment2_local(self) -> float:
        """
        () -> float.
        Get the contact moment acting on end2 in the local coordinate system.
        """
        pass

    def normal(self) -> vec.vec:
        """
        () -> vec.
        Get the contact unit normal (vector).
        """
        pass

    def normal_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact unit normal.
        """
        pass

    def normal_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact unit normal.
        """
        pass

    def offset(self) -> vec.vec:
        """
        () -> vec.
        Get the contact offset (vector).
        """
        pass

    def offset_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact offset.
        """
        pass

    def offset_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact offset.
        """
        pass

    def persist(self) -> bool:
        """
        () -> bool.
        Get the contact persistence flag.
        """
        pass

    def pos(self) -> vec.vec:
        """
        () -> vec.
        Get the contact position (vector).
        """
        pass

    def pos_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact position.
        """
        pass

    def pos_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact position.
        """
        pass

    def prop(self, property_name_or_index) -> typing.Any:
        """
        (property_name or index: str or int) -> any.
        Get a contact model property.
        """
        pass

    def prop_index(self, property_name: str) -> int:
        """
        (property_name: str) -> int.
        Get a contact model property index.
        """
        pass

    def props(self) -> typing.Dict[str, typing.Any]:
        """
        () -> dict {str: any}.
        Get the contact model properties as a dictionary.
        """
        pass

    def set_extra(self, slot: int, value: typing.Any) -> None:
        """
        (slot: int, value: any) -> None.
        Set the contact extra data in the given slot.
        """
        pass

    def set_force(self, value: vec.vec) -> None:
        """
        (value: vec) -> None.
        Set the contact model force.
        This operation is contact model specific.
        """
        pass

    def set_group(self, group_name, slot=...) -> None:
        """
        (group_name: str or int[, slot: str or int]) -> None.
        Set the contact group name in a given slot.
        """
        pass

    def set_inherit(self, property_name: str, inherit_flag: bool) -> None:
        """
        (property_name: str, inherit_flag: bool) -> None.
        Set the property inheritance.
        """
        pass

    def set_inhibit(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact inhibit flag.
        """
        pass

    def set_model(self, model_name: str = ...) -> None:
        """
        ([model_name: str]) -> None.
        Set the contact model for this contact.
        """
        pass

    def set_persist(self, flag: bool) -> None:
        """
        (flag: bool) -> None.
        Set the contact persistence flag.
        """
        pass

    def set_prop(self, property_name_or_index, value: typing.Any) -> None:
        """
        (property_name or index: str or int, value: any) -> None.
        Set a contact model property.
        """
        pass

    def shear(self) -> vec.vec:
        """
        () -> vec.
        Get the contact shear direction (vector).
        """
        pass

    def shear_x(self) -> float:
        """
        () -> float.
        Get the x-component of the contact shear direction.
        """
        pass

    def shear_y(self) -> float:
        """
        () -> float.
        Get the y-component of the contact shear direction.
        """
        pass

    def to_global(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the local to the global coordinate system.
        (vector).
        """
        pass

    def to_local(self, value: vec.vec) -> vec.vec:
        """
        (value: vec) -> vec.
        Transform a vector from the global to the local coordinate system.
        (vector).
        """
        pass

    def valid(self) -> bool:
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

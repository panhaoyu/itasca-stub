import numpy


def create(radii: numpy.ndarray, centroids: numpy.ndarray, **kwds) -> numpy.ndarray:
    """
    (radii: array float{ball}, centroids: array float{ball,dim}, **kwds) -> array int{ball} IDs of the newly created balls.
    Create balls from two arrays.
    The first array must contain the radii, and the second array the positions.
    The arrays must be the correct shape.
    Additional keyword arguments can be specified which will set the newly created ball attributes.
    The keyword arguments values can be scalars, vecs or arrays of 1 or two dimensions.
    The keyword argument props can be used to set ball properties, the value should be a dict of type {str: value}.
    The keyword argument extra can be used to set extra variables, the value should be a dict of type {int: value}.
    The props or extra dictionary values can be a 1 or 2 dimensional array of doubles, a number, a vec or a string.
    """
    pass


def damp() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball local damping.
    """
    pass


def density() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball density.
    """
    pass


def disp() -> numpy.ndarray:
    """
    () -> array float{ball,2}.
    Get a numpy array of the ball displacement.
    """
    pass


def extra(slot: int) -> numpy.ndarray:
    """
    (slot: int) -> array float{ball} or float{ball}.
    Get the ball extra data in the given slot as an array.
    Extra variables accessed by array must be of type float or vec.
    """
    pass


def fill_damp(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball local damping.
    The array must be the correct shape.
    """
    pass


def fill_density(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball density.
    The array must be the correct shape.
    """
    pass


def fill_disp(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Fill an existing array with the ball displacement.
    The array must be the correct shape.
    """
    pass


def fill_force_app(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Fill an existing array with the ball applied force.
    The array must be the correct shape.
    """
    pass


def fill_force_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Fill an existing array with the ball contact force.
    The array must be the correct shape.
    """
    pass


def fill_force_unbal(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Fill an existing array with the ball unbalanced force.
    The array must be the correct shape.
    """
    pass


def fill_mass(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the inertial ball mass.
    The array must be the correct shape.
    """
    pass


def fill_mass_real(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the real (gravitational) ball mass.
    The array must be the correct shape.
    """
    pass


def fill_moment_app(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball applied moment.
    The array must be the correct shape.
    """
    pass


def fill_moment_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball contact moment.
    The array must be the correct shape.
    """
    pass


def fill_moment_unbal(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball unbalanced moment.
    The array must be the correct shape.
    """
    pass


def fill_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Fill an existing array with the ball centroid location.
    The array must be the correct shape.
    """
    pass


def fill_radius(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball radii.
    The array must be the correct shape.
    """
    pass


def fill_rotation(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball orientation.
    The array must be the correct shape.
    """
    pass


def fill_spin(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Fill an existing array with the ball angular velocity.
    The array must be the correct shape.
    """
    pass


def fill_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Fill an existing array with the ball velocity.
    The array must be the correct shape.
    """
    pass


def force_app() -> numpy.ndarray:
    """
    () -> array float{ball,2}.
    Get a numpy array of the ball applied force.
    """
    pass


def force_contact() -> numpy.ndarray:
    """
    () -> array float{ball,2}.
    Get a numpy array of the ball contact force.
    """
    pass


def force_unbal() -> numpy.ndarray:
    """
    () -> array float{ball,2}.
    Get a numpy array of the ball unbalanced force.
    """
    pass


def ids() -> numpy.ndarray:
    """
    () -> array int{ball}.
    Get the ball ids as an array.
    """
    pass


def in_group(group_name: str, slot=...) -> numpy.ndarray:
    """
    (group_name: str, slot=1) -> array bool{ball}.
    Return ball group membership as a Boolean array.
    """
    pass


def mass() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the inertial ball mass.
    """
    pass


def mass_real() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the real (gravitational) ball mass.
    """
    pass


def moment_app() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball applied moment.
    """
    pass


def moment_contact() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball contact moment.
    """
    pass


def moment_unbal() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball unbalanced moment.
    """
    pass


def pos() -> numpy.ndarray:
    """
    () -> array float{ball,2}.
    Get a numpy array of the ball centroid location.
    """
    pass


def radius() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball radii.
    """
    pass


def rotation() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball orientation.
    """
    pass


def set_damp(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Set the ball local damping from an array.
    """
    pass


def set_density(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Set the ball density from an array.
    """
    pass


def set_disp(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Set the ball displacement from an array.
    """
    pass


def set_extra(slot: int, data: numpy.ndarray) -> None:
    """
    (slot: int, data: array float{ball} or float{ball}) -> None.
    Set the ball extra data in the given slot with an array.
    Extra variables set by array must be of type float or vec.
    """
    pass


def set_force_app(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Set the ball applied force from an array.
    """
    pass


def set_force_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Set the ball contact force from an array.
    """
    pass


def set_group(membership: numpy.ndarray, group_name: str, slot=...) -> None:
    """
    (membership: array bool{ball}, group_name: str, slot=1) -> None.
    Set ball group from an array.
    Where membership True set the corresponding ball to be a member of group group_name in the given slot.
    """
    pass


def set_moment_app(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Set the ball applied moment from an array.
    """
    pass


def set_moment_contact(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Set the ball contact moment from an array.
    """
    pass


def set_pos(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Set the ball centroid location from an array.
    """
    pass


def set_radius(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Set the ball radii from an array.
    """
    pass


def set_rotation(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Set the ball orientation from an array.
    """
    pass


def set_spin(data: numpy.ndarray) -> None:
    """
    (data: array float{ball}) -> None.
    Set the ball angular velocity from an array.
    """
    pass


def set_vel(data: numpy.ndarray) -> None:
    """
    (data: array float{ball,2}) -> None.
    Set the ball velocity from an array.
    """
    pass


def spin() -> numpy.ndarray:
    """
    () -> array float{ball}.
    Get a numpy array of the ball angular velocity.
    """
    pass


def vel() -> numpy.ndarray:
    """
    () -> array float{ball,2}.
    Get a numpy array of the ball velocity.
    """
    pass

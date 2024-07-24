#!/usr/bin/env python3
"""Stub generator for C modules.
The public interface is via the mypy.stubgen module.
"""

import inspect
import os.path
import re
from types import ModuleType
from typing import List, Dict, Tuple, Optional, Mapping, Any, Set

from mypy.moduleinspect import is_c_module
from mypy.stubdoc import (
    infer_prop_type_from_docstring, ArgSig,
    infer_arg_sig_from_anon_docstring, FunctionSig
)


def generate_stub_for_c_module(module: ModuleType,
                               target: str,
                               sigs: Optional[Dict[str, str]] = None,
                               class_sigs: Optional[Dict[str, str]] = None,
                               other_import: List[str] = None) -> None:
    """Generate stub for C module.
    This combines simple runtime introspection (looking for docstrings and attributes
    with simple builtin types) and signatures inferred from .rst documentation (if given).
    If directory for target doesn't exist it will be created. Existing stub
    will be overwritten.
    """
    assert is_c_module(module), '%s is not a C module' % module
    subdir = os.path.dirname(target)
    if subdir and not os.path.isdir(subdir):
        os.makedirs(subdir)
    imports = []  # type: List[str]
    functions = []  # type: List[str]
    done = set()
    items = sorted(module.__dict__.items(), key=lambda x: x[0])
    for name, obj in items:
        if is_c_function(obj):
            generate_c_function_stub(module, name, obj, functions, imports=imports, sigs=sigs)
            done.add(name)
    types = []  # type: List[str]
    for name, obj in items:
        if name.startswith('__') and name.endswith('__'):
            continue
        if is_c_type(obj):
            generate_c_type_stub(module, name, obj, types, imports=imports, sigs=sigs,
                                 class_sigs=class_sigs)
            done.add(name)
    variables = []
    for name, obj in items:
        if name.startswith('__') and name.endswith('__'):
            continue
        if name not in done and not inspect.ismodule(obj):
            type_str = type(obj).__name__
            if type_str not in ('int', 'str', 'bytes', 'float', 'bool'):
                type_str = 'Any'
            variables.append('%s: %s' % (name, type_str))
    output = []
    for other_module in other_import:
        output.append('from . import {}'.format(other_module))
    for line in sorted(set(imports)):
        output.append(line)
    for line in variables:
        output.append(line)
    if output and functions:
        output.append('')
    for line in functions:
        output.append(line)
    for line in types:
        if line.startswith('class') and output and output[-1]:
            output.append('')
        output.append(line)
    output = add_typing_import(output)
    with open(target, 'w') as file:
        for line in output:
            file.write('%s\n' % line)


def add_typing_import(output: List[str]) -> List[str]:
    """Add typing imports for collections/types that occur in the generated stub."""
    names = []
    for name in ['Any', 'Union', 'Tuple', 'Optional', 'List', 'Dict']:
        if any(re.search(r'\b%s\b' % name, line) for line in output):
            names.append(name)
    if names:
        return ['from typing import %s' % ', '.join(names), ''] + output
    else:
        return output[:]


def is_c_function(obj: object) -> bool:
    return inspect.isbuiltin(obj) or type(obj) is type(ord)


def is_c_method(obj: object) -> bool:
    return inspect.ismethoddescriptor(obj) or type(obj) in (type(str.index),
                                                            type(str.__add__),
                                                            type(str.__new__))


def is_c_classmethod(obj: object) -> bool:
    return inspect.isbuiltin(obj) or type(obj).__name__ in ('classmethod',
                                                            'classmethod_descriptor')


def is_c_property(obj: object) -> bool:
    return inspect.isdatadescriptor(obj) and hasattr(obj, 'fget')


def is_c_property_readonly(prop: Any) -> bool:
    return prop.fset is None


def is_c_type(obj: object) -> bool:
    return inspect.isclass(obj) or type(obj) is type(int)


def get_type_str(type_str):
    return_type_dict = {
        '': 'None',
        'none': 'None',
        'any': 'typing.Any',
        'numpy array': 'numpy.ndarray',
        'int': 'int',
        'float': 'float',
        'double': 'float',
        'bool': 'bool',
        'boolean': 'bool',
        'string': 'str',
        'str': 'str',
        'vec': 'vec.vec',
        'tens3': 'vec.tens3',
        'float or str': 'typing.Union[float, str]',
        'int or str': 'typing.Union[int, str]',
        'facet object': 'itasca.wall.facet.Facet',
        'qaction': 'PySide2.QtWidgets.QAction',
        'qdialog pointer': 'PySide2.QtWidgets.QDialog',
        'pointer to qdockwidget': 'PySide2.QtWidgets.QDockWidget',
        'qmainwindow': 'PySide2.QtWidgets.QMainWindow',
        'dict {any: tuple of str}': 'typing.Dict[typing.Any, typing.Tuple[str, ...]]',
        'typeobject': 'type',
        'contact object': 'itasca.contact.Contact',
        'contact iterator object': 'itasca.contact.ContactIter',
        'ball object': 'itasca.ball.Ball',
        'ball iterator object': 'itasca.ball.BallIter',
        'thermal ball object': 'itasca.ball.thermal.ThermalBall',
        'thermal ball iterator object': 'itasca.ball.thermal.ThermalBallIter',
        'clump object': 'itasca.clump.Clump',
        'clump object iterator': 'itasca.clump.ClumpIter',
        'template object': 'itasca.template.Template',
        'pebble object': 'itasca.clump.pebble.Pebble',
        'pebble iterator object': 'itasca.clump.pebble.PebbleIter',
        'thermal clump object': 'itasca.clump.thermal.ThermalClump',
        'thermal clump iterator object': 'itasca.clump.thermal.ThermalClumpIter',
        'thermal pebble object': 'itasca.clump.pebble.thermal.ThermalPebble',
        'thermal pebble iterator object': 'itasca.clump.pebble.thermal.ThermalPebbleIter',
        'wall object': 'itasca.wall.Wall',
        'wall object iterator': 'itasca.wall.WallIter',
        'facet iterator object': 'itasca.wall.facet.FacetIter',
        'wallvertex object': 'itasca.wall.WallVertex',
        'wallvertex iterator': 'itasca.wall.WallVertexIter',
        'thermal wall object': 'itasca.wall.thermal.ThermalWall',
        'thermal wall iterator object': 'itasca.wall.thermal.ThermalWallIter',
        'thermal facet object': 'itasca.wall.thermal.ThermalFacet',
        'thermal facet iterator object': 'itasca.wall.thermal.ThermalFacetIter',
        'measure object': 'itasca.measure.Measure',
        'measure iterator object': 'itasca.measure.MeasureIter',
        'rblock object': 'itasca.rblock.RBlock',
        'rblock object iterator': 'itasca.rblock.RBlockIter',
        'rblock template pebble object': 'itasca.rblock.template.RBlockTemplatePebble',
        'rblock template iterator object': 'itasca.rblock.template.RBlockTemplateIter',
        'tuple of pyobject pointers for the currenly in-scope and valid objects': 'typing.Tuple[object, ...]',
        'tuple of str': 'typing.Tuple[str, ...]',
        'int or (object1': 'typing.Union[int, object]',
        'tuple of pyobject pointers for the currenly in-scope and valid ball objects': 'typing.Tuple[itasca.ball.Ball, ...]',
        'tuple of ball objects': 'typing.Tuple[itasca.ball.Ball, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid thermal ball objects': 'typing.Tuple[itasca.ball.thermal.ThermalBall, ...]',
        'tuple of thermal ball objects': 'typing.Tuple[itasca.ball.thermal.ThermalBall, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid clump objects': 'typing.Tuple[itasca.clump.Clump, ...]',
        'dict {str: float}': 'typing.Dict[str, float]',
        'tuple of clump objects': 'typing.Tuple[itasca.clump.Clump, ...]',
        'clump template pebble object': 'itasca.rblock.template.RBlockTemplatePebble',
        'clump template iterator object': 'itasca.rblock.template.RBlockTemplateIter',
        'clump template object': 'itasca.rblock.template.RBlockTemplate',
        'tuple of pebble objects': 'typing.Tuple[itasca.clump.pebble.Pebble, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid thermal clump objects': 'typing.Tuple[itasca.clump.thermal.ThermalClump, ...]',
        'tuple of thermal clump objects': 'typing.Tuple[itasca.clump.thermal.ThermalClump, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid thermal pebble objects': 'typing.Tuple[itasca.clump.pebble.thermal.ThermalPebble, ...]',
        'tuple of thermal pebble objects': 'typing.Tuple[itasca.clump.pebble.thermal.ThermalPebble, ...]',
        'tuple of wall objects': 'typing.Tuple[itasca.wall.Wall, ...]',
        'tuple of facet objects': 'typing.Tuple[itasca.wall.facet.Facet, ...]',
        'tuple of wallvertex objects': 'typing.Tuple[itasca.wall.WallVertex, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid thermal wall objects': 'typing.Tuple[itasca.wall.thermal.ThermalWall, ...]',
        'tuple of thermal wall objects': 'typing.Tuple[itasca.wall.thermal.ThermalWall, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid thermal facet objects': 'typing.Tuple[itasca.wall.thermal.ThermalFacet, ...]',
        'tuple of thermal facet objects': 'typing.Tuple[itasca.wall.thermal.ThermalFacet, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid measure objects': 'typing.Tuple[itasca.measure.Measure, ...]',
        'tuple of pyobject pointers for the currenly in-scope and valid rblock objects': 'typing.Tuple[itasca.rblock.RBlock, ...]',
        'tuple of rblock objects': 'typing.Tuple[itasca.rblock.RBlock, ...]',
    }
    type_str = type_str.lower().strip()
    if type_str in return_type_dict:
        ret_type = return_type_dict[type_str]
    elif type_str.startswith('array '):
        ret_type = 'numpy.ndarray'
    else:
        return None
    return ret_type


def infer_func_args_return_types_from_docstring(docstr):
    match = re.match(r'^\((.*?)\) *-> *(.*?)(?:\.|$)', docstr)
    if not match:
        return None
    args_str, return_str = match.groups()
    args_list = []
    for arg_str in args_str.strip().split(','):
        arg_str = arg_str.strip()
        if ':' in arg_str and '=' not in arg_str:
            arg_name, arg_type = arg_str.split(':', maxsplit=1)
            arg_name = arg_name.strip()
            arg_type = get_type_str(arg_type)
            if arg_type is None:
                return None
            if '(' in arg_name:
                return None
            arg_name = arg_name.replace(' ', '_')
            args_list.append(ArgSig(name=arg_name, type=arg_type))
        else:
            return None
    if not args_str:
        args_list = []
    return_type = get_type_str(return_str)
    if return_type is None:
        return None
    return args_list, return_type


def generate_c_function_stub(module: ModuleType,
                             name: str,
                             obj: object,
                             output: List[str],
                             imports: List[str],
                             self_var: Optional[str] = None,
                             sigs: Optional[Dict[str, str]] = None,
                             class_name: Optional[str] = None,
                             class_sigs: Optional[Dict[str, str]] = None) -> None:
    """Generate stub for a single function or method.
    The result (always a single line) will be appended to 'output'.
    If necessary, any required names will be added to 'imports'.
    The 'class_name' is used to find signature of __init__ or __new__ in
    'class_sigs'.
    """
    if sigs is None:
        sigs = {}
    if class_sigs is None:
        class_sigs = {}

    ret_type = 'None' if name == '__init__' and class_name else 'Any'

    if (name in ('__new__', '__init__') and name not in sigs and class_name and
            class_name in class_sigs):
        inferred = [FunctionSig(name=name,
                                args=infer_arg_sig_from_anon_docstring(class_sigs[class_name]),
                                ret_type=ret_type)]  # type: Optional[List[FunctionSig]]
    else:
        docstr = getattr(obj, '__doc__', None)
        inferred_from_docstr = infer_func_args_return_types_from_docstring(docstr)
        if docstr is not None and inferred_from_docstr is None:
            print(docstr)
        if class_name and name not in sigs:
            class_args = infer_method_sig(name)
            if inferred_from_docstr is not None:
                inferred_args, inferred_return_type = inferred_from_docstr
                if inferred_args[0].name == 'self':
                    inferred_args = inferred_args[1:]
                class_args[1:] = inferred_args
                ret_type = inferred_return_type
            inferred = [FunctionSig(name, args=class_args, ret_type=ret_type)]
        else:
            args = infer_arg_sig_from_anon_docstring(sigs.get(name, '(*args, **kwargs)'))
            if inferred_from_docstr is None:
                inferred = [FunctionSig(name=name, args=args, ret_type=ret_type)]
            else:
                inferred = [FunctionSig(name=name, args=inferred_from_docstr[0], ret_type=inferred_from_docstr[1])]

    is_overloaded = len(inferred) > 1 if inferred else False
    if is_overloaded:
        imports.append('from typing import overload')
    if inferred:
        for signature in inferred:
            sig = []
            for arg in signature.args:
                if arg.name == self_var:
                    arg_def = self_var
                else:
                    arg_def = arg.name
                    if arg_def == 'None':
                        arg_def = '_none'  # None is not a valid argument name

                    if arg.type:
                        arg_def += ": " + strip_or_import(arg.type, module, imports)

                    if arg.default:
                        arg_def += " = ..."

                sig.append(arg_def)

            if is_overloaded:
                output.append('@overload')
            output.append('def {function}({args}) -> {ret}:'.format(
                function=name,
                args=", ".join(sig),
                ret=strip_or_import(signature.ret_type, module, imports)
            ))
            output.append('    """')
            for line in getattr(obj, '__doc__').split('. '):
                output.append('    {}.'.format(line).replace('..', '.'))
            output.append('    """')
            output.append('    pass')
            output.append('')


def strip_or_import(typ: str, module: ModuleType, imports: List[str]) -> str:
    """Strips unnecessary module names from typ.
    If typ represents a type that is inside module or is a type coming from builtins, remove
    module declaration from it. Return stripped name of the type.
    Arguments:
        typ: name of the type
        module: in which this type is used
        imports: list of import statements (may be modified during the call)
    """
    stripped_type = typ
    for sub_typ in re.findall(r'\b[a-zA-Z0-9_.]+', typ):
        if sub_typ in ('...', ''):
            continue
        stripped_type = sub_typ
        if module and sub_typ.startswith(module.__name__ + '.'):
            stripped_type = sub_typ[len(module.__name__) + 1:]
        elif '.' in sub_typ:
            arg_module = sub_typ[:sub_typ.rindex('.')]
            if arg_module == 'builtins':
                stripped_type = sub_typ[len('builtins') + 1:]
            else:
                imports.append('import %s' % (arg_module,))
    return stripped_type


def generate_c_property_stub(name: str, obj: object, output: List[str], readonly: bool) -> None:
    """Generate property stub using introspection of 'obj'.
    Try to infer type from docstring, append resulting lines to 'output'.
    """
    docstr = getattr(obj, '__doc__', None)
    inferred = infer_prop_type_from_docstring(docstr)
    if not inferred:
        inferred = 'Any'

    output.append('@property')
    output.append('def {}(self) -> {}: ...'.format(name, inferred))
    if not readonly:
        output.append('@{}.setter'.format(name))
        output.append('def {}(self, val: {}) -> None: ...'.format(name, inferred))


def generate_c_type_stub(module: ModuleType,
                         class_name: str,
                         obj: type,
                         output: List[str],
                         imports: List[str],
                         sigs: Optional[Dict[str, str]] = None,
                         class_sigs: Optional[Dict[str, str]] = None) -> None:
    """Generate stub for a single class using runtime introspection.
    The result lines will be appended to 'output'. If necessary, any
    required names will be added to 'imports'.
    """
    # typeshed gives obj.__dict__ the not quite correct type Dict[str, Any]
    # (it could be a mappingproxy!), which makes mypyc mad, so obfuscate it.
    obj_dict = getattr(obj, '__dict__')  # type: Mapping[str, Any]  # noqa
    items = sorted(obj_dict.items(), key=lambda x: method_name_sort_key(x[0]))
    methods = []  # type: List[str]
    properties = []  # type: List[str]
    done = set()  # type: Set[str]
    for attr, value in items:
        if is_c_method(value) or is_c_classmethod(value):
            done.add(attr)
            if not is_skipped_attribute(attr):
                if attr == '__new__':
                    # TODO: We should support __new__.
                    if '__init__' in obj_dict:
                        # Avoid duplicate functions if both are present.
                        # But is there any case where .__new__() has a
                        # better signature than __init__() ?
                        continue
                    attr = '__init__'
                if is_c_classmethod(value):
                    methods.append('@classmethod')
                    self_var = 'cls'
                else:
                    self_var = 'self'
                generate_c_function_stub(module, attr, value, methods, imports=imports,
                                         self_var=self_var, sigs=sigs, class_name=class_name,
                                         class_sigs=class_sigs)
        elif is_c_property(value):
            done.add(attr)
            generate_c_property_stub(attr, value, properties, is_c_property_readonly(value))

    variables = []
    for attr, value in items:
        if is_skipped_attribute(attr):
            continue
        if attr not in done:
            variables.append('%s: Any = ...' % attr)
    all_bases = obj.mro()
    if all_bases[-1] is object:
        # TODO: Is this always object?
        del all_bases[-1]
    # remove pybind11_object. All classes generated by pybind11 have pybind11_object in their MRO,
    # which only overrides a few functions in object type
    if all_bases and all_bases[-1].__name__ == 'pybind11_object':
        del all_bases[-1]
    # remove the class itself
    all_bases = all_bases[1:]
    # Remove base classes of other bases as redundant.
    bases = []  # type: List[type]
    for base in all_bases:
        if not any(issubclass(b, base) for b in bases):
            bases.append(base)
    if bases:
        bases_str = '(%s)' % ', '.join(
            strip_or_import(
                get_type_fullname(base),
                module,
                imports
            ) for base in bases
        )
    else:
        bases_str = ''
    if not methods and not variables and not properties:
        output.append('class %s%s: ...' % (class_name, bases_str))
    else:
        output.append('class %s%s:' % (class_name, bases_str))
        for variable in variables:
            output.append('    %s' % variable)
        for method in methods:
            output.append('    %s' % method)
        for prop in properties:
            output.append('    %s' % prop)


def get_type_fullname(typ: type) -> str:
    return '%s.%s' % (typ.__module__, typ.__name__)


def method_name_sort_key(name: str) -> Tuple[int, str]:
    """Sort methods in classes in a typical order.
    I.e.: constructor, normal methods, special methods.
    """
    if name in ('__new__', '__init__'):
        return 0, name
    if name.startswith('__') and name.endswith('__'):
        return 2, name
    return 1, name


def is_skipped_attribute(attr: str) -> bool:
    return attr in ('__getattribute__',
                    '__str__',
                    '__repr__',
                    '__doc__',
                    '__dict__',
                    '__module__',
                    '__weakref__')  # For pickling


def infer_method_sig(name: str) -> List[ArgSig]:
    args = None  # type: Optional[List[ArgSig]]
    if name.startswith('__') and name.endswith('__'):
        name = name[2:-2]
        if name in ('hash', 'iter', 'next', 'sizeof', 'copy', 'deepcopy', 'reduce', 'getinitargs',
                    'int', 'float', 'trunc', 'complex', 'bool', 'abs', 'bytes', 'dir', 'len',
                    'reversed', 'round', 'index', 'enter'):
            args = []
        elif name == 'getitem':
            args = [ArgSig(name='index')]
        elif name == 'setitem':
            args = [ArgSig(name='index'),
                    ArgSig(name='object')]
        elif name in ('delattr', 'getattr'):
            args = [ArgSig(name='name')]
        elif name == 'setattr':
            args = [ArgSig(name='name'),
                    ArgSig(name='value')]
        elif name == 'getstate':
            args = []
        elif name == 'setstate':
            args = [ArgSig(name='state')]
        elif name in ('eq', 'ne', 'lt', 'le', 'gt', 'ge',
                      'add', 'radd', 'sub', 'rsub', 'mul', 'rmul',
                      'mod', 'rmod', 'floordiv', 'rfloordiv', 'truediv', 'rtruediv',
                      'divmod', 'rdivmod', 'pow', 'rpow',
                      'xor', 'rxor', 'or', 'ror', 'and', 'rand', 'lshift', 'rlshift',
                      'rshift', 'rrshift',
                      'contains', 'delitem',
                      'iadd', 'iand', 'ifloordiv', 'ilshift', 'imod', 'imul', 'ior',
                      'ipow', 'irshift', 'isub', 'itruediv', 'ixor'):
            args = [ArgSig(name='other')]
        elif name in ('neg', 'pos', 'invert'):
            args = []
        elif name == 'get':
            args = [ArgSig(name='instance'),
                    ArgSig(name='owner')]
        elif name == 'set':
            args = [ArgSig(name='instance'),
                    ArgSig(name='value')]
        elif name == 'reduce_ex':
            args = [ArgSig(name='protocol')]
        elif name == 'exit':
            args = [ArgSig(name='type'),
                    ArgSig(name='value'),
                    ArgSig(name='traceback')]
    if args is None:
        args = [ArgSig(name='*args'),
                ArgSig(name='**kwargs')]
    return [ArgSig(name='self')] + args

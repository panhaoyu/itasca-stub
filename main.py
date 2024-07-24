import inspect
import inspect
import json
import os
import os.path
import socket
import struct
import subprocess
import time
import traceback
import types
from pathlib import Path
from typing import Dict, Optional, Set
from typing import List

import _itasca_com
import numpy
import select
from mypy.moduleinspect import is_c_module
from mypy.stubgenc import strip_or_import, get_type_fullname, add_typing_import, generate_c_type_stub, is_c_type, \
    generate_c_function_stub, is_c_function

import itasca

itasca.command(r'program directory custom "F:/projects/itasca-stub"')


def generate_stub_for_c_module(module: types.ModuleType,
                               target: Path,
                               sigs: Optional[Dict[str, str]] = None,
                               class_sigs: Optional[Dict[str, str]] = None) -> None:
    """Generate stub for C module.

    This combines simple runtime introspection (looking for docstrings and attributes
    with simple builtin types) and signatures inferred from .rst documentation (if given).

    If directory for target doesn't exist it will be created. Existing stub
    will be overwritten.
    """
    target = str(target)
    assert is_c_module(module), f'{module} is not a C module'
    subdir = os.path.dirname(target)
    if subdir and not os.path.isdir(subdir):
        os.makedirs(subdir)
    imports: List[str] = []
    functions: List[str] = []
    done = set()
    items = sorted(module.__dict__.items(), key=lambda x: x[0])
    for name, obj in items:
        if is_c_function(obj):
            generate_c_function_stub(module, name, obj, functions, imports=imports, sigs=sigs)
            done.add(name)
    types: List[str] = []
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
            type_str = strip_or_import(get_type_fullname(type(obj)), module, imports)
            variables.append(f'{name}: {type_str}')
    output = []
    for line in sorted(set(imports)):
        output.append(line)
    for line in variables:
        output.append(line)
    for line in types:
        if line.startswith('class') and output and output[-1]:
            output.append('')
        output.append(line)
    if output and functions:
        output.append('')
    for line in functions:
        output.append(line)
    output = add_typing_import(output)
    with open(target, 'w') as file:
        for line in output:
            file.write(f'{line}\n')


class PackageGenerator:
    def __init__(self, package):
        self.package = package
        self.all_packages: Dict[str, Optional[types.ModuleType]] = {
            # The names here will be skipped
            'itasca._test': None,
            'itasca.util': None,
        }
        self.found_objs: Set[types.ModuleType] = {
            # The objects here will be skipped
            numpy, json, subprocess, socket, os, _itasca_com, struct, time, select,
        }

    def find_package(self, name: str, module: types.ModuleType) -> None:
        for sub_name, instance in vars(module).items():
            if not isinstance(instance, types.ModuleType):
                continue
            if instance in self.found_objs:
                continue
            total_name = f'{name}.{sub_name}'
            if total_name in self.all_packages:
                continue
            self.all_packages[total_name] = instance
            self.found_objs.add(instance)
            self.find_package(total_name, instance)

    def generate(self) -> None:
        self.all_packages['itasca'] = self.package
        self.find_package('itasca', self.package)
        self.all_packages = {k: v for k, v in self.all_packages.items() if v is not None}
        list(map(print, self.all_packages))
        for name, module in self.all_packages.items():
            path = Path(name.replace('.', '/')) / '__init__.py'
            try:
                generate_stub_for_c_module(module, path)
            except (AssertionError, TypeError):
                traceback.print_exc()
                print('Error: ', name)


PackageGenerator(itasca).generate()

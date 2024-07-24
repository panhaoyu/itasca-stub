import importlib
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

import _itasca_com
import numpy
import select

import itasca

itasca.command(r'program directory custom "F:/projects/itasca-stub"')

import stubgenc

importlib.reload(stubgenc)


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
        for name, module in self.all_packages.items():
            path = Path(name.replace('.', '/')) / '__init__.py'
            other_imports = [key.replace(name + '.', '')
                             for key in self.all_packages.keys()
                             if key.startswith(name + '.')]
            other_imports = [other_import for other_import in other_imports if other_import]
            other_imports = [other_import for other_import in other_imports if '/' not in other_import]
            try:
                stubgenc.generate_stub_for_c_module(module, str(path), other_import=other_imports)
            except (AssertionError, TypeError):
                traceback.print_exc()
                print('Error: ', name)


PackageGenerator(itasca).generate()

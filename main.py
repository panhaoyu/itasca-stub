import importlib
import types
from typing import Dict

import mypy.stubgen

import itasca

itasca.command(r'program directory custom "F:/projects/itasca-stub"')

importlib.reload(mypy.stubgen)


class PackageGenerator:
    def __init__(self, package):
        self.package = package
        self.all_packages: Dict[str, types.ModuleType] = {}

    def find_package(self, name: str, module: types.ModuleType) -> None:
        for sub_name, instance in vars(module).items():
            if not isinstance(instance, types.ModuleType):
                continue
            if sub_name.startswith('_'):
                continue
            if hasattr(instance, '__package__') and instance.__package__:
                continue
            if instance in self.all_packages.values():
                continue
            total_name = f'{name}/{sub_name}'
            if total_name == 'itasca/util':
                continue
            print(total_name)
            self.all_packages[total_name] = instance
            self.find_package(total_name, instance)

    def generate(self) -> None:
        self.all_packages['itasca'] = self.package
        self.find_package('itasca', self.package)
        for name, package in self.all_packages.items():
            path = f'{name}/__init__.py'
            other_imports = [key.replace(f'{name}/', '')
                             for key in self.all_packages.keys()
                             if key.startswith(f'{name}/')]
            other_imports = [other_import for other_import in other_imports if other_import and '/' not in other_import]
            try:
                mypy.stubgen.generate_stub_for_c_module(package, path)
            except (AssertionError, TypeError):
                print('Error', name)


PackageGenerator(itasca).generate()

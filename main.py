import os
import types
import stubgenc
import itasca
import importlib

importlib.reload(stubgenc)


class PackageGenerator(object):
    def __init__(self, package):
        self.package = package
        self.all_packages = dict()

    def find_package(self, name, module):
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

    def generate(self):
        self.all_packages['itasca'] = self.package
        self.find_package('itasca', self.package)
        for name, package in self.all_packages.items():
            path = '{}/__init__.py'.format(name)
            other_imports = [key.replace(name + '/', '')
                             for key in self.all_packages.keys()
                             if key.startswith(name + '/')]
            other_imports = [other_import for other_import in other_imports if other_import]
            other_imports = [other_import for other_import in other_imports if '/' not in other_import]
            try:
                stubgenc.generate_stub_for_c_module(package, path, other_import=other_imports)
            except (AssertionError, TypeError):
                print('Error', name)


PackageGenerator(itasca).generate()

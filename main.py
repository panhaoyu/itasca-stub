import os
import types
import stubgenc
import itasca
import importlib

importlib.reload(stubgenc)

result_path = os.path.join(os.path.dirname('main.py'), r'itasca.pyi')
stubgenc.generate_stub_for_c_module(itasca, result_path)

#
# class PackageGenerator(object):
#     def __init__(self, package):
#         self.package = package
#         self.all_packages = dict()
#
#     def find_package(self, name, package):
#         for sub_name, instance in vars(package).items():
#             if not isinstance(instance, types.ModuleType):
#                 continue
#             if sub_name.startswith('_'):
#                 continue
#             if hasattr(instance, '__package__') and instance.__package__:
#                 continue
#             if instance in self.all_packages.values():
#                 continue
#             total_name = f'{name}/{sub_name}'
#             self.all_packages[total_name] = instance
#             self.find_package(total_name, instance)
#
#     def generate(self):
#         self.find_package('itasca', self.package)
#         for name, package in self.all_packages.items():
#             path = os.path.join('C:/stub/', name, '__init__.py')
#             try:
#                 stubgenc.generate_stub_for_c_module(package, path)
#             except (AssertionError, TypeError):
#                 print(name)
#
#
# PackageGenerator(itasca).generate()

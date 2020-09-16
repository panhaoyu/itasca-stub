import os
import shutil

os.system('setup.py sdist bdist_wheel')
os.system('twine upload dist/*')

for directory in ('build', 'dist', 'itasca_stub.egg-info'):
    os.path.exists(directory) and shutil.rmtree(directory)

setup.py sdist bdist_wheel
twine upload dist/*
rm -r build
rm -r dist
rm -r itasca_stub.egg-info
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='itasca-stub',
    packages=setuptools.find_packages(),
    version='1.0.4',
    license='MIT',
    description='Itasca PFC python stub',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='panhaoyu',
    author_email='panhaoyu.china@outlook.com',
    url='https://github.com/panhaoyu/itasca-stub',
    download_url='https://github.com/panhaoyu/itasca-stub/archive/1.0.0.tar.gz',
    keywords=['ITASCA', 'STUB', 'PFC'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)

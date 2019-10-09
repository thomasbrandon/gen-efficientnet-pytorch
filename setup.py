from setuptools import setup, find_packages

setup(
    name='gen_efficientnet',
    version='0.0.1',
    packages=find_packages(exclude=['data']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['torch>=1.1'],
    author='Ross Wightman',
    url='https://github.com/rwightman/gen-efficientnet-pytorch',
)
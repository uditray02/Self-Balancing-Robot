from setuptools import find_packages
from setuptools import setup

setup(
    name='mybot_controller',
    version='0.0.0',
    packages=find_packages(
        include=('mybot_controller', 'mybot_controller.*')),
)

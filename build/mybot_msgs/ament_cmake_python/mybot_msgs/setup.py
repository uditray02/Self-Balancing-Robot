from setuptools import find_packages
from setuptools import setup

setup(
    name='mybot_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('mybot_msgs', 'mybot_msgs.*')),
)

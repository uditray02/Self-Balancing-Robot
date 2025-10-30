from setuptools import find_packages, setup

package_name = 'mybot_py_programs'


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='uditr',
    maintainer_email='uditr@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = mybot_py_programs.simple_publisher:main',
            'simple_subscriber= mybot_py_programs.simple_subscriber:main',
            'simple_parameter= mybot_py_programs.simple_parameter:main',
            'simple_turtlesim_kinematics= mybot_py_programs.simple_turtlesim_kinematics:main',
            'simple_controller = mybot_controller.simple_controller:main',
            'simple_tf_kinematics = mybot_py_programs.simple_tf_kinematics:main',
            'simple_service_server = mybot_py_programs.simple_service_server:main',
            'simple_service_client = mybot_py_programs.simple_service_client:main',
        ],
    },
)

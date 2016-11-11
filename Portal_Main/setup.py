from setuptools import setup

setup(
    name='flask_portal',
    packages=['flask_portal'],
    include_package_data=True,
    install_requires=[
        'flask_portal',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
from setuptools import setup, find_packages

setup(
    name='sneaky_s0ng',
    version='0.1',
    py_modules=['music'],
    entry_points={
        'console_scripts': [
            'sneaky_s0ng=sneaky_s0ng:main',
        ],
    },
)
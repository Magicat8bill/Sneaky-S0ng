from setuptools import setup, find_packages

setup(
    name='sneaky_s0ng',
    version='0.1',
    py_modules=['music'],  # The module file should be music.py
    entry_points={
        'console_scripts': [
            'sneaky_s0ng=music:main',  # Assuming music.py has a main() function
        ],
    },
)

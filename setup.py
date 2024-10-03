from setuptools import setup, find_packages

setup(
    name='sneaky_s0ng',
    version='2.0.3-beta',
    packages=find_packages(),
    description='A Python package for encrypting English and German to music notation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/magicat8/Sneaky-S0ng',
    author='Cameron',
    author_email='magicat8bill@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    install_requires=[
        'music21>=9.1.0',
    ],
    python_requires='>=3.8',
)

from setuptools import setup, find_packages

setup(
    name='sneaky_s0ng',
    version='2.1.2-beta',
    description='A Python package for encrypting English and German to music notation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://magicat8.github.io',
    project_urls = {
        'Documentation': "https://github.com/Magicat8bill/Sneaky-S0ng/tree/main",
    },

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

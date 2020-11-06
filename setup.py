#!/usr/bin/python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
        name = 'pippo',
        version = '0.0.1a',
        author = 'Scorpion',
        author_email = 'glnvlln0@gmail.com',
        description = 'A simple program for setup new packages in python',
        long_descrption = long_description,
        package_dir = {'': 'src'},
        packages = find_packages(where='src'),
        entry_points={
            'console_scripts': [
                'pysetup=pysetup:main',
            ],
        },
)

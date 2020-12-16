#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='dndtools', 
        version='0.1', 
        description='Dungeons & Dragons tools.', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/dndtools',
        scripts=['idealweight'],
        install_requires=['asciimatics']
)


# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='math_series',
    description='math_series module',
    version=0.1,
    author='Jeff Torres',
    author_email='jeffrey.n.torres@gmail.com',
    license='MIT',
    py_modules=['series'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={}
)

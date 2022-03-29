#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['mock==4.0.3', 'pytest==7.1.1']

test_requirements = ['pytest>=3', ]

setup(
    author="Nebiyu Samuel",
    email="neba.samuel17@gmail.com",
    python_requires='>=3.6',
    description="Scripts for controlling Ruby Robot",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='pytest,parser',
    name='Ruby Robot Controller',
    packages=find_packages(include=['src', 'src.*']),
    test_suite='Tests',
    tests_require=test_requirements,
    url='https://github.com/nebasam/Ruby_Robot_Challenge',
    version='0.1.0',
    zip_safe=False,
)
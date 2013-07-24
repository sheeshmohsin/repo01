#!/usr/bin/env python
"""Shell Dummy project"""
from setuptools import find_packages, setup

dependencies = [
        'setuptools',
        'requests',
        'cmd2',
    ]

setup(name = 'shell',
    version = '0.2',
    description = "A python script to run an own shell",
    long_description = "A python script to run an own shell",
    platforms = ["Linux"],
    author = "Sheesh Mohsin",
    author_email = "sheeshmohsin@gmail.com",
    url = "http://dgplug.org/summertraining/2013/",
    license = "MIT",
    packages = find_packages(),
    install_requires = dependencies,
    include_package_data=True,
    scripts=['shell'],
    data_files=[('/usr/bin',['shell']),
    ('/usr/share/shell', ['README'])
    ]
    
    )

#!/usr/bin/env python
"""Shell Dummy project"""
from setuptools import find_packages, setup

dependencies=[
        'setuptools',
       	'requests',
       	'cmd2',
       	'fbconsole',
	'pyparsing',
    	],
setup(name = 'shell',
    version = '1.9',
    description = "A python script to run an own shell",
    long_description = "A python script to run an own shell",
    platforms = ["Linux"],
    author = "Sheesh Mohsin",
    author_email = "sheeshmohsin@gmail.com",
    url = "http://dgplug.org/summertraining/2013/",
    license = "MIT",
    packages = find_packages(),
    install_requires=dependencies,
    include_package_data=True,
    dependency_links=[
    "https://pypi.python.org/packages/source/r/requests/requests-1.2.3.tar.gz",
    "https://pypi.python.org/pypi/cmd2/0.6.5.1#downloads",
    "https://pypi.python.org/packages/source/f/fbconsole/fbconsole-0.3.tar.gz#md5=69856ea01782f2dada11e429ff8edb7c",
    "https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz#md5=9be0fcdcc595199c646ab317c1d9a709",
    "https://pypi.python.org/packages/source/p/poster/poster-0.8.1.tar.gz#md5=2db12704538781fbaa7e63f1505d6fc8",
    ],
    scripts=['shell'],
)

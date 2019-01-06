#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='asynchronize',
    version='0.0.1',
    description='Python package for converting callback functions to asynchronous coroutines',
    url='https://github.com/TMiguelT/Asynchronize',
    author='Michael Milton',
    author_email='michael.r.milton@gmail.com',
    license='GPLv3',
    test_suite='test',
    classifiers=[
        'Framework :: AsyncIO',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='asyncio async callback coroutine',
    packages=find_packages(),
)

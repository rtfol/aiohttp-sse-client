#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['aiohttp>=3', 'attrs', 'multidict', 'yarl', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Jason Hu",
    author_email='awaregit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Server-Sent Event python client base on aiohttp",
    install_requires=requirements,
    license="Apache License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='aiohttp_sse_client',
    name='aiohttp-sse-client',
    packages=find_packages(include=['aiohttp_sse_client']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rtfol/aiohttp-sse-client',
    version='0.2.1',
    zip_safe=False,
)

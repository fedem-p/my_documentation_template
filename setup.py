#!/usr/bin/env python3

import os
from setuptools import setup
from setuptools import find_packages

#get long description

with open("README.md") as f:
    long_description = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name='myproject',
    description='a template for making documentation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.2',
    author='Federico Puppo',
    author_email='federico.puppo@outlook.it',
    url='https://github.com/fedem-p/my_documentation_template',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    license='MIT',
    zip_safe=False,
    entry_points={
        'console_scripts': ['myproject=myproject.entry_points:main'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
    ],
    keywords='auto documentation'
)
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/23, 17:50
"""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="vcommand",
    version="0.1.0",
    author="Virink",
    author_email="virink@outlook.com",
    description="A command plugin for terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/virink/vCommand.git",
    packages=find_packages(),
    entry_points={'console_scripts': [
        'vcommand = vcommand.__main__:main'
    ]},
    # scripts=glob.glob("bin/*"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

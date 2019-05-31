#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/23, 17:50
"""

from setuptools import find_packages, setup

__NAME__ = "vcommand"
__VERSION__ = "0.1.0"
__AUTHOR__ = "Virink"
__EMAIL__ = "virink@outlook.com"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=__NAME__,
    version=__VERSION__,
    author=__AUTHOR__,
    author_email=__EMAIL__,
    description="A command plugin for terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/virink/vCommand.git",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'vcommand = vcommand.__main__:main'
        ]
    },
    install_requires=[    # 依赖列表
        'requests>=2.22.0',
    ],
    # scripts=glob.glob("bin/*"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

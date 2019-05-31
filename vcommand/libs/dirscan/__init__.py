#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/30, 14:30
"""


def func_dirscan(*args):
    """Scan dirs for CTF """
    from .dirscan import main_dirscan
    return main_dirscan(*args)

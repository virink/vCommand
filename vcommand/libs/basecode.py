#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/04/18, 14:27
"""

import base64


def paddingBase64(length, bit, sym='='):
    """Base64 Padding"""
    _length = length % bit
    return (8-_length) * sym if _length > 0 else ""


def func_b64d(*args):
    """Base64 Decode"""
    arg = args[0]
    arg += paddingBase64(len(arg), 4)
    arg = arg if isinstance(arg, bytes) else arg.encode('utf-8')
    return base64.b64decode(arg).decode('utf-8')


def func_b64e(*args):
    """Base64 Encode"""
    arg = args[0]
    arg = arg if isinstance(arg, bytes) else arg.encode('utf-8')
    return base64.b64encode(arg).decode('utf-8')


def func_b32d(*args):
    """Base32 Decode"""
    arg = args[0]
    arg += paddingBase64(len(arg), 8)
    arg = arg if isinstance(arg, bytes) else arg.encode('utf-8')
    return base64.b32decode(arg).decode('utf-8')


def func_b32e(*args):
    """Base32 Encode"""
    arg = args[0]
    arg = arg if isinstance(arg, bytes) else arg.encode('utf-8')
    return base64.b32encode(arg).decode('utf-8')


def func_b16d(*args):
    """Base16 Decode"""
    arg = args[0]
    arg = arg if not len(arg) % 2 else arg[:-1]
    arg = arg if isinstance(arg, bytes) else arg.encode('utf-8')
    return base64.b16decode(arg).decode('utf-8')


def func_b16e(*args):
    """Base14 Encode"""
    arg = args[0]
    arg = arg if isinstance(arg, bytes) else arg.encode('utf-8')
    return base64.b16encode(arg).decode('utf-8')

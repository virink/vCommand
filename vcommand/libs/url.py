#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/03/01, 14:27
"""

import urllib.parse


def func_urld(*args):
    """URL 解码"""
    return func_urldecode(*args)


def func_urldecode(*args):
    """URL 解码"""
    return urllib.parse.unquote(args[0].encode('utf-8'))


def func_urle(*args):
    """URL 编码"""
    return func_urlencode(*args)


def func_urlencode(*args):
    """URL 编码"""
    return urllib.parse.quote(args[0].encode('utf-8'))


def func_urldp(*args):
    """URL 解码 Plus"""
    return func_urldecode_plus(*args)


def func_urldecode_plus(*args):
    """URL 解码 Plus"""
    return urllib.parse.unquote_plus(args[0].encode('utf-8'))


def func_urlep(*args):
    """URL 编码 Plus"""
    return func_urlencode_plus(*args)


def func_urlencode_plus(*args):
    """URL 编码 Plus"""
    return urllib.parse.quote_plus(args[0].encode('utf-8'))

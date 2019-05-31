#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/03/01, 14:27
"""

import urllib.parse
import socket
import struct
import binascii
import re


def func_str2ascii(*args):
    """字符串 -> ASCII"""
    return ','.join([str(ord(i)) for i in args[0]])


def func_str2ord(*args):
    """字符串 -> ASCII"""
    return func_str2ascii(args[0])


def func_ascii2str(*args):
    """ASCII -> 字符串 (逗号分隔)"""
    return ''.join([chr(int(i)) for i in args[0].split(',')])


def func_ord2str(*args):
    """ASCII -> 字符串"""
    return func_ascii2str(args[0])


def func_dec2hex(*args):
    """Dec -> Hex"""
    return hex(int(args[0]))


def func_hex2dec(*args):
    """Hex -> Dec"""
    arg = args[0]
    return int(arg if arg.startswith('0x') else "0x" + arg, 16)


def func_byte2hex(*args):
    """Byte -> Hex"""
    return "0x%s" % binascii.hexlify(args[0]).decode('utf-8')


def func_str2byte(*args):
    """字符串 -> Byte"""
    return args[0].encode('utf-8')


def func_str2hex(*args):
    """字符串 -> Hex"""
    return func_byte2hex(func_str2byte(*args))


def func_hex2byte(*args):
    """Hex -> Byte"""
    arg = args[0]
    if arg.startswith('0x'):
        arg = arg[2:]
    return binascii.unhexlify(arg)


def func_hex2str(*args):
    """字符串 -> Hex"""
    return func_hex2byte(*args).decode('utf-8')


def func_ip2hex(*args):
    """IP -> Hex"""
    arg = args[0]
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", arg):
        return func_byte2hex(socket.inet_aton(arg))
    return False


def func_hex2ip(*args):
    """Hex -> IP"""
    return func_dec2ip(func_hex2dec(args[0]))


def func_dec2ip(*args):
    """Dec -> IP"""
    return socket.inet_ntoa(struct.pack('I', socket.htonl(int(args[0]))))


def func_ip2dec(*args):
    """IP -> Dec"""
    return func_hex2dec(func_ip2hex(args[0]))

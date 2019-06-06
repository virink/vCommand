#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/06/03, 15:33
"""

import sys

CRED = '\033[1;31m'
CGREEN = '\033[1;32m'
CYELLOW = '\033[1;33m'
CVIOLET = '\033[1;35m'
CBEIGE = '\033[1;36m'
CEND = '\033[0m'


def cprint(*args):
    if args[-1] == '\r':
        sys.stdout.write(''.join(args[:-1])+CEND+'\r')
    else:
        sys.stdout.write(''.join(args)+CEND+'\n')

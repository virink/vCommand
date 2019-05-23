#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/03/01, 14:27
"""
import sys
import os

from . import libs

funcs = [func for func in libs.__dir__() if func.startswith('func_')]


def main():
    args = list(sys.argv[1:])
    # stdin
    if not sys.stdin.isatty():
        args += [sys.stdin.readline().strip()]
    # Usage
    if len(args) < 1:
        print("[!] Usage: command arg1 [arg2...]")
        sys.exit(1)
    argv = 0
    command = args[argv]
    argv += 1
    # helper
    if command == 'help':
        print("[!] No help")
        return 1
    elif command in ['v', 'version', 'V']:
        print("[!] Version : 0.1.0 beta")
        return 1
    elif command in ['func', 'function', 'F']:
        print("[@] === Functions ===")
        for func in funcs:
            doc = libs.__dict__[func].__doc__
            line = "[*] {0:^15} - {1}"
            print(line.format(func[5:], doc if doc else ""))
        print("[@] ====== End ======")
        return 1
    elif command in ['_alias']:
        for func in funcs:
            print('alias {}="vcommand {}"'.format(func[5:], func[5:]))
        print('alias func="vcommand func"')
        return 1
    if 'func_%s' % command not in funcs:
        print('[!] Command [%s] not Found' % command)
        sys.exit(1)
    # Functions
    try:
        args = args[argv:]
        res = libs.__dict__['func_%s' % command](*args)
        print(res)
    except Exception as e:
        print("[-] Error : %s" % e)
        return 1


if __name__ == '__main__':
    main()

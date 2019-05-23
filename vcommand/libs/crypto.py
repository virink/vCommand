#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/04/18, 14:49
"""

import string
import re

L = string.ascii_lowercase
U = string.ascii_uppercase
A = string.ascii_letters


def func_atbash(*args):
    """埃特巴什码解码"""
    arg = args[0]
    arg = arg.lower().replace(' ', 'vvvzzzvvv')
    res = [L[25 - j] for i in arg for j in range(26) if i == L[j]]
    return ''.join(res).replace('eeeaaaeee', ' ')


def __caesar(offset, arg):
    """凯撒编码 : 内部调用"""
    result = ""
    for ch in arg:
        if ch.isupper():
            result += U[((U.index(ch) + offset) % 26)]
        elif ch.islower():
            result += L[((L.index(ch) + offset) % 26)]
        elif ch.isdigit():
            result += ch
        else:
            result += ch
    return result


def func_caesar(*args):
    """凯撒编码"""
    res = []
    for offset in range(26):
        res.append("[+] offset : %d\tresult : %s" %
                   (offset, __caesar(offset, args[0])))
    return "\r\n".join(res)


def func_rot13(*args):
    """rot13"""
    return __caesar(13, args[0])


def func_mpkc(*args):
    """手机键盘编码 Mobile Phone Keyboard Cipher"""
    T = {
        'A': 21, 'B': 22, 'C': 23, 'D': 31, 'E': 32, 'F': 33,
        'G': 41, 'H': 42, 'I': 43, 'J': 51, 'K': 52, 'L': 53,
        'M': 61, 'N': 62, 'O': 63, 'P': 71, 'Q': 72, 'R': 73, 'S': 74,
        'T': 81, 'U': 82, 'V': 83, 'W': 91, 'X': 92, 'Y': 93, 'Z': 94
    }
    arg = args[0].upper()
    if arg[0] in U:
        return ','.join([str(T.get(i, i)) for i in arg])
    else:
        T = {str(T[k]): k for k in T}
        if ',' in arg:
            arg = arg.split(',')
        elif ' ' in arg:
            arg = arg.split(' ')
        return ''.join([T.get(i, i) for i in arg])


def func_morse(*args):
    """摩斯电码"""
    T = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
        '?': '..--..', '=': '-...-',  "'": '.----.', '/': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
        ')': '-.--.-', '$': '...-..-', '&': '. . . .', '@': '.--.-.',
        '{': '----.--', '}': '-----.-'
    }
    arg = args[0]
    if re.match(r'^[\.\-\/ ]+$', arg):
        T = {str(T[k]): k for k in T}
        if len(args) > 1:
            arg = ' '.join(args)
        arg = arg.replace('/', ' ').split(' ')
        # TODO: morse auto decode when it is not sep
        # p = 0
        # res = ''
        # d = 5
        # while p < (len(arg)+7) and d > 0:
        #     print("[D] len : %d  p : %d" % (len(arg), p))
        #     for j in [6, 5, 4, 3, 2, 1, 0]:
        #         tmp = T.get(arg[p:p+j], None)
        #         print("[D] tmp = arg[%d:%s] = %s => %s" %
        #               (p, j, arg[p:p+j], tmp))
        #         if tmp:
        #             p = p+j
        #             res += tmp
        #             break
        #         # p = p+j-1
        #     # break
        #     d -= 1
        #     print("[D] Result : %s" % res)
        return ''.join([T.get(i) for i in arg])
    else:
        return '/'.join([str(T.get(i, '?')) for i in arg.upper()])


def func_peigen(*args):
    """培根密码"""
    T = {
        'H': 'aabbb', 'G': 'aabba', 'R': 'baaab', 'Q': 'baaaa',
        'Z': 'bbaab', 'Y': 'bbaaa', 'N': 'abbab', 'M': 'abbaa',
        'U': 'babaa', 'V': 'babab', 'I': 'abaaa', 'J': 'abaab',
        'F': 'aabab', 'E': 'aabaa', 'A': 'aaaaa', 'B': 'aaaab',
        'T': 'baabb', 'S': 'baaba', 'C': 'aaaba', 'D': 'aaabb',
        'P': 'abbbb', 'O': 'abbba', 'K': 'ababa', 'L': 'ababb',
        'W': 'babba', 'X': 'babbb'
    }
    arg = args[0]
    if re.match(r'^[ab]+$', arg):
        T = {str(T[k]): k for k in T}
        return ''.join([T.get(arg[i:i+5]) for i in range(0, len(arg), 5)])
    else:
        return ''.join([T.get(i.upper()) for i in arg])


def __vigenere(s, key='virink', de=0):
    """维吉利亚密码"""
    s = str(s).replace(" ", "").upper()
    key = str(key).replace(" ", "").upper()
    res = ''
    i = 0
    while i < len(s):
        j = i % len(key)
        k = U.index(key[j])
        m = U.index(s[i])
        if de:
            if m < k:
                m += 26
            res += U[m - k]
        else:
            res += U[(m + k) % 26]
        i += 1
    return res


def func_vigenere(*args):
    """维吉利亚密码"""
    if len(args) < 2:
        return '[-] Vigenere Usage : command key text [isdecode]'
    return __vigenere(args[1], args[0], 1 if len(args) >= 3 else 0)

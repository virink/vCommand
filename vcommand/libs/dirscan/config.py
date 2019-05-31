#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/30, 14:25
"""

import sys
import os

KEY_WORDS = ['flag', 'ctf', 'admin']
# 最大队列数
MAX_QUEUE_NUM = 5120
# 线程数
NUMBER_OF_THREAD = 5
# 请求方式
# 1 => HEAD  2 => GET
REQUEST_METHOD = 1
# 无效的状态码
INVALID_CODE = [404, 403]
# 超时时间
TIME_OUT = 5
# 记录缓存日志
CACHE_LOG = True
# Print Color
CRED = '\033[1;31m'
CGREEN = '\033[1;32m'
CYELLOW = '\033[1;33m'
CVIOLET = '\033[1;35m'
CBEIGE = '\033[1;36m'
CEND = '\033[0m'

_default_dic = {
    'files': [],
    'exts': [
        '$', '$.7z', '$.bak', '$.back', '$.backup', '$.bz2', '$.cab$.html',
        '$.gz', '$.iso', '$.php', '$.rar', '$.save', '$.sql', '$.swp', '$.swp~',
        '.$.swp', '$.tar', '$.tar.bz2', '$.tar.gz', '$.tgz', '$.txt', '$.viminfo',
        '$.xml', '$.zip', '$~', '.$~', '$.jsp', '$.asp', '$.aspx'
    ],
    'keywords': ['flag', 'index', 'source']
}

_config_path = os.path.join(os.getenv('HOME'), '.config', 'vcommand')
dic_files_path = os.path.join(_config_path, 'files.dic')
dic_exts_path = os.path.join(_config_path, 'exts.dic')
dic_keywords_path = os.path.join(_config_path, 'keywords.dic')

if not os.path.exists(_config_path):
    os.makedirs(_config_path)

if not os.path.exists(dic_files_path):
    with open(dic_files_path, 'w') as f:
        f.write('\n'.join(_default_dic['files']))
        f.flush()

if not os.path.exists(dic_exts_path):
    with open(dic_exts_path, 'w') as f:
        f.write('\n'.join(_default_dic['exts']))
        f.flush()

if not os.path.exists(dic_keywords_path):
    with open(dic_keywords_path, 'w') as f:
        f.write('\n'.join(_default_dic['keywords']))
        f.flush()


def cprint(*args):
    if args[-1] == '\r':
        sys.stdout.write(''.join(args[:-1])+CEND+'\r')
    else:
        sys.stdout.write(''.join(args)+CEND+'\n')

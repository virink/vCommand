#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/27, 10:23
"""

import requests
import json
import time

URL = "https://crt.sh/?q={domain}&output=json"


def func_ctfr(*args):
    """CFTR 查询子域名 Search By https://crt.sh"""
    arg = args[0]
    url = URL.format(domain=arg)
    ret = {}
    res = requests.get(url)
    if res.status_code == 200:
        jsonObj = json.loads(res.content)
        for obj in jsonObj:
            if obj["name_value"] not in ret:
                ret.update({obj["name_value"]: obj})
        ret = ["[+]     %s  %s" %
               (ret[u]['min_entry_timestamp'], u) for u in ret]
    return ('[+] Target : %s\n' % url)+'\n'.join(ret)


if __name__ == "__main__":
    domain = '%.52dandan.xyz'
    res = func_ctfr(domain)
    print(res)

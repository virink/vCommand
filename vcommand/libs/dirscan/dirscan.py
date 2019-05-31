#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/05/30, 14:25
"""

import requests as _req
import uuid
import random
import string
import asyncio
import urllib3
import difflib

from config import *

urllib3.disable_warnings()

requests = _req.Session()
requests.verify = False
requests.cert = False
# requests.max_redirects = 1
requests.proxies = {k: os.environ['ALL_PROXY'] for k in [
    'http', 'https'] if 'ALL_PROXY' in os.environ}


class Scanner():

    def __init__(self, url, req, files=[], keywords=[]):
        self.log = []
        self.redirects = []
        self.not_found_url = []
        self.q = asyncio.Queue(maxsize=MAX_QUEUE_NUM)
        self.url = self._init_url(url)
        self._get_files(keywords)
        _len, req = self._detect()
        print(_len, req)
        self.req = req
        self.len = _len
        # self.log = {self._getname(url): []}

    def start(self):
        if not self.req:
            return False
        loop = asyncio.get_event_loop()
        tasks = [self.run() for i in range(NUMBER_OF_THREAD)]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        return self.log

    async def run(self):
        while not self.q.empty():
            file = await self.q.get()
            try:
                url = self.url + file
                r = self.req(url, timeout=TIME_OUT, allow_redirects=False)
                if r.status_code in ['301', '302', 301, 302]:  # and \
                    print(r.headers.get('Location'))
                    if r.headers.get('Location') in self.not_found_url:
                        await asyncio.sleep(0.05)
                        continue
                self.display(r, file)
                await asyncio.sleep(0.05)
            except:
                continue

    def display(self, r, file):
        """判断逻辑+显示"""
        if self.len == -1:
            if r.status_code not in INVALID_CODE:
                cprint(CGREEN, '[{}] => {}{}'.format(
                    r.status_code, file, ' '*50))
                self.log[file] = r.status_code
            else:
                cprint(CRED, '[{}] => {}{}'.format(
                    r.status_code, file, ' '*50), '\r')
        else:
            if len(r.text) != self.len and r.status_code not in INVALID_CODE:
                cprint(CGREEN, '[{}] => {}{}'.format(
                    r.status_code, file, ' '*50))
                self.log[file] = r.status_code
            else:
                cprint(CRED, '[{}] => {}{}'.format(
                    r.status_code, file, ' ' * 50), '\r')

    def _getname(self, url):
        r = re.match(r'http[s]?://([\\\.\w\d:/]+)/', url).group(1)
        r = r.replace(':', '.').replace('/', '.').replace('\\', '.')
        return r+'.log'

    def _init_url(self, url):
        ''' 处理成标准的url格式'''
        if not url.startswith('http'):
            url = 'http://'+url
        if not url.endswith('/'):
            url = url + '/'
        return url

    def _detect(self):
        """识别模式"""
        try:
            rand1 = ''.join(random.sample(string.ascii_letters, 8))
            rand2 = uuid.uuid4()
            rand3 = random.randint(1000000, 99999999)
            r1 = requests.get(self.url+str(rand1), allow_redirects=False)
            r2 = requests.get(self.url+str(rand2)+'/' +
                              str(rand2), allow_redirects=False)
            r3 = requests.get(self.url + str(rand3), allow_redirects=False)
            # TODO 识别 404
            if r1.status_code == r2.status_code == r3.status_code == 200:
                if len(r1.text) == len(r2.text) == len(r3.text):
                    req = requests.get
                    # print(r1.text)
                    # print(r1.url)
                    # for k in r1.headers:
                    #     print(k, r1.headers[k])
                    return len(r1.text), req
                    # return -1, False
                else:
                    # TODO 根据相似度判断是否自定义 not found
                    d = difflib.Differ()
                    _r1 = r1.text.splitlines()
                    _r2 = r2.text.splitlines()
                    _r3 = r3.text.splitlines()
                    d12 = [i for i in list(
                        d.compare(_r1, _r2)) if i.startswith('  ')]
                    d13 = [i for i in list(
                        d.compare(_r1, _r3)) if i.startswith('  ')]
                    d23 = [i for i in list(
                        d.compare(d12, d13)) if i.startswith('  ')]
                    print(d23, len(d23))
                    return -2, False
            elif r1.status_code == r2.status_code == r3.status_code == 302 or \
                    r1.status_code == r2.status_code == r3.status_code == 301:
                if r1.headers.get('Location') == r2.headers.get('Location') \
                        == r3.headers.get('Location'):
                    self.not_found_url.append(
                        r1.headers.get('Location').strip())
                print(r1.headers.get('Location').strip())req = requests.get
                return -3, req
            else:
                if REQUEST_METHOD == 1:
                    req = requests.head
                elif REQUEST_METHOD == 2:
                    req = requests.get
                return -3, req
        except Exception as e:
            print("[!] Error : %s" % e)
        return -9, False

    def _generate_dict(self, keywords, exts):
        for e in exts:
            for kw in keywords:
                yield e.replace('$', kw)

    def _get_files(self, _keywords=[]):
        # get files
        with open(dic_files_path, 'r') as f:
            files = f.readlines()
        # get exts
        with open(dic_exts_path, 'r') as f:
            exts = [ext.strip() for ext in f.readlines()]
        # get keywords
        with open(dic_keywords_path, 'r') as f:
            keywords = [kw.strip() for kw in f.readlines()]
        if len(_keywords) > 0:
            keywords += [kw.strip() for kw in _keywords]
        # generate keywords dict
        for i in self._generate_dict(keywords, exts):
            files.append(i)
        files = list(set([file for file in files]))
        [self.q.put_nowait(file) for file in files]
        return True


def main_dirscan(*args):
    url = args[0]
    keywords = args[1:] if len(args) > 1 else[]
    scan = Scanner(url, keywords)
    scan.start()


if __name__ == "__main__":
    main_dirscan("www.baidu.com")

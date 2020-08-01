#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
古いファイルを削除する
"""

import argparse
from operator import itemgetter
import logging
import os

from pathlib import Path
import sys
from urllib.parse import urljoin, urlsplit
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument('-i', '--int-data', type=int, default=0, help='')
    # parser.add_argument('-b', '--bool-data', action='store_true', help='')
    # parser.add_argument('-c', '--counter', type=int, const=50, nargs='?', help='')
    # parser.add_argument('userid', type=int, help='')
    # parser.add_argument('filenames', nargs='+', help='')
    args = parser.parse_args()

    rm_files_cnt = 0

    local_path_pdf = Path("./pdf")
    logger.warning('対象パス：' + str(local_path_pdf))
    
    filelists = []
    for file in os.listdir():
        base, ext = os.path.splitext(local_path_pdf)
        if ext == '.pdf':
            filelists.append([file, os.path.getctime(local_path_pdf)])
    filelists.sort(key=itemgetter(1), reverse=True)
    MAX_CNT = 0
    for i,file in enumerate(filelists):
        if i > MAX_CNT - 1:
            rm_files_cnt = rm_files_cnt + 1
            #print('{}は削除します'.format(file[0]))
            logger.warning('{}は削除します'.format(file[0]))

    # 削除ファイル数をログ出力＆ダミー戻り値設定
    logger.warning('削除ファイル数：' + str(rm_files_cnt))
    print('dummy')


if __name__ == '__main__':
    main()

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

    MAX_CNT = 30

    os.system('git rm ./csv/2020041701.csv')
    
    # PDF削除
    rm_files_cnt = 0
    local_path_pdf = Path("./pdf")
    logger.warning('対象パス：' + str(local_path_pdf))
    
    filelists_pdf = []
    for file in os.listdir(local_path_pdf):
        base, ext = os.path.splitext(file)
        if ext == '.pdf':
            #filelists_pdf.append([file, os.path.getctime(str(local_path_pdf) + "/" + file)])
            filestr = str(base)
            filelists_pdf.append([file, filestr[0:10]])
    filelists_pdf.sort(key=itemgetter(1), reverse=True)
    for i,file in enumerate(filelists_pdf):
        if i > MAX_CNT - 1:
            rm_files_cnt = rm_files_cnt + 1
            #print('{}を削除します'.format(file[0]))
            logger.warning('{}を削除します'.format(file[0]))
            os.remove(str(local_path_pdf) + "/" + file[0])
    
    # 削除ファイル数をログ出力
    logger.warning('PDF削除ファイル数：' + str(rm_files_cnt))
    
    # CSV削除
    rm_files_cnt = 0
    local_path_csv = Path("./csv")
    logger.warning('対象パス：' + str(local_path_csv))
    
    filelists_csv = []
    for file in os.listdir(local_path_csv):
        base, ext = os.path.splitext(file)
        if ext == '.csv':
            #filelists_csv.append([file, os.path.getctime(str(local_path_csv) + "/" + file)])
            filestr = str(base)
            filelists_csv.append([file, filestr[0:10]])
    filelists_csv.sort(key=itemgetter(1), reverse=True)
    for i,file in enumerate(filelists_csv):
        if i > MAX_CNT - 1:
            rm_files_cnt = rm_files_cnt + 1
            #print('{}を削除します'.format(file[0]))
            logger.warning('{}を削除します'.format(file[0]))
            os.remove(str(local_path_csv) + "/" + file[0])
    
    # 削除ファイル数をログ出力
    logger.warning('CSV削除ファイル数：' + str(rm_files_cnt))


if __name__ == '__main__':
    main()

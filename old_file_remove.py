import os
import logging
from pathlib import Path
from operator import itemgetter


filelists = []
for file in os.listdir():
    base, ext = os.path.splitext(file)
    if ext == '.zip':
        filelists.append([file, os.path.getctime(file)])
filelists.sort(key=itemgetter(1), reverse=True)
MAX_CNT = 0
for i,file in enumerate(filelists):
    if i > MAX_CNT - 1:
        #print('{}は削除します'.format(file[0]))
        logger.warning('{}は削除します'.format(file[0]))
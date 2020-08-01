import os
import logging
from pathlib import Path
from operator import itemgetter


local_pdf_path = Path("pdf")
filelists = []
for file in os.listdir():
    base, ext = os.path.splitext(local_pdf_path)
    if ext == '.zip':
        filelists.append([file, os.path.getctime(local_pdf_path)])
filelists.sort(key=itemgetter(1), reverse=True)
MAX_CNT = 0
for i,file in enumerate(filelists):
    if i > MAX_CNT - 1:
        #print('{}は削除します'.format(file[0]))
        logger.warning('{}は削除します'.format(file[0]))
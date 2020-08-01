import os
import logging
from pathlib import Path
from operator import itemgetter


local_pdf_path = Path('pdf')
filelists = []
for file in os.listdir():
    base, ext = os.path.splitext(file)
    if ext == '.zip':
        filelists.append([file, os.path.getctime(file)])
filelists.sort(key=itemgetter(1), reverse=True)
MAX_CNT = 0
for i,file in enumerate(filelists):
    if i > MAX_CNT - 1:
        #print('{}‚Ííœ‚µ‚Ü‚·'.format(file[0]))
        logger.warning('{}‚Ííœ‚µ‚Ü‚·'.format(file[0]))
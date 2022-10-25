#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import defaultdict
import re
import logging
import os

logger = logging.getLogger(__name__)


# def main():
#     parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
#     parser.add_argument('filename', type=str, help='別紙 PDF のファイル名')
#     args = parser.parse_args()
# 
#     logging.basicConfig(level=os.getenv("LOGGING_LEVEL", "INFO"))
# 
#     strSplitNum = [];
#     strSplitName = [];
#     cntSplitNum = 0;
#     cntSplitName = 0;
#     
#     # CSVファイルオープン
#     f = open(args.filename, 'r', encoding='UTF-8')
#     csvData = f.read()
#     f.close()
# 
#     strSplit = csvData.split('\n', 1)
#     csvData_Name = '';
#     
#     for strSplit_for in strSplit:
#         strSplit_sub = strSplit_for.split();
#         for strSplit_sub_for in strSplit_sub:
#             strSplit_sub_for = strSplit_sub_for.replace(",", "")
#             if isonlynum(strSplit_sub_for) == True:
#                 cntSplitNum = cntSplitNum + 1
#                 strSplitNum.append(strSplit_sub_for);
#             if cntSplitNum > 11:
#                 break
#             #logger.warning("strSubst:" + strSplit_sub_for);
# 
#     
#     csvData = "";
#     i = 0;
#     while i < cntSplitNum:
#         csvData = csvData + getAgeName(i) + "," + strSplitNum[i]  + "\n";
#         i = i + 1;
#     csvData = csvData[0: len(csvData) - 1];
#     print(f"{csvData}")
# 
# def isonlynum(s):
#     return True if re.fullmatch('[0-9]+', s) else False
# 
# def getAgeName(cnt):
#     sRet = "不明"
#     if cnt == 0:
#         sRet = "10歳未満"
#     elif cnt == 1:
#         sRet = "10代"
#     elif cnt == 2:
#         sRet = "20代"
#     elif cnt == 3:
#         sRet = "30代"
#     elif cnt == 4:
#         sRet = "40代"
#     elif cnt == 5:
#         sRet = "50代"
#     elif cnt == 6:
#         sRet = "60代"
#     elif cnt == 7:
#         sRet = "70代"
#     elif cnt == 8:
#         sRet = "80代"
#     elif cnt == 9:
#         sRet = "90代"
#     elif cnt == 10:
#         sRet = "100歳以上"
#     return sRet
# 
# if __name__ == '__main__':
#     main()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', type=str, help='別紙 PDF のファイル名')
    args = parser.parse_args()

    logging.basicConfig(level=os.getenv("LOGGING_LEVEL", "INFO"))

    strSplitNum = [];
    strSplitName = [];
    cntSplitNum = 0;
    cntSplitName = 0;
    
    # CSVファイルオープン
    f = open(args.filename, 'r', encoding='UTF-8')
    csvData = f.read()
    f.close()

    strSplit = csvData.split('\n', 1)
    csvData_Name = '';
    getStartFlg = 0;
    cntTmpNum = 0;
    cntTmpNumCnt = 0;
    getTmpNumFlg = 0;
    
    for strSplit_for in strSplit:
        strSplit_sub = strSplit_for.split();
        for strSplit_sub_for in strSplit_sub:
            strSplit_sub_for = strSplit_sub_for.replace(",", "")
            if strSplit_sub_for == '合計' or strSplit_sub_for == '登録ｾﾝﾀｰ':
                getStartFlg += 1;
            elif getStartFlg == 2 and isonlynum(strSplit_sub_for) == True:
                cntTmpNum += int(strSplit_sub_for);
                cntTmpNumCnt += 1;
                if cntTmpNumCnt == 3:
                    # 10歳未満
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 4:
                    # 10代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 5:
                    # 20代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 6:
                    # 30代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 7:
                    # 40代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 8:
                    # 50代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 10:
                    # 60代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 11:
                    # 70代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 12:
                    # 80代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 13:
                    # 90代
                    getTmpNumFlg = 1;
                elif cntTmpNumCnt == 14:
                    # 不明
                    getTmpNumFlg = 1;
                else:
                    getTmpNumFlg = 0;
                
                if getTmpNumFlg == 1:
                    cntSplitNum = cntSplitNum + 1
                    # strSplitNum.append(strSplit_sub_for);
                    strSplitNum.append(str(cntTmpNum));
                    cntTmpNum = 0;
                    getTmpNumFlg = 0;
                    
                
            if cntSplitNum > 11:
                break
            #logger.warning("strSubst:" + strSplit_sub_for);
            #logger.warning("getStartFlg:" + str(getStartFlg) + " || strSplit_sub_for:" + strSplit_sub_for);

    
    csvData = "";
    i = 0;
    while i < cntSplitNum:
        csvData = csvData + getAgeName(i) + "," + strSplitNum[i]  + "\n";
        i = i + 1;
    csvData = csvData[0: len(csvData) - 1];
    print(f"{csvData}")

def isonlynum(s):
    return True if re.fullmatch('[0-9]+', s) else False

def getAgeName(cnt):
    sRet = "不明"
    if cnt == 0:
        sRet = "10歳未満"
    elif cnt == 1:
        sRet = "10代"
    elif cnt == 2:
        sRet = "20代"
    elif cnt == 3:
        sRet = "30代"
    elif cnt == 4:
        sRet = "40代"
    elif cnt == 5:
        sRet = "50代"
    elif cnt == 6:
        sRet = "60代"
    elif cnt == 7:
        sRet = "70代"
    elif cnt == 8:
        sRet = "80代"
    elif cnt == 9:
        sRet = "90代"
#     elif cnt == 10:
#         sRet = "100歳以上"
    elif cnt == 10:
        sRet = "不明"

    return sRet

if __name__ == '__main__':
    main()
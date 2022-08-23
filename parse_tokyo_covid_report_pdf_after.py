#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import defaultdict
import re
import logging
import os

logger = logging.getLogger(__name__)


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

    strSplit = csvData.split(',', 1)
    if strSplit[0] != '千代田':
        csvData_Name = '';
        
        i = csvData.find("'");
        while True:
            if i > -1:
                j = csvData.find("'", i + 1);
                csvData_Name = csvData_Name + csvData[i + 1: j];
                i = j + 1;
                i = csvData.find("'" , i );
            else:
                break
        
        i = csvData_Name.find('千代田');
        csvData_Name = csvData_Name[i:];
        strSplit = csvData_Name.split();
        #logger.warning("csvData_Name:" + csvData_Name);
        
        for strSplit_for in strSplit:
            #logger.warning("strSplit_for:" + strSplit_for);
            strSplit_sub = strSplit_for.split('\\n');
            for strSplit_sub_for in strSplit_sub:
                #logger.warning("strSplit_sub_for:" + strSplit_sub_for);
                j = strSplit_sub_for.find('\\');
                if j > -1:
                    strSplit_sub_for = strSplit_sub_for[0: j];
                
                strSubst = strSplit_sub_for[0: 1];
                #logger.warning("strSubst:" + strSubst);
                if len(strSubst) > 0:
                    if isonlynum(strSubst) == True:
                        #logger.warning("Num:" + strSplit_sub_for);
                        cntSplitNum = cntSplitNum + 1;
                        strSplitNum.append(strSplit_sub_for);
                    elif strSubst != '(':
                        #logger.warning("Name:" + strSplit_sub_for);
                        cntSplitName = cntSplitName + 1;
                        strSplitName.append(strSplit_sub_for);
                    #else:
                        #logger.warning("それ以外:");
                
            
        #logger.warning(str(cntSplitName) + "/" +  str(cntSplitNum));
        
        if cntSplitNum < cntSplitName:
            cntSplitName = cntSplitNum;
        elif cntSplitName < cntSplitNum:
            cntSplitNum = cntSplitName;
        
        csvData = "";
        i = 0;
        while i < cntSplitNum:
            csvData = csvData + strSplitName[i] + "," + strSplitNum[i]  + "\n";
            i = i + 1;
        
        csvData = csvData[0: len(csvData) - 1];
        
        #logger.warning(str(cntSplitNum));
        #logger.warning(csvData);
        
    
    print(f"{csvData}")

def isonlynum(s):
    return True if re.fullmatch('[0-9]+', s) else False

if __name__ == '__main__':
    main()

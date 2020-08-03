#!/bin/bash

# 古いファイルを削除
#./oldfiles_remove.py
echo "不要ファイル削除（csv）"

TARGET_DIR=./csv
#DELETE_DAY=`date "+%Y%m%d" --date '30 days ago'`
DELETE_FILE_MAX=30

cd $TARGET_DIR
FILE_LIST=`ls "-r"`

DELETE_FILE_CNT=0
for FILE in $FILE_LIST
do
 # ファイル名にYYYYMMDDを含む
 if [[ ${FILE} =~ 202[0-9]{5} ]]
 then

  # ファイル名日付部分を取り出す
  #FILE_DATE=`expr "${FILE}" : ".*\(202[0-9]\{5\}\)"`

  # 日付を比較して削除
  #if [ ${FILE_DATE} -lt ${DELETE_DAY} ]
  #then
  # #rm ${FILE}
  # #git rm ./csv/"${FILE}"
  # echo "./csv/"${FILE}"は削除します"
  #fi
  
  DELETE_FILE_CNT=$(expr $DELETE_FILE_CNT + 1)
  if [ ${DELETE_FILE_CNT} -gt ${DELETE_FILE_MAX} ]
  then
    git rm "${FILE}"
    echo ""$TARGET_DIR"/"${FILE}"は削除します"
  fi
 fi
done
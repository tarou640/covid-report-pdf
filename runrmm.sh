#!/bin/bash

echo "不要ファイル削除（csv）"

TARGET_DIR=/csv
DELETE_DAY=`date +"%Y%m%d" -d '14 days ago'`

cd $TARGET_DIR
FILE_LIST=`ls`

for FILE in $FILE_LIST
do
 # ファイル名にYYYYMMDDを含む
 if [[ ${FILE} =~ 201[0-9]{5} ]]
 then

  # ファイル名日付部分を取り出す
  FILE_DATE=`expr "${FILE}" : ".*\(201[0-9]\{5\}\)"`

  # 日付を比較して削除
  if [ ${FILE_DATE} -lt ${DELETE_DAY} ]
  then
   #rm ${FILE}
   echo ${FILE} "は削除します"
  fi
 fi
done
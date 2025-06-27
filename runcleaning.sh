#!/bin/bash

# 古いファイルを削除
echo "## 不要ファイル削除処理 開始"

DELETE_FILE_MAX=30

# datファイル
echo "## 削除処理（dat）"

TARGET_DIR=../dat
cd $TARGET_DIR
FILE_LIST=`ls "-r"`

FILE_CNT=0
DELETE_FILE_CNT=0
for FILE in $FILE_LIST
do
 # ファイル名にYYYYMMDDを含む
 if [[ ${FILE} =~ 202[0-9]{5} ]]
 then

  FILE_CNT=$(expr $FILE_CNT + 1)
  if [ ${FILE_CNT} -gt ${DELETE_FILE_MAX} ]
  then
    git rm "${FILE}"
    #echo ""$TARGET_DIR"/"${FILE}"は削除します"
    DELETE_FILE_CNT=$(expr $DELETE_FILE_CNT + 1)
  fi
 fi
done
echo "削除ファイル数（dat）:"${DELETE_FILE_CNT}""

echo "## 不要ファイル削除処理 終了"

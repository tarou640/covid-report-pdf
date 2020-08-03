#!/usr/bin/env bash

# 古いファイルを削除
#./oldfiles_remove.py
echo "不要ファイル削除（csv）"

TARGET_DIR=./csv
DELETE_DAY=`date "+%Y%m%d" --date '30 days ago'`

cd $TARGET_DIR
FILE_LIST=`ls`

for FILE in $FILE_LIST
do
 # ファイル名にYYYYMMDDを含む
 if [[ ${FILE} =~ 202[0-9]{5} ]]
 then

  # ファイル名日付部分を取り出す
  FILE_DATE=`expr "${FILE}" : ".*\(202[0-9]\{5\}\)"`

  # 日付を比較して削除
  if [ ${FILE_DATE} -lt ${DELETE_DAY} ]
  then
   #rm ${FILE}
   git rm ./csv/"${FILE}"
   echo "./csv/"${FILE}"は削除します"
  fi
 fi
done

TARGET_DIR=../
cd $TARGET_DIR

# PDF をとってくる
NEW_PDF_FILE=$(./fetch_tokyo_covid_report_pdf.py)
if [[ -z "${NEW_PDF_FILE}" ]] ;then
  echo "No new PDF. exited"
  exit 255
fi

# PDF から CSV を生成
NEW_CSV_FILE=${NEW_PDF_FILE//pdf/csv}
./parse_tokyo_covid_report_pdf.py ${NEW_PDF_FILE} > ${NEW_CSV_FILE}

# もしファイル名の末尾に数字がついていたら、日付のみの csv も作る
DAY_CSV_FILE=${NEW_CSV_FILE:0:12}.csv
if [[ ${NEW_CSV_FILE} != ${DAY_CSV_FILE} ]]; then
  cp "${NEW_CSV_FILE}" "${DAY_CSV_FILE}"
fi

# latest.csv のコピーを生成
cp "${NEW_CSV_FILE}" csv/latest.csv

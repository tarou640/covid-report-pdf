#!/usr/bin/env bash

# PDF をとってくる
NEW_PDF_FILE=$(./fetch_tokyo_covid_report_pdf.py)
if [[ -z "${NEW_PDF_FILE}" ]] ;then
  echo "No new PDF. exited"
  exit 255
fi

# 市区町村別の感染者情報
# PDF から CSV を生成
NEW_CSV_FILE=${NEW_PDF_FILE//pdf/csv}
./parse_tokyo_covid_report_pdf.py ${NEW_PDF_FILE} > ${NEW_CSV_FILE}

# もしファイル名の末尾に数字がついていたら、日付のみの csv も作る
DAY_CSV_FILE=${NEW_CSV_FILE:0:12}.csv
if [[ ${NEW_CSV_FILE} != ${DAY_CSV_FILE} ]]; then
  cp "${NEW_CSV_FILE}" "${DAY_CSV_FILE}"
fi

# 年齢別の感染者情報
# PDF から CSF（便宜上CSFとしたけど中身はCSV）を生成
NEW_CSF_FILE=${NEW_PDF_FILE//pdf/csf}
./parse_tokyo_covid_report_age.py ${NEW_PDF_FILE} > ${NEW_CSF_FILE}

# もしファイル名の末尾に数字がついていたら、日付のみの csf も作る
DAY_CSF_FILE=${NEW_CSF_FILE:0:12}.csf
if [[ ${NEW_CSF_FILE} != ${DAY_CSF_FILE} ]]; then
  cp "${NEW_CSF_FILE}" "${DAY_CSF_FILE}"
fi

# latest.csv のコピーを生成
cp "${NEW_CSV_FILE}" csv/latest.csv
cp "${NEW_CSF_FILE}" csf/latest.csf


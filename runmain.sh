#!/usr/bin/env bash

TARGET_URL="https://survey.tmiph.metro.tokyo.lg.jp/epidinfo/weeklyhc.do"
TEMP_FILE="temp.dat"

# 更新日付 をとってくる
NEW_DAT_FILE=$(./parse_tokyo_covid_report_updt.py ${TARGET_URL})
if [ -z "$NEW_DAT_FILE" ]; then
  echo "エラー: NEW_DAT_FILE が未設定または空です。"
  exit 255
fi
if [ -e "$NEW_DAT_FILE" ]; then
  echo "エラー: ファイル '$NEW_DAT_FILE' はすでに存在しています。"
  exit 255
fi

# 都の感染者情報から市区町村別の感染者情報を抜粋する
./parse_tokyo_covid_report_main.py ${TARGET_URL} > ${NEW_DAT_FILE}
if [ ! -f "$NEW_DAT_FILE" ]; then
  echo "エラー: ファイルが存在しません: $NEW_DAT_FILE"
  exit 255
fi
if [ ! -s "$NEW_DAT_FILE" ]; then
  echo "ファイルが空です: $NEW_DAT_FILE"
  exit 255
fi

# latest.csv のコピーを生成
cp "${NEW_DAT_FILE}" dat/latest.dat

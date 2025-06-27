#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import urllib.request
import re
from pathlib import Path

#
def fetch_html(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8', errors='replace')

def extract_end_date(html):
    # 対象期間：2025年6月9日 - 2025年6月15日
    pattern = r"対象期間：\s*(\d{4})年(\d{1,2})月(\d{1,2})日\s*[-～]\s*(\d{4})年(\d{1,2})月(\d{1,2})日"
    match = re.search(pattern, html)
    if not match:
        return None

    # 終了日（右側の日付）
    year, month, day = match.group(4), match.group(5), match.group(6)
    return f"{int(year):04d}{int(month):02d}{int(day):02d}"

def main():
    if len(sys.argv) != 2:
        print("使い方: python get_period_end.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        html = fetch_html(url)
        end_date = extract_end_date(html)
        if end_date:
            local_path = Path("dat") / f"{end_date}.dat"
            print(local_path)
        else:
            print("")
    except Exception as e:
        print("")

if __name__ == "__main__":
    main()
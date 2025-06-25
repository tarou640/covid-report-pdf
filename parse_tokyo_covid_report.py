import sys
import urllib.request
import re

#
def fetch_html(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8', errors='replace')

def extract_period_end_date(html):
    # 例: 対象期間：2025年6月9日 - 2025年6月15日
    pattern = r"対象期間：\s*\d{4}年\d{1,2}月\d{1,2}日\s*[-～]\s*(\d{4})年(\d{1,2})月(\d{1,2})日"
    match = re.search(pattern, html)
    if not match:
        return "対象期間/不明"
    
    year, month, day = match.group(1), match.group(2), match.group(3)
    formatted = f"{int(year):04d}{int(month):02d}{int(day):02d}"
    return f"対象期間/{formatted}"

def extract_24_values(html, keyword):
    td_tag = '<TD class="padright">'
    end_tag = '</TD>'

    start_pos = html.find(keyword)
    if start_pos == -1:
        return f"{keyword}/(キーワード未検出)"

    values = []
    search_pos = start_pos

    for i in range(24):
        td_start = html.find(td_tag, search_pos)
        if td_start == -1:
            values.append("0")
            break

        td_end = html.find(end_tag, td_start + len(td_tag))
        if td_end == -1:
            values.append("0")
            break

        value = html[td_start + len(td_tag):td_end].strip()
        if not value:
            value = "0"

        values.append(value)
        search_pos = td_end + len(end_tag)

    # 足りない値は 0 で補完
    while len(values) < 24:
        values.append("0")

    return f"{keyword}/" + "/".join(values)

def main():
    if len(sys.argv) != 2:
        print("使い方: python get_full_data.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    keywords = [
        "合計", "千代田", "中央区", "みなと", "新宿区", "文京", "台東", "墨田区", "江東区",
        "品川区", "目黒区", "大田区", "世田谷", "渋谷区", "中野区", "杉並", "池袋",
        "北区", "荒川区", "板橋区", "練馬区", "足立", "葛飾区", "江戸川",
        "八王子市", "町田市", "西多摩", "南多摩", "多摩立川", "多摩府中", "多摩小平", "島しょ"
    ]

    try:
        html = fetch_html(url)

        # 追加処理：対象期間の終了日を最初に出力
        period_info = extract_period_end_date(html)
        print(period_info)

        # 各キーワードのデータ出力
        for keyword in keywords:
            result = extract_24_values(html, keyword)
            print(result)

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
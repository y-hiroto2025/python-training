# 余計な記号や文字列の入った文字列データをきれいにする
# １：ユーザー名のリストを作る
# ２：タグを削除してきれいなテキストを取り出す

import re

# 課題のデータ
log_data = """
[INFO] User:Yamada Message:ご飯食べたい
[ERROR] Code:404 User:Yuuki Message:リンク切れです <a href="http://あああ.com">Link</a>
[INFO] User:Mori Message:ピザ食べたい... map_id:55
[WARNING] User:Simizu Message:在庫が足りない (item_id: 302)
"""

user_names = re.findall(r'User:(\w+)', log_data, re.MULTILINE)
# "User"に続く英数字の連続文字
print(user_names)

cleaned_log_data = re.sub(r"\[\w+\]", "", log_data)
print(cleaned_log_data)
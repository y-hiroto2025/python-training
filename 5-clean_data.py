# 余計な記号や文字列の入った文字列データをきれいにする
# １：ユーザー名のリストを作る
# ２：タグを削除してきれいなテキストを取り出す
import re

log_data = """
[INFO] User:Yamada Message:ご飯食べたい
[ERROR] Code:404 User:Asuna Message:リンク切れです <a href="http://あああ.com">Link</a>
[INFO] User:Mori Message:ピザ食べたい... map_id:55
[WARNING] User:Agil Message:在庫が足りない (item_id: 302)
"""


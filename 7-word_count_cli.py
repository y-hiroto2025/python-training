import os

def main():
    # ユーザーのファイルパス入力
    print("分析したいファイルのパスを入力してください")
    path = input().strip('"')

    # ファイルが存在すればテキストを分析する
    if not os.path.exists(path):
        print("This File Doesn't Exist.")
        return

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    words_dic = {}

    for line in lines:
        # 文字列の前処理
        line = line.strip().lower()
        line = line.replace(",", "").replace(".", "").split()

        # 文字の出現回数をカウント
        for word in line:
            if word not in words_dic:
                words_dic[word] = 1
            else:
                words_dic[word] += 1

    words_rank = []
    word_count = 0

    # [回数, 単語]のリストを作って数字でソートができるようにする
    for key, value in words_dic.items():
        words_rank.append([value, key])
        word_count += value

    # リストをソートする
    words_rank = sorted(words_rank, reverse=True)

    print("=== 分析結果 ===")
    print(f"総単語数: {word_count}")
    print("【頻出単語トップ10】")
    for i, item in enumerate(words_rank[:10]): # スライスで最大10個取り出す
        count = item[0]
        word = item[1]
        print(f"{i + 1: >2}. {word: <10}: {count:> 4}回")

if __name__ == "__main__":
    main()
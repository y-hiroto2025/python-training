# ユーザーが入力した、言葉とその意味をファイルに記録する
# add=>単語&意味を辞書に追加、ask=>入力された単語の意味を答える

def add_word(word_dict):
    word = input("word: ")
    mean = input("mean: ")
    word_dict[word] = mean

def ask_word(word_dict):
    word = input("word: ")
    if word in word_dict:
        print(f"mean => {word_dict[word]}")
    else:
        print("記録されていません")

def memorize_dict(word_dict):
    # 改善点："a"(追記)にすると辞書の中身全部がファイルの末尾に追加されるので、"w"(上書き)でいい
    with open("memory.txt", "w", encoding="utf-8") as f:
        for key, value in word_dict.items(): # 改善点：itemsを使うとすっきりする
            f.write(f"{key},{value}\n")

def main(): # 改善点：関数名を main にするのは慣習的におすすめ
    my_dict = {}

    try:
        with open("memory.txt", "r", encoding="utf-8") as f:
            # テキストファイルの文字列を辞書に変換する
            # 改善点：空行を読み込んでもエラーにならないようにする
            for line in f:
                if "," in line:
                    # 改善点： , を一回だけ分割する
                    key, value = line.strip().split(",", 1)
                    my_dict[key] = value
    except FileNotFoundError:
        # 改善点：ファイル上書きの時に勝手にファイルが新規作成されるので何もしない
        print("新規データを作成します")

    # 改善点：whileを外にだすことで、exceptになっても処理が止まらない
    while True:
            print("\nInput Your Order (add/ask/end): ", end="")
            user_order = input()

            if user_order == "add":
                add_word(my_dict)
            elif user_order == "ask":
                ask_word(my_dict)
            elif user_order == "end":
                memorize_dict(my_dict)
                print("辞書を保存しました")
                break

if __name__ == "__main__":
    main()
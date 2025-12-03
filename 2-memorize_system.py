# ユーザーが入力した、言葉とその意味をファイルに記録する
# add=>単語&意味を辞書に追加、ask=>入力された単語の意味を答える


def add_word(word_dict):
    # 入力した言葉とその意味を辞書に保存する
    print("word: ", end="")
    word = input()
    print("mean: ", end="")
    mean = input()

    word_dict[word] = mean

def ask_word(word_dict):
    print("word: ", end="")
    word = input()
    if word in word_dict:
        print(f"mean => {word_dict[word]}")
    else:
        print("記録されていません")

def memorize_dict(word_dict):
    with open("memory.txt", "a", encoding="utf-8") as f:
        word_dict_keys = word_dict.keys()
        for key in word_dict_keys:
            f.write(f"{key},{word_dict[key]}\n")

def memorize_or_ask():
    my_dict = {}
    try:
        with open("memory.txt", "r", encoding="utf-8") as f:
            # テキストファイルの文字列を辞書に変換する
            for line in f:
                key, value = line.strip().split(",")
                my_dict[key] = value

        while True:
            print("Input Your Order: ", end="")
            user_order = input()
            if user_order == "add":
                add_word(my_dict)

            elif user_order == "ask":
                ask_word(my_dict)
    
            elif user_order == "end":
                print(my_dict)
                memorize_dict(my_dict)
                print("辞書を保存しました")
                break

    except FileNotFoundError:
        with open("memory.txt", "x", encoding="utf-8") as f:
            pass

memorize_or_ask()
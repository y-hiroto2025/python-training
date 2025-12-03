my_dict = {"a": "sa", "b": "bv"}

with open("memory.txt", "a", encoding="utf-8") as f:
    my_dict_keys = my_dict.keys()
    for key in my_dict_keys:
        print(key, my_dict[key])
        f.write(f"{key},{my_dict[key]}\n")
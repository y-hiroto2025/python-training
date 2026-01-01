def flatten_data(data):
    new_data = []
    for d in data:
        if isinstance(d, int):
            new_data.append(d)
        elif isinstance(d, list):
            new_data.extend(flatten_data(d))
        else:
            pass
    return new_data


chaos_data = [
    1,
    [2, 3],
    [4, [5, 6, [7]], 8],
    "error_code",
    [[9, "warning"], 10],
    11,
    [[[12]]]
]

print(flatten_data(chaos_data))
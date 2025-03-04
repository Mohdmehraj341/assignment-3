merge_lists_to_dict = lambda keys, values: dict(zip(keys, values))


keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

result = merge_lists_to_dict(keys, values)
print(result)
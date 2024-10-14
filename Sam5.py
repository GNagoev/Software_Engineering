def unique_sorted_items(purchases):
    item_count = {}

    for item in purchases:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    sorted_items = sorted(item_count.keys())

    result = tuple((item, item_count[item]) for item in sorted_items)

    return result


print(unique_sorted_items(['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']))
print(unique_sorted_items(['carrot', 'beet', 'carrot', 'potato', 'beet', 'carrot']))
print(unique_sorted_items(['dog', 'cat', 'dog', 'mouse', 'cat', 'cat']))
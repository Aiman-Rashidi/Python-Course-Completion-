def merge_sales(store1, store2):
    to_be_returned_dict = {}
    for item_1 in store1:
        for item_2 in store2:
            if item_1 == item_2:
                to_be_returned_dict.update({item_1: store1[item_1] + store2[item_2]})
            elif item_1 not in store2:
                to_be_returned_dict.update({item_1: store1[item_1]})
            elif item_2 not in store1:
                to_be_returned_dict.update({item_2: store2[item_2]})
    return to_be_returned_dict

store1_sales = {
    "apple": 120,
    "banana": 80,
    "orange": 100
}

store2_sales = {
    "banana": 90,
    "grapes": 70,
    "apple": 130
}

print(merge_sales(store1_sales, store2_sales))
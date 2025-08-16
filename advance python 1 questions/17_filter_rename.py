def filter_and_rename_products_1(products):
    return {f"Item: {name}": products[name] for name in products if products[name] > 100}

def filter_and_rename_products_2(products):
    to_be_returned_dict = {}
    for item in products:
        if products[item] > 100:
            to_be_returned_dict.update({f"Item: {item}": products[item]})
    return to_be_returned_dict

products = {
    "notebook": 120,
    "pen": 25,
    "mouse": 550,
    "eraser": 15,
    "keyboard": 999
}

print(filter_and_rename_products_1(products))
print(filter_and_rename_products_2(products))
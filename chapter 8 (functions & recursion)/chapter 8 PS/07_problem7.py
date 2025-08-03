def remove_word_from_list(name_list, target_word):
    cleaned_names = []
    for current_name in name_list:
        if current_name != target_word:
            cleaned_names.append(current_name.strip(target_word))
    return cleaned_names

names = ["anAiman", "aHarry", "nRohan", "an", "AN"]
print(remove_word_from_list(names, "an"))
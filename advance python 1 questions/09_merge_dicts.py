dict1 = {"name": "Aiman", "age": 19}
dict2 = {"age": 20, "city": "Chennai"}

# # dict combination without mutation 
# merged1 = dict1 | dict2
# merged2 = dict2 | dict1
# print(merged1, type(merged1))
# print(merged2, type(merged2))
# print(dict1, dict2)


# # dict combination with mutation
# dict1.update(dict2)
# print(dict1, dict2)





# student_scores = {"Aiman": 85, "Lyra": 90}
# new_scores = {"Zara": 95, "Aiman": 88}

# # merging the two dictionaries without mutation
# merged_scores = student_scores | new_scores
# print(f"Merged dictionary (no mutation): {merged_scores}")

# # merging the two dictionaries with mutation
# student_scores.update(new_scores)
# print(student_scores)
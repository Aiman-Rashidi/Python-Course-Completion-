def average_score_1(math_scores, science_scores):
    average_score_dict = {}
    for math_keys in math_scores:
        for science_keys in science_scores:
            if math_keys == science_keys:
                average_score = (math_scores[math_keys] + science_scores[science_keys]) / 2
                # average_score_dict.update({math_keys: average_score})
                average_score_dict.update({science_keys: average_score})
    return average_score_dict

def average_score_2(math_scores, science_scores):
    return {student: (math_scores[student] + science_scores[student]) / 2 for student in math_scores if student in science_scores}

math_scores = {
    "Aiman": 88,
    "Zara": 76,
    "Ravi": 92
}

science_scores = {
    "Aiman": 91,
    "Zara": 82,
    "Ravi": 78
}

print(average_score_1(math_scores, science_scores))
print(average_score_2(math_scores, science_scores))
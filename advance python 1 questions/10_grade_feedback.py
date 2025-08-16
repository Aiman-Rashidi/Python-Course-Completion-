def grade_feedback(score: int) -> str:
    match score:
        case _ if 90 <= score <= 100:
            return "Excellent"
        case _ if 75 <= score < 90:
            return "Good"
        case _ if 50 <= score < 75:
            return "Needs Improvement"
        case _ if 0 <= score < 50:
            return "Fail"
        case _:
            return "Invalid score range"

while True:
    user_input = input("Enter the score or 'stop' to exit: ").strip().lower()
    if user_input == "stop":
        break
    try:
        score = int(user_input)
        print(grade_feedback(score))
    except ValueError:
        print("Enter a valid score")
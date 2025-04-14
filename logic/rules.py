def recommend_career(responses):
    score = {
        "Engineering": 0,
        "Medicine": 0,
        "Arts": 0,
        "Business": 0
    }

    for answer in responses:
        category = answer.get("category")
        if category == "analytical":
            score["Engineering"] += 1
        elif category == "social":
            score["Medicine"] += 1
        elif category == "creative":
            score["Arts"] += 1
        elif category in ["business", "leadership"]:
            score["Business"] += 1

    recommended = max(score, key=score.get)
    return recommended

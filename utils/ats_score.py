def calculate_ats_score(skills):

    total_possible_skills = 10

    score = (
        len(skills) / total_possible_skills
    ) * 100

    return round(score, 2)
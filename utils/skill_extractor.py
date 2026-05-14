skills_list = [
    'python',
    'java',
    'html',
    'css',
    'javascript',
    'sql',
    'flask',
    'react',
    'c',
    'c++'
]


def extract_skills(resume_text):

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills_list:

        if skill in resume_text:
            found_skills.append(skill)

    return found_skills
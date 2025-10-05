def extract_skills(text):
    keywords = ["python", "sql", "machine learning", "data analysis", "c++", "java"]
    found = []
    for word in keywords:
        if word in text.lower():
            found.append(word)
    return found

if __name__ == "__main__":
    print(extract_skills("I know python, SQL, and Machine Learning"))

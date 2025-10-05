def score_candidate(skills):
    """
    Simple score based on skill count.
    Args:
        skills (list): List of skills
    Returns:
        int: Candidate score
    """
    return len(skills) * 10

if __name__ == "__main__":
    print(score_candidate(["python", "sql", "machine learning"]))

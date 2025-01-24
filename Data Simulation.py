import pandas as pd
import numpy as np

# Simulate Current Quiz Data
current_quiz_data = {
    "QuestionID": [1, 2, 3, 4, 5],
    "Topic": ["Biology", "Chemistry", "Physics", "Biology", "Physics"],
    "Difficulty": ["Easy", "Medium", "Hard", "Medium", "Easy"],
    "Correct": [1, 0, 0, 1, 1],  # 1 = Correct, 0 = Incorrect
}

current_quiz_df = pd.DataFrame(current_quiz_data)

# Simulate Historical Quiz Data (last 5 quizzes)
historical_quiz_data = {
    "QuizID": [1, 2, 3, 4, 5],
    "Biology Accuracy": [0.8, 0.6, 0.7, 0.9, 0.85],
    "Chemistry Accuracy": [0.7, 0.5, 0.6, 0.65, 0.75],
    "Physics Accuracy": [0.6, 0.55, 0.7, 0.6, 0.65],
    "Average Score": [75, 65, 70, 80, 78],
}

historical_quiz_df = pd.DataFrame(historical_quiz_data)

# Print the datasets
print("Current Quiz Data:\n", current_quiz_df)
print("\nHistorical Quiz Data:\n", historical_quiz_df)

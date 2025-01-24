# Analyze Current Quiz Data
def analyze_current_quiz(df):
    topic_analysis = df.groupby("Topic").agg(
        Total_Questions=("QuestionID", "count"),
        Correct_Answers=("Correct", "sum"),
    )
    topic_analysis["Accuracy"] = (topic_analysis["Correct_Answers"] / topic_analysis["Total_Questions"]) * 100
    return topic_analysis

current_quiz_analysis = analyze_current_quiz(current_quiz_df)
print("\nCurrent Quiz Analysis:\n", current_quiz_analysis)

# Analyze Historical Quiz Data
def analyze_historical_quiz(df):
    topic_trends = df.iloc[:, 1:-1]  # Exclude QuizID and Average Score
    avg_accuracy = topic_trends.mean().to_dict()
    return avg_accuracy

historical_trends = analyze_historical_quiz(historical_quiz_df)
print("\nHistorical Trends:\n", historical_trends)

# Generate Recommendations
def generate_recommendations(current_analysis, historical_trends):
    recommendations = []
    for topic, stats in current_analysis.iterrows():
        current_accuracy = stats["Accuracy"]
        historical_accuracy = historical_trends.get(f"{topic} Accuracy", 0)

        if current_accuracy < 70:  # Weak topic threshold
            recommendations.append(f"Focus more on {topic}. Current accuracy is {current_accuracy:.2f}%.")
        elif current_accuracy > historical_accuracy:
            recommendations.append(f"Good improvement in {topic}! Keep practicing to maintain accuracy.")
        else:
            recommendations.append(f"{topic}: Review advanced questions to further strengthen your skills.")
    return recommendations

recommendations = generate_recommendations(current_quiz_analysis, historical_trends)
print("\nPersonalized Recommendations:\n")
for rec in recommendations:
    print("-", rec)

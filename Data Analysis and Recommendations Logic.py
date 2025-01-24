import pandas as pd

# Function to analyze historical and current quiz data
def analyze_data(historical_quiz_data, current_quiz_data):
    # Example analysis: Calculate the number of correct responses per topic
    historical_performance = historical_quiz_data.groupby('Topic')['Correct'].sum()
    current_performance = current_quiz_data.groupby('Topic')['Correct'].sum()

    # Example: Find topics with low performance
    weak_areas = current_performance[current_performance < historical_performance].index.tolist()

    # Return a simple result for now
    return {
        'historical_performance': historical_performance.to_dict(),
        'current_performance': current_performance.to_dict(),
        'weak_areas': weak_areas
    }

# Function to generate personalized recommendations
def generate_recommendations(analysis_result):
    weak_areas = analysis_result['weak_areas']
    
    recommendations = []
    for area in weak_areas:
        recommendations.append(f"Focus more on the topic: {area}")
    
    # Additional recommendations based on analysis (e.g., improvement in specific areas)
    if len(weak_areas) == 0:
        recommendations.append("Great job! Keep practicing.")
    
    return {'recommendations': recommendations}

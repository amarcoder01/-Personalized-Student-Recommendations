from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated datasets for demonstration
current_quiz_data = {
    'topics': ['Math', 'Physics', 'Chemistry', 'Biology'],
    'performance': [75, 65, 85, 90]  # Representing accuracy % per topic
}

historical_performance = {
    'Math': {'accuracy': [70, 75, 80], 'improvement': True},
    'Physics': {'accuracy': [65, 60, 55], 'improvement': False},
    'Chemistry': {'accuracy': [90, 85, 88], 'improvement': True},
    'Biology': {'accuracy': [95, 93, 90], 'improvement': False}
}

# Helper function to generate the student persona
def generate_student_persona(current_analysis, historical_trends):
    persona = {}
    strengths = []
    weaknesses = []
    improving_areas = []
    
    for topic, score in zip(current_analysis['topics'], current_analysis['performance']):
        historical_accuracy = historical_trends.get(topic, {'accuracy': []})['accuracy'][-1]
        
        if score >= 80:
            strengths.append(topic)
        elif score < 70:
            weaknesses.append(topic)
        
        if historical_accuracy < score:
            improving_areas.append(topic)
    
    if len(strengths) >= 3 and len(weaknesses) == 0:
        persona["Type"] = "High Performer"
    elif len(improving_areas) >= 2:
        persona["Type"] = "Steady Improver"
    elif len(strengths) >= 2 and len(weaknesses) >= 2:
        persona["Type"] = "Topic Specialist"
    else:
        persona["Type"] = "Needs Attention"
    
    persona["Strengths"] = strengths
    persona["Weaknesses"] = weaknesses
    persona["Improving Areas"] = improving_areas
    
    return persona

# Route to analyze performance and generate persona and recommendations
@app.route('/analyze_performance', methods=['POST'])
def analyze_performance():
    data = request.get_json()  # Get data from the user
    current_analysis = {
        'topics': data['topics'],
        'performance': data['performance']
    }
    student_persona = generate_student_persona(current_analysis, historical_performance)
    
    return jsonify({
        'student_persona': student_persona,
        'message': 'Performance analyzed successfully!'
    })

# Route to generate recommendations based on persona
@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
    data = request.get_json()  # Get the student persona
    persona = data['student_persona']
    
    recommendations = []
    
    if persona['Type'] == "High Performer":
        recommendations.append("Keep practicing advanced questions in your strengths.")
    elif persona['Type'] == "Steady Improver":
        recommendations.append("Focus on your weak areas, particularly Physics.")
    elif persona['Type'] == "Topic Specialist":
        recommendations.append("Broaden your skills by working on weaker topics.")
    else:
        recommendations.append("Focus on building foundational knowledge and practice more.")
    
    return jsonify({
        'recommendations': recommendations
    })

# Route to get the student persona
@app.route('/get_student_persona', methods=['GET'])
def get_student_persona():
    student_persona = generate_student_persona(current_quiz_data, historical_performance)
    return jsonify({
        'student_persona': student_persona
    })

if __name__ == '__main__':
    app.run(debug=True)

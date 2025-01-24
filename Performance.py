def generate_student_persona(current_analysis, historical_trends):
    persona = {}
    strengths = []
    weaknesses = []
    improving_areas = []
    
    # Analyze strengths and weaknesses
    for topic, row in current_analysis.iterrows():
        accuracy = row["Accuracy"]
        historical_accuracy = historical_trends.get(f"{topic} Accuracy", 0)
        
        if accuracy >= 80:
            strengths.append(topic)
        elif accuracy < 70:
            weaknesses.append(topic)
        
        # Identify improvement trends
        if historical_accuracy < accuracy:
            improving_areas.append(topic)
    
    # Define persona
    if len(strengths) >= 3 and len(weaknesses) == 0:
        persona["Type"] = "High Performer"
    elif len(improving_areas) >= 2:
        persona["Type"] = "Steady Improver"
    elif len(strengths) >= 2 and len(weaknesses) >= 2:
        persona["Type"] = "Topic Specialist"
    else:
        persona["Type"] = "Needs Attention"
    
    # Add details to persona
    persona["Strengths"] = strengths
    persona["Weaknesses"] = weaknesses
    persona["Improving Areas"] = improving_areas
    
    return persona

# Generate persona for the student
student_persona = generate_student_persona(current_quiz_analysis, historical_trends)

# Display the persona
print("Student Persona:")
print(f"Type: {student_persona['Type']}")
print(f"Strengths: {', '.join(student_persona['Strengths']) if student_persona['Strengths'] else 'None'}")
print(f"Weaknesses: {', '.join(student_persona['Weaknesses']) if student_persona['Weaknesses'] else 'None'}")
print(f"Improving Areas: {', '.join(student_persona['Improving Areas']) if student_persona['Improving Areas'] else 'None'}")

from flask import Flask, request, jsonify
import pandas as pd
from analysis import analyze_data, generate_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Personalized Student Recommendations API!"

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the data from the POST request
    data = request.get_json()
    
    # Process the current quiz data
    current_quiz_data = pd.DataFrame(data['current_quiz_data'])
    
    # Process the historical quiz data
    historical_quiz_data = pd.DataFrame(data['historical_quiz_data'])

    # Analyze data
    analysis_result = analyze_data(historical_quiz_data, current_quiz_data)
    
    # Generate recommendations
    recommendations = generate_recommendations(analysis_result)
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

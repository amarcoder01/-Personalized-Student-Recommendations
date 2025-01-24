# -Personalized-Student-Recommendations





# Personalized Student Recommendations - Project

## Project Overview

This project provides a Python-based solution to analyze quiz performance and offer personalized recommendations to students to improve their preparation. The application uses historical quiz data to identify weak areas, generate insights, and suggest actionable steps to improve the student’s quiz performance.

## Features

- Analyzes both current and historical quiz data.
- Identifies weak areas, trends in improvement, and performance gaps.
- Provides personalized recommendations on topics, question types, and difficulty levels to focus on.
- A simple web API built with Flask that can be interacted with via POST requests.

## Setup Instructions

Follow the steps below to set up the project locally.

### Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.6+
- `pip` for Python package installation

### Step 1: Clone the repository

```bash
git clone <repository_url>
cd personalized-student-recommendations
```

### Step 2: Install dependencies

Install the required Python libraries by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will install the necessary libraries:
- Flask
- pandas

### Step 3: Run the application

Once the dependencies are installed, you can start the Flask web server using the following command:

```bash
python app.py
```

This will start a web server at `http://127.0.0.1:5000/`.

### Step 4: Test the API

You can interact with the API using any API testing tool (such as Postman) or by using `curl` in your terminal. To test the POST endpoint for personalized recommendations, you can send a `POST` request to `http://127.0.0.1:5000/recommend` with the appropriate quiz data in JSON format.

### Sample Request:

```json
{
  "user_id": "123",
  "current_quiz_data": {
    "questions": [
      {"id": 1, "topic": "Math", "selected_option": 2, "correct_option": 1},
      {"id": 2, "topic": "Science", "selected_option": 3, "correct_option": 3}
    ]
  },
  "historical_quiz_data": [
    {"quiz_id": "q1", "topic": "Math", "score": 70, "question_response_map": {1: 2, 2: 3}},
    {"quiz_id": "q2", "topic": "Science", "score": 85, "question_response_map": {1: 1, 2: 2}}
  ]
}
```

### Sample Response:

```json
{
  "recommendations": [
    "Focus on improving your Math knowledge by practicing related topics.",
    "Try more practice questions with higher difficulty to boost performance."
  ]
}
```

## Project Approach

1. **Data Collection**: The application takes both current quiz data and historical quiz data for a given user.
   
2. **Data Analysis**: Using pandas, we analyze the historical data to identify trends such as weak topics, incorrect responses, and general performance gaps. We also analyze the current quiz data to provide real-time insights into how the student is performing.

3. **Recommendations**: Based on the analysis, personalized recommendations are provided. For example, the application might suggest focusing more on certain topics or attempting more difficult questions to improve performance.

4. **API Endpoint**: The application exposes a `POST` API endpoint to allow users to send their quiz data and receive personalized recommendations.

## Screenshots

### Sample Quiz Performance Data:

![Sample Quiz Performance](./screenshots/quiz-performance.png)

### Sample Recommendations:

![Sample Recommendations](./screenshots/recommendations.png)

## Insights Summary

- The application analyzes quiz data to highlight weak areas.
- Personalized recommendations focus on improvement.
- The output helps students target areas for better preparation.

## Demo Video

You can find a short demonstration video of the script in action (./demo-video.mp4).

---

### Additional Notes:

- Make sure to replace the placeholders (`<repository_url>`, `./screenshots/quiz-performance.png`, `./demo-video.mp4`, etc.) with actual links or paths based on your project folder structure.
- The images and video mentioned in the README need to be generated from your local setup or mock-ups if you're not providing actual data yet.
- The `requirements.txt` file should include all dependencies:
  ```


from flask import Flask, render_template, request, redirect


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

# Global list to store user responses
# responses = []

# from surveys import satisfaction_survey

@app.route('/')
def show_start():
    """Display the survey start page."""
    return "<h1>Welcome to the Survey!</h1>"
    # return render_template('start.html', survey=satisfaction_survey)

# @app.route('/questions/<int:question_id>')
# def show_question(question_id):
#     """Display the current question."""
#     # Check if question_id is valid

#     if question_id != len(responses):
#         return redirect(f"/questions/{len(responses)}")
    
#     question = satisfaction_survey.questions[question_id]
#     return render_template('question.html', survey=satisfaction_survey, question=question, question_id=question_id)

# @app.route('/answer', methods=['POST'])
# def handle_answer():
#     """Handle answer and redirect to next question."""
#     # Get answer from form
#     answer = request.form['answer']
    
#     # Append answer to responses
#     responses.append(answer)
    
#     # Check if all questions have been answered
#     if len(responses) < len(satisfaction_survey.questions):
#         return redirect(f"/questions/{len(responses)}")
#     else:
#         return "Survey Complete! Thank you for your responses."
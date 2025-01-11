from flask import Flask, render_template, redirect, request, flash, get_flashed_messages, session
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here' # Replace with your secret key

# Global variable to store user responses
responses = []

@app.route('/')
def show_start():
    """Display the survey start page."""
    return render_template('start.html', survey=satisfaction_survey)

@app.route('/questions/<int:question_id>')
def show_question(question_id):
    """Display the current question, ensuring users follow the correct question order."""
    responses = session.get("responses", [])

    # If the user has completed the survey, redirect to the thank you page
    if len(responses) == len(satisfaction_survey.questions):
        flash("You have already completed the survey!")
        return redirect('/complete')
    
    # If the user tries to access a question out of order, redirect to the current question
    if question_id != len(responses):
        flash("Invalid question. Please answer the question in order. Thank you!")
        return redirect(f"/questions/{len(responses)}")
    
    # If the user tries to access a question ID that doesn't exist, redirect to the correct question
    if question_id >= len(satisfaction_survey.questions):
        return redirect(f"/questions/{len(responses)}")
    
    # Otherwise, show the question
    question = satisfaction_survey.questions[question_id]
    return render_template('question.html', survey=satisfaction_survey, question=question, question_id=question_id)

@app.route('/start', methods=['POST'])
def start_survey():
    """Start the survey by clearing the responses list."""
    session["responses"] = [] # Initialize empty responses list
    return redirect('/questions/0')

@app.route('/answer', methods=['POST'])
def handle_answer():
    """Handle the answer and redirect to the next question."""
    # Get the answer from the form
    answer = request.form['answer']

    # Add the answer to the responses list
    responses = session.get("responses",[])
    responses.append(answer)
    session["responses"] = responses

    # Check if the survey is complete
    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/complete')
    else:
        # Redirect to the next question
        return redirect(f"/questions/{len(responses)}")

@app.route('/complete')
def complete():
    """Survey complete page."""
    return "Thank you for completing the survey!"

if __name__ == "__main__":
    app.run(debug=True)

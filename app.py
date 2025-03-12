# Import necessary modules
from flask import Flask, request, jsonify, render_template  # Flask framework for web handling
import random  # Used for generating random passwords
import string  # Contains different character sets (letters, digits, punctuation)
import re  # Regular expressions for password strength checking
from flask_cors import CORS  # Enables Cross-Origin Resource Sharing (CORS) for frontend-backend communication

app = Flask(__name__, static_folder="", template_folder="")  # Serve files from the same directory
CORS(app)  # Allows frontend (JavaScript) to make requests to this backend

def generate_password(length, complexity):
    """Generates a password based on the chosen complexity."""
    if complexity == "weak":
        characters = string.ascii_lowercase  # Lowercase letters only
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits  # Letters and numbers
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, numbers, and symbols
    else:
        return "Invalid complexity!"  # Handle invalid input
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def home():
    """Serves the index.html file."""
    return render_template("index.html")  # Loads the user interface from index.html


@app.route('/generate')
def generate():
    # Get parameters from the frontend (length & complexity)
    length = int(request.args.get('length'))
    complexity = request.args.get('complexity')

    # Generate a password
    password = generate_password(length, complexity)

    # Return password as a JSON response
    return jsonify({"password": password})

if __name__ == "__main__":
    # Starts the Flask application.
    app.run(host="0.0.0.0", port=5000, debug=True)

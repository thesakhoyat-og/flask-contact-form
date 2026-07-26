# Flask Contact Form App

This is a beginner-friendly Flask project that demonstrates how to handle HTML form submissions using Python.

The app displays a contact form where users can enter their name, email, and message. When the form is submitted, Flask receives the data using a POST request and saves it into a text file.

## Features

- Simple Flask web app
- Contact form using HTML
- Handles GET and POST requests
- Receives user input from a form
- Saves submitted data into a text file
- Beginner-friendly backend project
- Demonstrates basic form handling in Flask

## Technologies Used

- Python
- Flask
- HTML
- File Handling

## Project Structure

FLASK_FORM/
│
├── main.py
├── README.md
├── .gitignore
├── sample_data.txt
└── templates/
    └── contact.html

## How It Works

The user opens the contact form in the browser.

When the page is opened normally, Flask handles a GET request and displays the contact form.

When the user fills out the form and clicks submit, the browser sends a POST request to Flask.

Flask receives the submitted form data using request.form.

The submitted data is then saved into a text file using Python file handling.

## Main Flask Code

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        with open("data.txt", "a") as f:
            f.write(
                f"The name is {request.form['name']}, "
                f"the email is {request.form['email']}, "
                f"the message is {request.form.get('message', '')}\n"
            )

    return render_template("contact.html")

app.run(debug=True)

## Form Fields

The HTML form collects:

- Name
- Email
- Message

The name attributes in the HTML form must match the keys used in Flask.

Example:

name="name"
name="email"
name="message"

These match:

request.form["name"]
request.form["email"]
request.form.get("message")

## How to Run the Project

### 1. Install Flask

pip install flask

### 2. Run the Flask app

python main.py

### 3. Open the app in your browser

http://127.0.0.1:5000/

## Important Note

The file data.txt stores submitted form data.

Do not push data.txt to GitHub if it contains real names, emails, or messages.

Use .gitignore to keep private submitted data out of GitHub.

Example .gitignore:

data.txt
__pycache__/
*.pyc
.env

## Sample Data

Instead of uploading real data, you can include a sample_data.txt file with fake example content:

The name is John Doe, the email is john@example.com, the message is Hello

## What I Learned

Through this project, I learned:

- How Flask works with Python
- How to create a route in Flask
- The difference between GET and POST requests
- How HTML forms send data to the backend
- How to use request.form to get submitted data
- How to save form data into a text file
- Why return is needed in a Flask route
- Why private data should not be pushed to GitHub

## Author

Sakhoyat Hossain Siam
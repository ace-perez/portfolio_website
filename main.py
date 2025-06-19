from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Route definitions
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

# Run the application, used port 8000 because for some reason something is occupying my port 5000 lol
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

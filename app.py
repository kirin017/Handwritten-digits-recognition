from flask import Flask, render_template, request

# Initialize Flask application
app = Flask(__name__)

# Define route for the home page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
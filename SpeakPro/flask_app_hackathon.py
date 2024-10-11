from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the home page

@app.route('/recording')
def about():
    return render_template('final_recording.html')  # Renders the about page

@app.route('/profile')
def profile():
    return render_template('Profile.html')  # Renders the about page
@app.route('/signup')
def signup():
    return render_template('SignUp.html')  # Renders the about page
if __name__ == '__main__':
    app.run(debug=True)
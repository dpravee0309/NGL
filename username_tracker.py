from flask import Flask, request, redirect, render_template
import pymysql

app = Flask(__name__)

# Database connection
def save_username(username):
    connection = pymysql.connect(host='localhost', user='root', password='praveen', database='TrackerDB')
    cursor = connection.cursor()
    query = "INSERT INTO Usernames (username) VALUES (%s)"
    cursor.execute(query, (username,))
    connection.commit()
    connection.close()

# Route to display the form
@app.route('/')
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    if username:
        save_username(username)  # Save username to the database
    return redirect("https://ngl.link/praveen65230")  # Redirect to NGL

if __name__ == "__main__":
    app.run(debug=True)

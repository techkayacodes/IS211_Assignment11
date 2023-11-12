from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# A global list to store To Do items
todo_items = []

# A function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/')
def index():
    return render_template('index.html', todo_items=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    # Validate data
    if not is_valid_email(email) or priority not in ['Low', 'Medium', 'High']:
        # Redirect to the home page with an error
        return redirect(url_for('index'))

    # Add the new item to the list
    todo_items.append({'task': task, 'email': email, 'priority': priority})
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    todo_items.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

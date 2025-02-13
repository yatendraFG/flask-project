import os
from flask import Flask, render_template , request

app = Flask(__name__)
print("Templates Path:", os.path.abspath("templates"))

@app.route('/')
def form():
    return render_template('form.html')  # Ensure this matches the file name

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return f"Thank you, {name}! Your message has been received."
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

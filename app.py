from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import os
import webbrowser

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def extract_users_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        users = set()
        for tag in soup.find_all('a'): 
            users.add(tag.text.strip())
    
    return users

@app.route('/')
def upload_files():
    return render_template('upload.html')

@app.route('/result', methods=['POST'])
def result():
    if 'folder' not in request.files:
        return "No file part"
    
    folder = request.files.getlist('folder')
    
    followers_file = None
    following_file = None
    
    for file in folder:
        if file.filename.endswith('followers_1.html'):
            followers_file = file
        elif file.filename.endswith('following.html'):
            following_file = file
    
    if not followers_file or not following_file:
        return "Required files not found"
    
    followers_path = os.path.join(app.config['UPLOAD_FOLDER'], 'followers_1.html')
    following_path = os.path.join(app.config['UPLOAD_FOLDER'], 'following.html')
    
    followers_file.save(followers_path)
    following_file.save(following_path)
    
    followers = extract_users_from_html(followers_path)
    following = extract_users_from_html(following_path)
    
    not_following_back = sorted(following - followers)
    
    return render_template('result.html', users=not_following_back)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
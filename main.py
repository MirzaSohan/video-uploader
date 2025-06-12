from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/videos'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

videos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video = request.files['video']
        title = request.form['title']
        filename = video.filename
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        video.save(save_path)
        videos.append({'title': title, 'filename': filename})
        return redirect(url_for('index'))
    return render_template('index.html', videos=videos)

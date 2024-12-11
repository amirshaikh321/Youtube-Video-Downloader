from flask import Flask, render_template, request, redirect, url_for, flash
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Define the download function
def download_video(url):
    options = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Save with the video title
    }
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        return "Download completed successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        # Call the download_video function
        message = download_video(url)
        flash(message)  # Display the success/error message
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from pytubefix import YouTube
import os

app = Flask(__name__)

def descargar_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    os.makedirs("downloads", exist_ok=True)
    video.download("downloads")
    return yt.title

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None

    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            mensaje = "⚠️ Por favor, introduce un enlace válido."
        else:
            try:
                titulo = descargar_video(url)
                mensaje = f"✅ Video '{titulo}' descargado correctamente."
            except Exception as e:
                mensaje = f"❌ Error: {e}"

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

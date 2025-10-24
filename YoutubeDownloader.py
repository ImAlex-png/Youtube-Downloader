from pytubefix import YouTube
import os

def descargar_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        
        # Carpeta donde se guardarán los videos
        save_path = os.path.join(os.getcwd(), "downloads")
        os.makedirs(save_path, exist_ok=True)
        
        # Descargar video
        video.download(output_path=save_path)
        return yt.title
    
    except Exception as e:
        raise Exception(f"Error al descargar el video: {e}")
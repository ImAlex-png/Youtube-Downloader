from pytubefix import YouTube # type: ignore

link = input("Link de youtube : ")

print("Descargando...")

yt = YouTube(link)

yt.streams.get_highest_resolution().download()

print("El video se descargo correctamente en la misma carpeta que el archivo Python")
 # Aqui esta el archivo Python para descargar videos y funcionapy
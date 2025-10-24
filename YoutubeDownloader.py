from pytubefix import YouTube # type: ignore

link = input("Link de youtube : ")

print("Descargando...")

yt = YouTube(link)

yt.streams.get_highest_resolution().download()

print("El video se descargo correctamente :3")
 # Aqui esta el archivo Python para descargar videos y funcionapy
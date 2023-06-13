from pytube import YouTube

def Download(link):
    youtube = YouTube(link)
    youtube = youtube.streams.get_highest_resolution()
    try:
        youtube.download()
    except:
        print("Houve um erro ao baixar o vídeo")
        exit(1)
    print("Download is completed successfully")


link = input("Insira o link do vídeo que deseja baixar: ")
Download(link)
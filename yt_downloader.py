from pytube import YouTube

def descarregar_video(url):
    YouTube('https://www.youtube.com/watch?v=MeWGJWZ_jVo').streams.first().download()
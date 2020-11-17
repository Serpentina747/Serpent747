from moviepy.editor import VideoFileClip

def convert_to_mp3(dir):
    videoclip = VideoFileClip()
    print(dir)
    audioclip = videoclip.audio
    audioclip.write_audiofile(dir[:-4] + ".mp3")
    audioclip.close()
    videoclip.close()
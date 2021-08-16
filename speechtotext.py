import gtts as gTTS
import pyglet
import time,os

def tts(text,lang):
    file=gTTS(text=text,lanng=lang)
    filename='/tmp/temp.mp3'
    file.save(filename)
    music=pyglet.media.load(filename)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)

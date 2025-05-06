import acoustid
import chromaprint
from pydub import AudioSegment
import shutil

API_KEY = "temOqWDZUZ"

def get_fingerprint(mp3_path):
    duration, fp = acoustid.fingerprint_file(mp3_path)
    print("Duration: ", duration)
    print("Fingerprint: ", fp)

path = input("Input music directory: ")
copy = "edited_music.mp3"
shutil.copyfile(path, copy)
get_fingerprint(path)

sound = AudioSegment.from_mp3(copy)
sound.export("converted.wav", format="wav")

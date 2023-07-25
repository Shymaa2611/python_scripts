from gtts import gTTS
from pydub.playback import play
from pydub import AudioSegment

text = "hello in python world"
tts = gTTS(text=text)
tts.save('sound.mp3')
audio = AudioSegment.from_file('sound.mp3')
play(audio)
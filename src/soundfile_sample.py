#!/usr/bin/env python3

# waveだけでは読み込めないファイルへの対応

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import soundfile
import wave

SetLogLevel(0)

if not os.path.exists("/model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

filepath = sys.argv[1]
tmp_filepath = '/tmp/tmp.wav'
sf = soundfile.SoundFile(filepath)
data = sf.read(-1)
print(sf.channels)
print(sf.format)
print(sf.subtype)
print(data)
if sf.channels != 1:
    data = [sum(d) / sf.channels for d in data ]
soundfile.write(tmp_filepath, data, sf.samplerate)
wf = wave.open(tmp_filepath, "rb")

if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("/model/vosk-model-small-ja-0.22")
rec = KaldiRecognizer(model, sf.samplerate)
rec.SetWords(True)
rec.SetPartialWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        pass
        #print(rec.Result())
    else:
        pass
        #print(rec.PartialResult())

print(rec.FinalResult())
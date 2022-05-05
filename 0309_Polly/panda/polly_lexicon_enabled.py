import boto3
import contextlib
import os
polly = boto3.client('polly')

text = '先日生まれたパンダの暁暁と蕾蕾は、すくすくと成長しています。双子のお父さんパンダの名前は力力です。'
result = polly.synthesize_speech(
    Text=text, OutputFormat='mp3', VoiceId='Mizuki',
    LexiconNames=['pandaLex'])
path = 'polly_lexicon_enabled.mp3'
with contextlib.closing(result['AudioStream']) as stream:
    with open(path, 'wb') as file:
        file.write(stream.read())
if os.name == 'nt':
    os.startfile(path)
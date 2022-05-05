import boto3
import contextlib
import os
polly = boto3.client('polly')

with open('intro.txt', mode='r', encoding='utf-8') as text:
    result = polly.synthesize_speech(
        Text=text.read(), OutputFormat='mp3', VoiceId='Mizuki',
        LexiconNames=['ExLexicon'])
    path = 'polly_lexicon_enabled.mp3'
    with contextlib.closing(result['AudioStream']) as stream:
        with open(path, 'wb') as file:
            file.write(stream.read())
    if os.name == 'nt':
        os.startfile(path)
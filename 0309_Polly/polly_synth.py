# boto3をインポート
import boto3
# contextlibをインポート
import contextlib
# osをインポート
import os
# pollyサービスクライアントを作成
polly = boto3.client('polly')
# 音声合成するテキスト
text = 'こんにちは！音声合成を使ったプログラムを一緒に作りましょう。'
# テキストから音声を合成
result = polly.synthesize_speech(
    Text=text, OutputFormat='mp3', VoiceId='Mizuki')
# 出力ファイルのパス
path = 'polly_synth.mp3'
# 音声ストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
    # 出力ファイルを開く
    with open(path, 'wb') as file:
        # 音声を読み込んで出力ファイルに書き込む
        file.write(stream.read())
# 出力ファイルを再生する
if os.name == 'nt':
    os.startfile(path)

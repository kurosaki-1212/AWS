# boto3 をインポート
import boto3
# contextlib をインポート
import contextlib
# os をインポート
import os
# sys をインポート
import sys

# 引数チェック
if len(sys.argv) < 2:
  print('Usage: python lexicon_speach.py 音声合成する文章')
  exit()

# Polly サービスクライアントを作成
polly = boto3.client('polly')

# 音声合成するファイルをオープン
with open(sys.argv[1], 'r', encoding='utf-8') as speech_file:
  # 音声合成するファイルの読み込み
  text = speech_file.read()
  # 読み込んだ文章を音声合成
  result = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Mizuki',
    LexiconNames=['ExLexicon']
  )
  
# 出力ファイルのパス
path = 'ex_lexicon.mp3'
# 音声のストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
  # 出力ファイルを開く
  with open(path, 'wb') as file:
    # 音声を読み込んで出力ファイルに書き込む
    file.write(stream.read())

# 出力ファイルを再生する
if os.name == 'nt':
  os.startfile(path)
# レキシコン登録プログラム

# boto3 をインポート
import boto3
# sys をインポート
import sys

# プログラム引数のチェック
if len(sys.argv) < 2:
  print('Usage: python lexicon_regist.py ex_lexicon.pls')
  exit()

# Polly サービスクライアントを作成
polly = boto3.client('polly')

# レキシコンファイルを開く
with open(sys.argv[1], 'r', encoding='utf-8') as file:
    # レキシコンを登録
    polly.put_lexicon(Name='ExLexicon', Content=file.read())
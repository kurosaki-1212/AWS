# boto3 をインポート
import boto3
# contextlib をインポート
import contextlib
# os をインポート
import os
# リージョンを指定して、Polly サービスクライアントを作成
polly = boto3.client('polly', 'us-east-1')
# Translateサービスクライアントを作成
translate = boto3.client('translate')

# 翻訳元テキストを入力
text = input('翻訳元テキスト = ')
# 翻訳元テキストを英語に翻訳
result = translate.translate_text(
    Text=text,
    SourceLanguageCode='ja',
    TargetLanguageCode='en'
)
print(result['TranslatedText'])
# 音声合成する SSML 形式のテキスト
text_news = '''
<speak>
<amazon:domain name="news">
{}
</amazon:domain>
</speak>
'''.format(result['TranslatedText'])

# エンジンとテキスト形式を指定してテキストから音声を合成
result = polly.synthesize_speech(
    Text=text_news, # 音声合成するテキスト
    OutputFormat='mp3', # 音声のフォーマット
    VoiceId='Joanna',   # 音声ID
    Engine='neural',    # エンジン = ニューラル音声
    TextType='ssml'     # テキストのタイプ
)
# 出力ファイルのパス
path = 'polly_news.mp3'
# 音声のストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
    # 出力ファイルを開く
    with open(path, 'wb') as file:
        # 音声を読み込んで出力ファイルに書き込む
        file.write(stream.read())
# 出力ファイルを再生する
if os.name == 'nt':
    os.startfile(path)

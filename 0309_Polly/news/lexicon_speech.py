# boto3をインポート
import boto3

# Translateサービスクライアント
translate = boto3.client('translate')
polly = boto3.client('polly')

# 翻訳する日本語を入力してもらう
text = input('翻訳する日本語を入力してください')

# 翻訳する
result = translate.translate_text(
    Text=text,
    SourceLanguageCode='ja', TargetLanguageCode='en',
    TerminologyNames=['term_ja'])

text = result['TranslatedText']

result = polly.synthesize_speech(
        Text=text, OutputFormat='mp3', VoiceId='joanna',
        LexiconNames=['ExLexicon'])
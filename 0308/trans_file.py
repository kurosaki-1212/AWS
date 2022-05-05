# boto3をインポート
from fnmatch import translate
import boto3
# Translateサービスクライアント
translate = boto3.client('translate')
# (1) 入力ファイルを開く
with open('trans_file_in.txt', 'r', encoding='utf-8') as file_in:
    # 出力ファイルを開く
    with open('trans_file_out.txt', 'w', encoding='utf-8') as file_out:
        # (3) 入力ファイルを１行ずつ読み込む
        for text in file_in:
            # (4) 空行でなければ翻訳する
            if text != '\n':
                result = translate.translate_text(
                    Text=text,
                    SourceLanguageCode='ja', TargetLanguageCode='en',
                    TerminologyNames=['term_ja'])
                 # 翻訳された歴ストをファイルに書きこむ
                file_out.write(result['TranslatedText'])
            # (6) 改行ファイルに書き込む
            file_out.write('\n')
#trans_ex1.py
#boto3をインポート
import boto3
#Translateサービスクライアントを作成
translate = boto3.client('translate')
#入力ファイルを開く
with open('trans_file_in.txt', 'r', encoding='utf-8') as file_in:
    #出力ファイルを開く
    with open('trans_file_out.txt', 'w', encoding='utf-8') as file_out:
        #入力ファイルを１行ずつ読み込む
        for text in file_in:
            #空行でなければ翻訳する
            if text != '¥n':
                result = translate.translate_text(
                    Text = text,
                    SourceLanguageCode = 'ja', TargetLanguageCode = 'en',
                    TerminologyNames=['term_ja'])
                file_out.write(result['TranslatedText'])
            file_out.write('¥n')
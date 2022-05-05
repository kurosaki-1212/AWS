import boto3
import trans_term_import

#インポートを呼び出す
trans_term_import.terminology()

#クライアントの作成
translate = boto3.client('translate')

#翻訳したいファイル名
print('翻訳したいファイル名を入力してください')
trans_before = input()

#翻訳を入力するファイル名
print('翻訳先のファイルを入力してください')
trans_after = input()

#翻訳先の言語を選択
print('翻訳先の言語を選択してください')
print('1. 英語')
print('2. スペイン語')
lang_num = int(input())
if lang_num == 1:
    lang_code = 'en'
else:
    lang_code = 'es'

#各ファイルを開く
with open(trans_before, 'r', encoding = 'utf-8') as file_in:
    with open(trans_after, 'w', encoding = 'utf-8') as file_out:
        
        #１行ずつ読み込む
        for text in file_in:

            #改行じゃなければ翻訳
            if text != '\n':
                result = translate.translate_text(
                    Text = text, 
                    SourceLanguageCode = 'ja',
                    TargetLanguageCode = lang_code,
                    TerminologyNames = ['term_ja'])

                #翻訳されたテキストを書き込む
                file_out.write(result['TranslatedText'])
                print(result['TranslatedText'])

            #改行を書き込む
            file_out.write('\n')
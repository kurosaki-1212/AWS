# 例外処理
try:
    
    # boto3をインポート
    import boto3

    # Translateサービスクライアント
    translate = boto3.client('translate')

    print('--------------------------------------------------------------------')
    print('１：日本語から英語への翻訳')
    print('２：翻訳するファイル名、翻訳する言語、翻訳後のファイル名 を指定して実行')
    print('--------------------------------------------------------------------')
    select = int(input('数字を入力して下さい：'))

    # 1の場合
    if select == 1:

        # 翻訳する日本語を入力してもらう
        text = input('翻訳する日本語を入力してください')

        # 翻訳する
        result = translate.translate_text(
            Text=text,
            SourceLanguageCode='ja', TargetLanguageCode='en',
            TerminologyNames=['term_ja'])

        # 表示する
        print(result['TranslatedText'])

    # 2の場合
    elif select == 2:

        # (1) 入力ファイルを開く
        # 翻訳元のファイルを入力してもらう
        former = input('翻訳元のファイル名を入力してください')
        with open(former, 'r', encoding='utf-8') as file_in:

            # 出力ファイルを開く
            # 翻訳先のファイルを入力してもらう
            ahead = input('翻訳先のファイル名を入力してください')
            with open(ahead, 'w', encoding='utf-8') as file_out:

                # 翻訳したい言葉を入力してもらう
                lang = input("翻訳したい言語を入力してください")

                # (3) 入力ファイルを１行ずつ読み込む
                for text in file_in:

                    # (4) 空行でなければ翻訳する
                    if text != '\n':
                        result = translate.translate_text(
                            Text=text,
                            SourceLanguageCode='ja', TargetLanguageCode=lang,
                            TerminologyNames=['term_ja'])
                            
                        # 翻訳された歴ストをファイルに書きこむ
                        file_out.write(result['TranslatedText'])
                        print(result['TranslatedText'])

                    # (6) 改行ファイルに書き込む
                    file_out.write('\n')
                    
    # 1か2以外入力されたら表示する
    else:
        print("1か2の数字を入力してください")
except:
    print('数字を入力してください')
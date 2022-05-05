# 例外処理
try:

    # boto3をインポートする
    import boto3
    # contextlibについてはP90 (2)の解説を読むこと
    import contextlib
    # 音声ファイルの自動再生のためにosの機能を使用するためにimportする
    import os
    # AWSの pollyサービスを呼び出す
    polly = boto3.client('polly')
    # 読み上げさせたい内容
    text = input('読み上げさせたい文字を入力してください')
    voice = input('読み上げさせたい声を入力してください')

    # polly.synthesize_speech は音声合成の詳細を設定している
    # VoiceId = 'Mizuki' 以外の声はP94を確認
    result = polly.synthesize_speech(
        Text=text, OutputFormat='mp3', VoiceId=voice)

    # ファイル名
    path = 'polly_synth.mp3'

    # 音声ストリームの再生
    with contextlib.closing(result['AudioStream']) as stream:
        # 作成した音声出力ファイルを開く
        with open(path, 'wb') as file:
            file.write(stream.read())

    # os.name == 'nt'　は Windows
    if os.name == 'nt':
        os.startfile(path)

except:
    print('[Zenia, Zhiyu, Naja, Mads, Lotte, Ruben, Nicole, Russell, Amy, Emma, Brian, Aditi, Raveena, Ivy, Joanna, Kendra, Kimberly, Salli, Joey, Justin, Matthew, Geraint, Celine, Marlene, Vicki, Hans, Aditi, Dora, Karl, Carla, Bianca, Giorgio, Mizuki, Takumi, Seoyeon, Liv, Ewa, Maja, Jacek, Jan, Vitoria, Ricardo, Ines, Cristiano, Carman, Tatyana, Maxim, Conchita, Lucia, Enripue, Mia, Penelope, Miguel, Astrid, Filiz, Gwyneth]の中から選んでください')

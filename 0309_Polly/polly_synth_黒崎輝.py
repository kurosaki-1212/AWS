# 例外処理
try:

    # (1) boto3をインポート
    import boto3
    # (2) contextlibをインポート
    import contextlib
    # (3) osをインポート
    import os
    # (4) Pollyサービスを呼び出す
    polly = boto3.client('polly')
    # (5) 音声合成するテキスト
    text = input('読み上げさせたい文字を入力してください')
    voice = input('読み上げさせたい声を入力してください')

    # (6) テキストから音声を合成
    result = polly.synthesize_speech(
        Text=text, OutputFormat='mp3', VoiceId=voice)

    # (7) 出力ファイルのパス
    path = 'polly_synth.mp3'

    # (8) 音声のストリームを開く
    with contextlib.closing(result['AudioStream']) as stream:
        # (9) 出力ファイルを開く
        with open(path, 'wb') as file:
            # (10) 音声を読み込んで出力ファイルに書き込む
            file.write(stream.read())

    # 出力ファイルを再生する
    if os.name == 'nt':
        os.startfile(path)

# 声を出せる人の名前を表示する
except:
    print('[Zenia, Zhiyu, Naja, Mads, Lotte, Ruben, Nicole, Russell, Amy, Emma, Brian, Aditi, Raveena, Ivy, Joanna, Kendra, Kimberly, Salli, Joey, Justin, Matthew, Geraint, Celine, Marlene, Vicki, Hans, Aditi, Dora, Karl, Carla, Bianca, Giorgio, Mizuki, Takumi, Seoyeon, Liv, Ewa, Maja, Jacek, Jan, Vitoria, Ricardo, Ines, Cristiano, Carman, Tatyana, Maxim, Conchita, Lucia, Enripue, Mia, Penelope, Miguel, Astrid, Filiz, Gwyneth]の中から選んでください')

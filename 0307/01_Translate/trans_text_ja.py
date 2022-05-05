# coding: utf-8

import boto3
translate = boto3.client('translate')

text = '今日からAWSを使うよ！'

result = translate.translate_text(
    Text= text,
    SourceLanguageCode = 'ja',
    TargetLanguageCode = 'en'
)

print(result['TranslatedText'])
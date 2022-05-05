import boto3
polly = boto3.client('polly')
with open('ex_lexicon.pls', 'r', encoding='utf-8') as file:
        polly.put_lexicon(Name='ExLexicon', Content=file.read())
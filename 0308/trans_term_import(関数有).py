import boto3
def terminology():
    translate = boto3.client('translate')
    with open('term_ja.csv', 'rb') as file:
        translate.import_terminology(
            Name='term_ja',
            MergeStrategy='OVERWRITE',
            TerminologyData={'File': file.read(), 'Format': 'CSV'})
